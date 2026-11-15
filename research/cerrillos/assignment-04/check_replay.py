"""Replay the historical Cerrillos annotations in a temporary local workspace.

The only excluded comparison field is dependencies.python. All other fields,
including library versions and input/workflow/specification hashes, must match.
No source downloads, model calls, or human-decision updates are performed.
"""

import argparse
from copy import deepcopy
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent


def digest(data):
    return sha256(data).hexdigest()


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def normalized(packet):
    result = deepcopy(packet)
    del result["dependencies"]["python"]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional generated packet path outside this package, for example /tmp/cerrillos-replayed-packet.json")
    args = parser.parse_args()
    if args.output and args.output.resolve().is_relative_to(HERE):
        parser.error("Write generated output outside this package; historical records are preserved.")
    started = utc_now()
    before = {p.name: digest(p.read_bytes()) for p in HERE.iterdir() if p.is_file()}
    expected_bytes = (HERE / "review-packet.json").read_bytes()
    expected = json.loads(expected_bytes)
    historical = json.loads((HERE / "run-receipt.json").read_bytes())
    mapping = {"SPEC.md": "SPEC-original.txt", **{name: name for name in ("cases.json", "workflow.py", "test_workflow.py", "requirements.txt", "review-packet.json")}}
    for name, public_name in mapping.items():
        if before[public_name] != historical["files_sha256"][name]:
            raise ValueError(f"Historical input digest mismatch: {public_name}")
    with TemporaryDirectory(prefix="cerrillos-replay-") as temporary:
        work = Path(temporary)
        for public_name, runtime_name in (("workflow.py", "workflow.py"), ("test_workflow.py", "test_workflow.py"), ("cases.json", "cases.json"), ("SPEC-original.txt", "SPEC.md")):
            (work / runtime_name).write_bytes((HERE / public_name).read_bytes())
        tests = subprocess.run([sys.executable, "-B", "-m", "unittest", "-v", "test_workflow"], cwd=work, capture_output=True, text=True, timeout=120)
        test_match = re.search(r"Ran (\d+) tests?", tests.stderr)
        if tests.returncode != 0 or not test_match:
            raise RuntimeError("Historical tests failed:\n" + tests.stdout + tests.stderr)
        tests_run = int(test_match.group(1))
        if tests_run != historical["test_suite"]["passed"]:
            raise ValueError("Test count differs from the historical suite")
        replay = subprocess.run([sys.executable, "-B", "workflow.py", "--cases", "cases.json"], cwd=work, capture_output=True, timeout=120)
        if replay.returncode != 0:
            raise RuntimeError("Replay failed:\n" + replay.stderr.decode("utf-8", errors="replace"))
    actual = json.loads(replay.stdout)
    if actual["dependencies"]["python"] != platform.python_version():
        raise ValueError("Generated packet does not identify the running Python version")
    if normalized(actual) != normalized(expected):
        raise ValueError("Replay differs beyond the permitted Python-version metadata field")
    if actual["runtime_model"] is not None or actual["hosted_tracing"] is not False:
        raise ValueError("Unexpected runtime model or tracing state")
    if actual["review_status"] != "pending_human_review" or any(c["review_status"] != "pending_human_review" for c in actual["claims"]):
        raise ValueError("Replay must preserve provisional graph statuses")
    if any(digest((HERE / name).read_bytes()) != value for name, value in before.items()):
        raise ValueError("A package input changed during the replay")
    if args.output:
        args.output.write_bytes(replay.stdout)
    report = {
        "record_type": "Publication replay receipt",
        "started_at_utc": started,
        "completed_at_utc": utc_now(),
        "historical_run_recorded_at_utc": historical["recorded_at_utc"],
        "historical_source_receipt": "run-receipt.json",
        "scope": "Tests and replay of unchanged annotated case data in a temporary directory; no original-source reinspection or byte-hash recheck.",
        "execution_commands": ["python -B -m unittest -v test_workflow", "python -B workflow.py --cases cases.json"],
        "input_files_sha256": {public_name: before[public_name] for public_name in mapping.values()},
        "checker_sha256": before["check_replay.py"],
        "historical_receipt_sha256": before["run-receipt.json"],
        "human_review_record_sha256": before["human-review.json"],
        "runtime": actual["dependencies"],
        "tests": {"run": tests_run, "passed": tests_run, "failed": 0, "output": (tests.stdout + tests.stderr).strip()},
        "packet_comparison": {
            "all_fields_except_python_version_match": True,
            "excluded_field": "dependencies.python",
            "historical_python": expected["dependencies"]["python"],
            "replay_python": actual["dependencies"]["python"],
            "byte_identical": replay.stdout == expected_bytes,
            "historical_packet_sha256": digest(expected_bytes),
            "replayed_packet_sha256": digest(replay.stdout),
            "generated_packet_written_outside_package": args.output is not None,
        },
        "candidate_counts": actual["counts"],
        "runtime_model_calls": 0,
        "hosted_tracing": False,
        "original_source_hashes_rechecked": False,
        "package_inputs_unchanged": True,
        "human_decisions_changed": False,
        "limitations": ["Matching output reproduces supplied annotations; it does not independently validate source interpretation.", "No new human fidelity review, original-source download, field observation or calibration assessment occurred.", "Only Python-version metadata is excluded from the portable comparison; library versions, claims, annotations and input hashes must match."],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f"Cannot validate replay: {error}", file=sys.stderr)
        raise SystemExit(1)
