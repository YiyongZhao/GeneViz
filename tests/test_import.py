"""Basic import and CLI tests for GeneViz."""

def test_import():
    import geneviz
    assert geneviz.__version__ == "1.0.0"

def test_version():
    import subprocess
    result = subprocess.run(["python", "-m", "geneviz.GeneViz", "--version"],
                            capture_output=True, text=True)
    assert "1.0.0" in result.stdout or "1.0.0" in result.stderr
