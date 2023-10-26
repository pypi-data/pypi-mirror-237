from otSpec.table import head


def test_getMacStyleBitNames():
    assert head.getMacStyleBitNames(head.macStyle_BOLD | head.macStyle_ITALIC) == [
        "Bold",
        "Italic",
    ]
