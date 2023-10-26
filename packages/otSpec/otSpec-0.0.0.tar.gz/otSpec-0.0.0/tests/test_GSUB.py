from otSpec.table import GSUB


def test_getLookupTypeName():
    assert GSUB.getLookupTypeName(GSUB.GSUB_LOOKUP_SINGLE) == "Single"