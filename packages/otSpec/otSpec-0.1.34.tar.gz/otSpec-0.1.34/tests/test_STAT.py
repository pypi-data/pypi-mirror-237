from otSpec.table import STAT


def test_getAxisName():
    assert STAT.getAxisName("opsz") == "Optical size"