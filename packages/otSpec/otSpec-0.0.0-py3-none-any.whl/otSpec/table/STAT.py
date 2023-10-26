OLDER_SIBLING_FONT_ATTRIBUTE = 0x0001
ELIDABLE_AXIS_VALUE_NAME = 0x0002

AxisTagToNameMap = {
    "ital": "Italic",
    "opsz": "Optical size",
    "slnt": "Slant",
    "wdth": "Width",
    "wght": "Weight",
}

def getAxisName(axisTag):
    return AxisTagToNameMap.get(axisTag)