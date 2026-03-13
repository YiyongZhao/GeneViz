"""Basic tests for MicroSynViz core module."""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_import():
    import microsynviz
    assert hasattr(microsynviz, '__version__')
    assert microsynviz.__version__ == "1.0.0"


def test_parse_attributes_gff3():
    from microsynviz.core import parse_attributes
    result = parse_attributes("ID=gene01;Name=ABC;Parent=chr1")
    assert result['ID'] == 'gene01'
    assert result['Name'] == 'ABC'
    assert result['Parent'] == 'chr1'


def test_parse_attributes_gtf():
    from microsynviz.core import parse_attributes
    result = parse_attributes('gene_id "ENSG001"; transcript_id "ENST001";')
    assert result['gene_id'] == 'ENSG001'
    assert result.get('ID') is not None


def test_parse_region_valid():
    from microsynviz.core import parse_region
    chrom, start, end = parse_region("Chr1:1000-5000")
    assert chrom == "Chr1"
    assert start == 1000
    assert end == 5000


def test_parse_region_invalid():
    from microsynviz.core import parse_region
    with pytest.raises(ValueError):
        parse_region("bad_format")


def test_parse_region_start_gt_end():
    from microsynviz.core import parse_region
    with pytest.raises(ValueError):
        parse_region("Chr1:5000-1000")


def test_xml_escape():
    from microsynviz.core import xml_escape
    assert xml_escape('A<B>C&D"E') == "A&lt;B&gt;C&amp;D&quot;E"
    assert xml_escape(None) == ""


def test_detect_format_gff(tmp_path):
    from microsynviz.core import detect_format
    gff = tmp_path / "test.gff"
    gff.write_text("chr1\tmaker\tgene\t100\t200\t.\t+\t.\tID=gene01\n")
    assert detect_format(str(gff)) == 'gff'


def test_detect_format_bed(tmp_path):
    from microsynviz.core import detect_format
    bed = tmp_path / "test.bed"
    bed.write_text("chr1\t100\t200\tgene01\t0\t+\n")
    assert detect_format(str(bed)) == 'bed'


def test_format_error():
    from microsynviz.core import FormatError
    err = FormatError('gff', 'test.gff', 'bad_line_here')
    assert 'gff' in str(err)
    assert 'test.gff' in str(err)
