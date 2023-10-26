from otSpec.table import OS2
from otSpec.cpg import data as codepage


def test_getfsSelectionBitNames():
    fsSelection = OS2.fsSelection_BOLD | OS2.fsSelection_ITALIC
    assert OS2.getfsSelectionBitNames(fsSelection) == ["Italic", "Bold"]


def test_getEmbeddingDescription():
    assert (
        OS2.getEmbeddingDescription(OS2.fsType_PrintPreviewEmbedding)
        == "Print & Preview embedding"
    )


# def test_getUnicodeRange1Bits():
#     assert OS2.getUnicodeRange1Bits(codepage["cp1252"]) == 1

def test_getCodePageRange1Bits():
    assert OS2.getCodePageRange1Bits(codepage["cp1252"]) == 1
