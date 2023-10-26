from otSpec.table import GPOS


def test_getLookupTypeName():
    assert GPOS.getLookupTypeName(GPOS.GPOS_LOOKUP_SINGLE) == "Single adjustment"
