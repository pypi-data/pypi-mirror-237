from otSpec.table import name


def test_getPlatformName():
    assert name.getPlatformName(name.PLATFORM_UNI) == "Unicode"


def test_getUnicodeEncodingName():
    assert name.getUnicodeEncodingName(name.UNI_2_BMP) == "Unicode 2.0 BMP only"


def test_getMacEncodingName():
    assert name.getMacEncodingName(name.MAC_ROMAN) == "Roman"


def test_getWinEncodingName():
    assert name.getWinEncodingName(name.WIN_UNI) == "Unicode BMP"


def test_getLanguageName():
    assert name.getLanguageName(0x0409) == "English - US"


def test_getLanguageID():
    assert name.getLanguageID("English - US") == 0x0409


def test_nameID():
    assert name.getNameDescription(0) == "Copyright notice"
