from otSpec.table import MVAR


def test_getMVARtagName():
    assert MVAR.getMVARtagName("hasc") == "horizontal ascender"


def test_getMVARtagTargetTable():
    assert MVAR.getMVARtagTargetTable("hasc") == "OS/2"


def test_getMVARtagTargetAttribute():
    assert MVAR.getMVARtagTargetAttribute("hasc") == "sTypoAscender"
