import re
import subprocess
from pathlib import Path

OUTPUT_FILE = Path("/app/output.txt")


def run_solution():
    subprocess.run(["./solution.sh"], check=True)


def test_output_exists_and_is_sha256():
    run_solution()

    assert OUTPUT_FILE.exists()

    out = OUTPUT_FILE.read_text().strip()
    assert re.fullmatch(r"[a-f0-9]{64}", out)


def test_exact_expected_hash():
    run_solution()

    out = OUTPUT_FILE.read_text().strip()

    expected = (
        subprocess.check_output(
            ["bash", "-c", "echo -n 2377126 | sha256sum | awk '{print $1}'"]
        )
        .decode()
        .strip()
    )

    assert out == expected


def test_deterministic_output():
    run_solution()

    first = OUTPUT_FILE.read_text()

    run_solution()
    second = OUTPUT_FILE.read_text()

    assert first == second


def test_duplicate_ids_exist_in_log():
    log = Path("/app/assets/server.log").read_text()
    assert log.count("request_id=17") > 1


def test_malformed_ids_exist_in_log():
    log = Path("/app/assets/server.log").read_text()
    assert "request_id=abc" in log
