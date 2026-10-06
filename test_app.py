import subprocess
import sys


def run_script(filename):
    return subprocess.run(
        [sys.executable, filename],
        capture_output=True,
        text=True,
    )


def test_helloworld_runs_and_prints_greeting():
    result = run_script("helloworld.py")
    assert result.returncode == 0
    assert "Hello World" in result.stdout


def test_profile_runs_and_prints_profile():
    result = run_script("profile.py")
    assert result.returncode == 0
    assert "profile" in result.stdout
