"""Basic import and CLI tests for MicroSynViz."""

def test_import():
    import microsynviz
    assert microsynviz.__version__ == "1.0.0"

def test_version():
    import subprocess
    result = subprocess.run(["python", "-m", "microsynviz.MicroSynViz", "--version"],
                            capture_output=True, text=True)
    assert "1.0.0" in result.stdout or "1.0.0" in result.stderr
