"""Basic import and CLI tests for MicroSynViz."""

def test_import():
    import microsynviz
    assert microsynviz.__version__ == "1.0.0"

def test_version():
    import subprocess
    result = subprocess.run(["python", "-m", "microsynviz", "--version"],
                            capture_output=True, text=True)
    assert "1.0.0" in result.stdout or "1.0.0" in result.stderr

def test_core_import():
    from microsynviz.core import parse_region
    # Test region parsing
    chrom, start, end = parse_region("Chr1:1000-5000")
    assert chrom == "Chr1"
    assert start == 1000
    assert end == 5000
