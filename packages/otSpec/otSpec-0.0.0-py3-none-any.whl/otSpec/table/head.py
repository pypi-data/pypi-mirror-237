# flags
flag_BaselineAtZero = 2 ** 0  # bit  0
flag_LeftSidebearingAtZero = 2 ** 1  # bit  1
flag_InstructionsDependOnPtSize = 2 ** 2  # bit  2
flag_ForceppemToInt = 2 ** 3  # bit  3
flag_InstructionsAlterWidth = 2 ** 4  # bit  4
flag_FontDataIsLossless = 2 ** 11  # bit 11
flag_FontConverted = 2 ** 12  # bit 12
flag_FontOptimizedForClearType = 2 ** 13  # bit 13
flag_LastResortFont = 2 ** 14  # bit 13

flagToNameMap = {
flag_BaselineAtZero : "Baseline for font at y=0",
flag_LeftSidebearingAtZero : "Left sidebearing point at x=0",
flag_InstructionsDependOnPtSize : "Instructions may depend on point size",
flag_ForceppemToInt : "Force ppem to integer values for scaler math",
flag_InstructionsAlterWidth : "Instructions may alter advance width",
flag_FontDataIsLossless : "Font data is lossless",
flag_FontConverted : "Font converted",
flag_FontOptimizedForClearType : "Font optimized for ClearType",
flag_LastResortFont : "Last Resort font",
}

# macStyle bits
macStyle_BOLD = 2 ** 0  # macStyle bit 0
macStyle_ITALIC = 2 ** 1  # macStyle bit 1
macStyle_UNDERLINE = 2 ** 2  # macStyle bit 2
macStyle_OUTLINE = 2 ** 3  # macStyle bit 3
macStyle_SHADOW = 2 ** 4  # macStyle bit 4
macStyle_CONDENSED = 2 ** 5  # macStyle bit 5
macStyle_EXTENDED = 2 ** 6  # macStyle bit 6
# Bits 7-15: Reserved (set to 0).

macStyleToNameMap = {
    macStyle_BOLD: "Bold",
    macStyle_ITALIC: "Italic",
    macStyle_UNDERLINE: "Underline",
    macStyle_OUTLINE: "Outline",
    macStyle_SHADOW: "Shadow",
    macStyle_CONDENSED: "Condensed",
    macStyle_EXTENDED: "Extended",
}


def getMacStyleBitNames(macStyle):
    styleBitNames = []
    for bit in macStyleToNameMap:
        if macStyle & bit:
            styleBitNames.append(macStyleToNameMap[bit])
    return styleBitNames
