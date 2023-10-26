from unicodedata import category
from .. import cpg

# fsSelection bits
fsSelection_ITALIC = 1 << 0  # fsSelection bit 0
fsSelection_UNDERSCORE = 1 << 1  # fsSelection bit 1
fsSelection_NEGATIVE = 1 << 2  # fsSelection bit 2
fsSelection_OUTLINED = 1 << 3  # fsSelection bit 3
fsSelection_STRIKEOUT = 1 << 4  # fsSelection bit 4
fsSelection_BOLD = 1 << 5  # fsSelection bit 5
fsSelection_REGULAR = 1 << 6  # fsSelection bit 6
fsSelection_USE_TYPO_METRICS = 1 << 7  # fsSelection bit 7
fsSelection_WWS = 1 << 8  # fsSelection bit 8
fsSelection_OBLIQUE = 1 << 9  # fsSelection bit 9

# fsSelection bits defined in OS/2 tabele version 0 - 3
fsSelection_OS2_v3_mask = (
    fsSelection_ITALIC
    | fsSelection_UNDERSCORE
    | fsSelection_NEGATIVE
    | fsSelection_OUTLINED
    | fsSelection_STRIKEOUT
    | fsSelection_BOLD
    | fsSelection_REGULAR
)
# fsSelection bits defined in OS/2 tabele version 4 - 5
fsSelection_OS2_v4_mask = (
    fsSelection_OS2_v3_mask
    | fsSelection_USE_TYPO_METRICS
    | fsSelection_WWS
    | fsSelection_OBLIQUE
)


def get_fsSelection_mask(OS2table):
    """
    Mask for valid fsSelection bits.
    """
    if 0 <= OS2table.version <= 3:
        return fsSelection_OS2_v3_mask
    if 4 <= OS2table.version <= 5:
        return fsSelection_OS2_v4_mask


fsSelectionToStyleNameMap = {
    fsSelection_ITALIC: "Italic",
    fsSelection_UNDERSCORE: "Underscore",
    fsSelection_NEGATIVE: "Negative",
    fsSelection_OUTLINED: "Outline",
    fsSelection_STRIKEOUT: "Strikeout",
    fsSelection_BOLD: "Bold",
    fsSelection_REGULAR: "Regular",
    fsSelection_OBLIQUE: "Oblique",
}


def getfsSelectionStyleBitNames(fsSelection):
    styleBitNames = []
    for bit in fsSelectionToStyleNameMap:
        if fsSelection & bit:
            styleBitNames.append(fsSelectionToStyleNameMap[bit])
    return styleBitNames


fsSelectionBitToNameMap = {
    fsSelection_ITALIC: "Italic",
    fsSelection_UNDERSCORE: "Underscore",
    fsSelection_NEGATIVE: "Negative",
    fsSelection_OUTLINED: "Outline",
    fsSelection_STRIKEOUT: "Strikeout",
    fsSelection_BOLD: "Bold",
    fsSelection_REGULAR: "Regular",
    fsSelection_USE_TYPO_METRICS: "Use Typo Metric",
    fsSelection_WWS: "WWS Names",
    fsSelection_OBLIQUE: "Oblique",
}


def getfsSelectionBitNames(fsSelection):
    bitNames = []
    for bit in fsSelectionBitToNameMap:
        if fsSelection & bit:
            bitNames.append(fsSelectionBitToNameMap[bit])
    return bitNames


# fsType bits AKA embedding bits
fsType_reserved_0 = 1 << 0  # fsType bit 0 reserved
fsType_NoEmbedding = 1 << 1  # fsType bit 1
fsType_PrintPreviewEmbedding = 1 << 2  # fsType bit 2
fsType_EditableEmbedding = 1 << 3  # fsType bit 3
fsType_reserved_4 = 1 << 4  # fsType bit 4 reserved
fsType_reserved_5 = 1 << 5  # fsType bit 5 reserved
fsType_reserved_6 = 1 << 6  # fsType bit 6 reserved
fsType_reserved_7 = 1 << 7  # fsType bit 7 reserved
fsType_NoSubsetting = 1 << 8  # fsType bit 8
fsType_BitmapOnly = 1 << 9  # fsType bit 9
fsType_reserved_10 = 1 << 10  # fsType bit 10 reserved
fsType_reserved_11 = 1 << 11  # fsType bit 11 reserved
fsType_reserved_12 = 1 << 12  # fsType bit 12 reserved
fsType_reserved_13 = 1 << 13  # fsType bit 13 reserved
fsType_reserved_14 = 1 << 14  # fsType bit 14 reserved
fsType_reserved_15 = 1 << 15  # fsType bit 15 reserved

fsType_EmbeddingMask = 0x000F
fsType_SubsettingMask = 0x0100
fsType_BitmapMask = 0x0200
fsType_invalidMask = (
    fsType_reserved_0
    | fsType_reserved_4
    | fsType_reserved_5
    | fsType_reserved_6
    | fsType_reserved_7
    | fsType_reserved_10
    | fsType_reserved_11
    | fsType_reserved_12
    | fsType_reserved_13
    | fsType_reserved_14
    | fsType_reserved_15
)


def getEmbeddingDescription(fsType):
    if fsType & fsType_invalidMask:
        return "Invalid embedding settings"
    embedding = fsType & fsType_EmbeddingMask
    if not embedding:
        result = "Installable embedding"
    elif embedding == fsType_NoEmbedding:
        result = "No embedding allowed"
    elif embedding == fsType_PrintPreviewEmbedding:
        result = "Print & Preview embedding"
    elif embedding == fsType_EditableEmbedding:
        result = "Editable embedding"
    else:
        return "Invalid embedding settings"
    if fsType & fsType_NoSubsetting:
        result += ", No subsetting"
    if fsType & fsType_BitmapOnly:
        result += ", Bitmap embedding only"
    return result


# usWeightClass
FW_THIN = 100
FW_EXTRALIGHT = 200
FW_LIGHT = 300
FW_NORMAL = 400
FW_MEDIUM = 500
FW_SEMIBOLD = 600
FW_BOLD = 700
FW_EXTRABOLD = 800
FW_BLACK = 900

weightClassToNameMap = {
    FW_THIN: "Thin",
    FW_EXTRALIGHT: "Extra-light (Ultra-light)",
    FW_LIGHT: "Light",
    FW_NORMAL: "Normal (Regular)",
    FW_MEDIUM: "Medium",
    FW_SEMIBOLD: "Semi-bold (Demi-bold)",
    FW_BOLD: "Bold",
    FW_EXTRABOLD: "Extra-bold (Ultra-bold)",
    FW_BLACK: "Black (Heavy)",
}
# usWidthClass
FWIDTH_ULTRA_CONDENSED = 1
FWIDTH_EXTRA_CONDENSED = 2
FWIDTH_CONDENSED = 3
FWIDTH_SEMI_CONDENSED = 4
FWIDTH_NORMAL = 5
FWIDTH_SEMI_EXPANDED = 6
FWIDTH_EXPANDED = 7
FWIDTH_EXTRA_EXPANDED = 8
FWIDTH_ULTRA_EXPANDED = 9

widthClassToNameMap = {
    FWIDTH_ULTRA_CONDENSED: "Ultra-condensed",
    FWIDTH_EXTRA_CONDENSED: "Extra-condensed",
    FWIDTH_CONDENSED: "Condensed",
    FWIDTH_SEMI_CONDENSED: "Semi-condensed",
    FWIDTH_NORMAL: "Medium (normal)",
    FWIDTH_SEMI_EXPANDED: "Semi-expanded",
    FWIDTH_EXPANDED: "Expanded",
    FWIDTH_EXTRA_EXPANDED: "Extra-expanded",
    FWIDTH_ULTRA_EXPANDED: "Ultra-expanded",
}

# Unicode Character Range
# see http://www.microsoft.com/typography/otspec/os2.htm#ur

UnicodeRange1 = {
    1 << 0: set(range(0x0000, 0x007F + 1)),  # Basic Latin
    1 << 1: set(range(0x0080, 0x00FF + 1)),  # Latin-1 Supplement
    1 << 2: set(range(0x0100, 0x017F + 1)),  # Latin Extended-A
    1 << 3: set(range(0x0180, 0x024F + 1)),  # Latin Extended-B
    1
    << 4: set(
        list(range(0x0250, 0x02AF + 1))  # IPA Extensions
        + list(range(0x1D00, 0x1D7F + 1))  # Phonetic Extensions
        + list(range(0x1D80, 0x1DBF + 1))  # Phonetic Extensions Supplement
    ),
    1
    << 5: set(
        list(range(0x02B0, 0x02FF + 1))  # Spacing Modifier Letters
        + list(range(0xA700, 0xA71F + 1))  # Modifier Tone Letters
    ),
    1
    << 6: set(
        list(range(0x0300, 0x036F + 1))  # Combining Diacritical Marks
        + list(range(0x1DC0, 0x1DFF + 1))  # Combining Diacritical Marks Supplement
    ),
    1 << 7: set(list(range(0x0370, 0x03FF + 1))),  # Greek and Coptic
    1 << 8: set(list(range(0x2C80, 0x2CFF + 1))),  # Coptic
    1
    << 9: set(
        list(range(0x0400, 0x04FF + 1))  # Cyrillic
        + list(range(0x0500, 0x052F + 1))  # Cyrillic Supplement
        + list(range(0x2DE0, 0x2DFF + 1))  # Cyrillic Extended-A
        + list(range(0xA640, 0xA69F + 1))  # Cyrillic Extended-B
    ),
    1 << 10: set(range(0x0530, 0x058F + 1)),  # Armenian
    1 << 11: set(range(0x0590, 0x05FF + 1)),  # Hebrew
    1 << 12: set(range(0xA500, 0xA63F + 1)),  # Vai
    1
    << 13: set(
        list(range(0x0600, 0x06FF + 1))  # Arabic
        + list(range(0x0750, 0x077F + 1))  # Arabic Supplement
    ),
    1 << 14: set(range(0x07C0, 0x07FF + 1)),  # NKo
    1 << 15: set(range(0x0900, 0x097F + 1)),  # Devanagari
    1 << 16: set(range(0x0980, 0x09FF + 1)),  # Bengali
    1 << 17: set(range(0x0A00, 0x0A7F + 1)),  # Gurmukhi
    1 << 18: set(range(0x0A80, 0x0AFF + 1)),  # Gujarati
    1 << 19: set(range(0x0B00, 0x0B7F + 1)),  # Oriya
    1 << 20: set(range(0x0B80, 0x0BFF + 1)),  # Tamil
    1 << 21: set(range(0x0C00, 0x0C7F + 1)),  # Telugu
    1 << 22: set(range(0x0C80, 0x0CFF + 1)),  # Kannada
    1 << 23: set(range(0x0D00, 0x0D7F + 1)),  # Malayalam
    1 << 24: set(range(0x0E00, 0x0E7F + 1)),  # Thai
    1 << 25: set(range(0x0E80, 0x0EFF + 1)),  # Lao
    1
    << 26: set(
        list(range(0x10A0, 0x10FF + 1))  # Georgian
        + list(range(0x2D00, 0x2D2F + 1))  # Georgian Supplement
    ),
    1 << 27: set(range(0x1B00, 0x1B7F + 1)),  # Balinese
    1 << 28: set(range(0x1100, 0x11FF + 1)),  # Hangul Jamo
    1
    << 29: set(
        list(range(0x1E00, 0x1EFF + 1))  # Latin Extended Additional
        + list(range(0x2C60, 0x2C7F + 1))  # Latin Extended-C
        + list(range(0xA720, 0xA7FF + 1))  # Latin Extended-D
    ),
    1 << 30: set(range(0x1F00, 0x1FFF + 1)),  # Greek Extended
    1
    << 31: set(
        list(range(0x2000, 0x206F + 1))  # General Punctuation
        + list(range(0x2E00, 0x2E7F + 1))  # Supplemental Punctuation
    ),
}

UnicodeRange1bitToNameMap = {
    1 << 0: "Basic Latin",
    1 << 1: "Latin-1 Supplement",
    1 << 2: "Latin Extended-A",
    1 << 3: "Latin Extended-B",
    1 << 4: "IPA Extensions",
    1 << 5: "Spacing Modifier Letters",
    1 << 6: "Combining Diacritical Marks",
    1 << 7: "Greek and Coptic",
    1 << 8: "Coptic",
    1 << 9: "Cyrillic",
    1 << 10: "Armenian",
    1 << 11: "Hebrew",
    1 << 12: "Vai",
    1 << 13: "Arabic",
    1 << 14: "NKo",
    1 << 15: "Devanagari",
    1 << 16: "Bengali",
    1 << 17: "Gurmukhi",
    1 << 18: "Gujarati",
    1 << 19: "Oriya",
    1 << 20: "Tamil",
    1 << 21: "Telugu",
    1 << 22: "Kannada",
    1 << 23: "Malayalam",
    1 << 24: "Thai",
    1 << 25: "Lao",
    1 << 26: "Georgian",
    1 << 27: "Balinese",
    1 << 28: "Hangul Jamo",
    1 << 29: "Latin Extended Additional",
    1 << 30: "Greek Extended",
    1 << 31: "General Punctuation",
}

UnicodeRange2 = {
    2**0: set([*range(0x2070, 0x209F + 1)]),  # Superscripts And Subscripts
    2**1: set([*range(0x20A0, 0x20CF + 1)]),  # Currency Symbols
    2
    ** 2: set([*range(0x20D0, 0x20FF + 1)]),  # Combining Diacritical Marks For Symbols
    2**3: set([*range(0x2100, 0x214F + 1)]),  # Letterlike Symbols
    2**4: set([*range(0x2150, 0x218F + 1)]),  # Number Forms
    2
    ** 5: set(
        [*range(0x2190, 0x21FF + 1)]  # Arrows
        + [*range(0x27F0, 0x27FF + 1)]  # Supplemental Arrows-A
        + [*range(0x2900, 0x297F + 1)]  # Supplemental Arrows-B
        + [*range(0x2B00, 0x2BFF + 1)]
    ),  # Miscellaneous Symbols and Arrows
    2
    ** 6: set(
        [*range(0x2200, 0x22FF + 1)]  # Mathematical Operators
        + [*range(0x2A00, 0x2AFF + 1)]  # Supplemental Mathematical Operators
        + [*range(0x27C0, 0x27EF + 1)]  # Miscellaneous Mathematical Symbols-A
        + [*range(0x2980, 0x29FF + 1)]# Miscellaneous Mathematical Symbols-B
    ),  
    2**7: set([*range(0x2300, 0x23FF + 1)]),  # Miscellaneous Technical
    2**8: set([*range(0x2400, 0x243F + 1)]),  # Control Pictures
    2**9: set([*range(0x2440, 0x245F + 1)]),  # Optical Character Recognition
    2**10: set([*range(0x2460, 0x24FF + 1)]),  # Enclosed Alphanumerics
    2**11: set([*range(0x2500, 0x257F + 1)]),  # Box Drawing
    2**12: set([*range(0x2580, 0x259F + 1)]),  # Block Elements
    2**13: set([*range(0x25A0, 0x25FF + 1)]),  # Geometric Shapes
    2**14: set([*range(0x2600, 0x26FF + 1)]),  # Miscellaneous Symbols
    2**15: set([*range(0x2700, 0x27BF + 1)]),  # Dingbats
    2**16: set([*range(0x3000, 0x303F + 1)]),  # CJK Symbols And Punctuation
    2**17: set([*range(0x3040, 0x309F + 1)]),  # Hiragana
    2
    ** 18: set(
        [*range(0x30A0, 0x30FF + 1)] # Katakana
        + [*range(0x31F0, 0x31FF + 1)]  # Katakana Phonetic Extensions
    ),  
    2
    ** 19: set(
        [*range(0x3100, 0x312F + 1)]   # Bopomofo
        + [*range(0x31A0, 0x31BF + 1)]  # Bopomofo Extended
    ),
    2**20: set([*range(0x3130, 0x318F + 1)]),  # Hangul Compatibility Jamo
    2**21: set([*range(0xA840, 0xA87F + 1)]),  # Phags-pa
    2**22: set([*range(0x3200, 0x32FF + 1)]),  # Enclosed CJK Letters And Months
    2**23: set([*range(0x3300, 0x33FF + 1)]),  # CJK Compatibility
    2**24: set([*range(0xAC00, 0xD7AF + 1)]),  # Hangul Syllables
    2**25: set([*range(0x10000, 0x10FFF + 1)]),  # Non-Plane 0 *
    2**26: set([*range(0x10900, 0x1091F + 1)]),  # Phoenician
    2
    ** 27: set(
        [*range(0x4E00, 0x9FFF + 1)]  # CJK Unified Ideographs
        + [*range(0x2E80, 0x2EFF + 1)]  # CJK Radicals Supplement
        + [*range(0x2F00, 0x2FDF + 1)]  # Kangxi Radicals
        + [*range(0x2FF0, 0x2FFF + 1)]  # Ideographic Description Characters
        + [*range(0x3400, 0x4DBF + 1)]  # CJK Unified Ideographs Extension A
        + [*range(0x20000, 0x2A6DF + 1)]  # CJK Unified Ideographs Extension B
        + [*range(0x3190, 0x319F + 1)]# Kanbun
    ),  
    2**28: set([*range(0xE000, 0xF8FF + 1)]),  # Private Use Area (plane 0)
    2
    ** 29: set(
        [*range(0x31C0, 0x31EF + 1)]  # CJK Strokes
        + [*range(0xF900, 0xFAFF + 1)]  # CJK Compatibility Ideographs
        + [*range(0x2F800, 0x2FA1F + 1)]# CJK Compatibility Ideographs Supplement
    ),  
    2**30: set([*range(0xFB00, 0xFB4F + 1)]),  # Alphabetic Presentation Forms
    2**31: set([*range(0xFB50, 0xFDFF + 1)]),  # Arabic Presentation Forms-A
}

UnicodeRange2bitToNameMap = {
    2**0: "Superscripts And Subscripts",
    2**1: "Currency Symbols",
    2**2: "Combining Diacritical Marks For Symbols",
    2**3: "Letterlike Symbols",
    2**4: "Number Forms",
    2**5: "Arrows",
    2**6: "Mathematical Operators",
    2**7: "Miscellaneous Technical",
    2**8: "Control Pictures",
    2**9: "Optical Character Recognition",
    2**10: "Enclosed Alphanumerics",
    2**11: "Box Drawing",
    2**12: "Block Elements",
    2**13: "Geometric Shapes",
    2**14: "Miscellaneous Symbols",
    2**15: "Dingbats",
    2**16: "CJK Symbols And Punctuation",
    2**17: "Hiragana",
    2**18: "Katakana",
    2**19: "Bopomofo",
    2**20: "Hangul Compatibility Jamo",
    2**21: "Phags-pa",
    2**22: "Enclosed CJK Letters And Months",
    2**23: "CJK Compatibility",
    2**24: "Hangul Syllables",
    2**25: "Non-Plane 0",
    2**26: "Phoenician",
    2**27: "CJK Unified Ideographs",
    2**28: "Private Use Area (plane 0)",
    2**29: "CJK Strokes",
    2**30: "Alphabetic Presentation Forms",
    2**31: "Arabic Presentation Forms-A",
}

UnicodeRange3 = {
    2**0: set([*range(0xFE20, 0xFE2F + 1)]),  # Combining Half Marks
    2
    ** 1: set(
        [*range(0xFE10, 0xFE1F + 1)] + [*range(0xFE30, 0xFE4F + 1)]  # Vertical Forms
    ),  # CJK Compatibility Forms
    2**2: set([*range(0xFE50, 0xFE6F + 1)]),  # Small Form Variants
    2**3: set([*range(0xFE70, 0xFEFF + 1)]),  # Arabic Presentation Forms-B
    2**4: set([*range(0xFF00, 0xFFEF + 1)]),  # Halfwidth And Fullwidth Forms
    2**5: set([*range(0xFFF0, 0xFFFF + 1)]),  # Specials
    2**6: set([*range(0x0F00, 0x0FFF + 1)]),  # Tibetan
    2**7: set([*range(0x0700, 0x074F + 1)]),  # Syriac
    2**8: set([*range(0x0780, 0x07BF + 1)]),  # Thaana
    2**9: set([*range(0x0D80, 0x0DFF + 1)]),  # Sinhala
    2**10: set([*range(0x1000, 0x109F + 1)]),  # Myanmar
    2
    ** 11: set(
        [*range(0x1200, 0x137F + 1)]  # Ethiopic
        + [*range(0x1380, 0x139F + 1)]  # Ethiopic Supplement
        + [*range(0x2D80, 0x2DDF + 1)]# Ethiopic Extended
    ),  
    2**12: set([*range(0x13A0, 0x13FF + 1)]),  # Cherokee
    2**13: set([*range(0x1400, 0x167F + 1)]),  # Unified Canadian Aboriginal Syllabics
    2**14: set([*range(0x1680, 0x169F + 1)]),  # Ogham
    2**15: set([*range(0x16A0, 0x16FF + 1)]),  # Runic
    2
    ** 16: set(
        [*range(0x1780, 0x17FF + 1)]   # Khmer
        + [*range(0x19E0, 0x19FF + 1)]  # Khmer Symbols
    ),
    2**17: set([*range(0x1800, 0x18AF + 1)]),  # Mongolian
    2**18: set([*range(0x2800, 0x28FF + 1)]),  # Braille Patterns
    2
    ** 19: set(
        [*range(0xA000, 0xA48F + 1)]   # Yi Syllables
        + [*range(0xA490, 0xA4CF + 1)]# Yi Radicals
    ),  
    2
    ** 20: set(
        [*range(0x1700, 0x171F + 1)]  # Tagalog
        + [*range(0x1720, 0x173F + 1)]  # Hanunoo
        + [*range(0x1740, 0x175F + 1)]  # Buhid
        + [*range(0x1760, 0x177F + 1)]# Tagbanwa
    ),  
    2**21: set([*range(0x10300, 0x1032F + 1)]),  # Old Italic
    2**22: set([*range(0x10330, 0x1034F + 1)]),  # Gothic
    2**23: set([*range(0x10400, 0x1044F + 1)]),  # Deseret
    2
    ** 24: set(
        [*range(0x1D000, 0x1D0FF + 1)]  # Byzantine Musical Symbols
        + [*range(0x1D100, 0x1D1FF + 1)]  # Musical Symbols
        + [*range(0x1D200, 0x1D24F + 1)]# Ancient Greek Musical Notation
    ),  
    2**25: set([*range(0x1D400, 0x1D7FF + 1)]),  # Mathematical Alphanumeric Symbols
    2
    ** 26: set(
        [*range(0xFF000, 0xFFFFD + 1)]  # Private Use (plane 15)
        + [*range(0x100000, 0x10FFFD + 1)]# Private Use (plane 16)
    ),  
    2
    ** 27: set(
        [*range(0xFE00, 0xFE0F + 1)]  # Variation Selectors
        + [*range(0xE0100, 0xE01EF + 1)]# Variation Selectors Supplement
    ),  
    2**28: set([*range(0xE0000, 0xE007F + 1)]),  # Tags
    2**29: set([*range(0x1900, 0x194F + 1)]),  # Limbu
    2**30: set([*range(0x1950, 0x197F + 1)]),  # Tai Le
    2**31: set([*range(0x1980, 0x19DF + 1)]),  # New Tai Lue
}

UnicodeRange3bitToNameMap = {
    2**0: "Combining Half Marks",
    2**1: "Vertical Forms",
    2**2: "Small Form Variants",
    2**3: "Arabic Presentation Forms-B",
    2**4: "Halfwidth And Fullwidth Forms",
    2**5: "Specials",
    2**6: "Tibetan",
    2**7: "Syriac",
    2**8: "Thaana",
    2**9: "Sinhala",
    2**10: "Myanmar",
    2**11: "Ethiopic",
    2**12: "Cherokee",
    2**13: "Unified Canadian Aboriginal Syllabics",
    2**14: "Ogham",
    2**15: "Runic",
    2**16: "Khmer",
    2**17: "Mongolian",
    2**18: "Braille Patterns",
    2**19: "Yi Syllables",
    2**20: "Tagalog",
    2**21: "Old Italic",
    2**22: "Gothic",
    2**23: "Deseret",
    2**24: "Byzantine Musical Symbols",
    2**25: "Mathematical Alphanumeric Symbols",
    2**26: "Private Use (plane 15/16)",
    2**27: "Variation Selectors",
    2**28: "Tags",
    2**29: "Limbu",
    2**30: "Tai Le",
    2**31: "New Tai Lue",
}

UnicodeRange4 = {
    2**0: set(range(0x1A00, 0x1A1F + 1)),  # Buginese
    2**1: set(range(0x2C00, 0x2C5F + 1)),  # Glagolitic
    2**2: set(range(0x2D30, 0x2D7F + 1)),  # Tifinagh
    2**3: set(range(0x4DC0, 0x4DFF + 1)),  # Yijing Hexagram Symbols
    2**4: set(range(0xA800, 0xA82F + 1)),  # Syloti Nagri
    2**5: set(range(0x10000, 0x1007F + 1)),  # Linear B Syllabary
    2**5: set(range(0x10080, 0x100FF + 1)),  # Linear B Ideograms
    2**5: set(range(0x10100, 0x1013F + 1)),  # Aegean Numbers
    2**6: set(range(0x10140, 0x1018F + 1)),  # Ancient Greek Numbers
    2**7: set(range(0x10380, 0x1039F + 1)),  # Ugaritic
    2**8: set(range(0x103A0, 0x103DF + 1)),  # Old Persian
    2**9: set(range(0x10450, 0x1047F + 1)),  # Shavian
    2**10: set(range(0x10480, 0x104AF + 1)),  # Osmanya
    2**11: set(range(0x10800, 0x1083F + 1)),  # Cypriot Syllabary
    2**12: set(range(0x10A00, 0x10A5F + 1)),  # Kharoshthi
    2**13: set(range(0x1D300, 0x1D35F + 1)),  # Tai Xuan Jing Symbols
    2**14: set(range(0x12000, 0x123FF + 1)),  # Cuneiform
    2**14: set(range(0x12400, 0x1247F + 1)),  # Cuneiform Numbers and Punctuation
    2**15: set(range(0x1D360, 0x1D37F + 1)),  # Counting Rod Numerals
    2**16: set(range(0x1B80, 0x1BBF + 1)),  # Sundanese
    2**17: set(range(0x1C00, 0x1C4F + 1)),  # Lepcha
    2**18: set(range(0x1C50, 0x1C7F + 1)),  # Ol Chiki
    2**19: set(range(0xA880, 0xA8DF + 1)),  # Saurashtra
    2**20: set(range(0xA900, 0xA92F + 1)),  # Kayah Li
    2**21: set(range(0xA930, 0xA95F + 1)),  # Rejang
    2**22: set(range(0xAA00, 0xAA5F + 1)),  # Cham
    2**23: set(range(0x10190, 0x101CF + 1)),  # Ancient Symbols
    2**24: set(range(0x101D0, 0x101FF + 1)),  # Phaistos Disc
    2**25: set(range(0x102A0, 0x102DF + 1)),  # Carian
    2**25: set(range(0x10280, 0x1029F + 1)),  # Lycian
    2**25: set(range(0x10920, 0x1093F + 1)),  # Lydian
    2**26: set(range(0x1F030, 0x1F09F + 1)),  # Domino Tiles
    2**26: set(range(0x1F000, 0x1F02F + 1)),  # Mahjong Tiles
}

UnicodeRange4bitToNameMap = {
    2**0: "Buginese",
    2**1: "Glagolitic",
    2**2: "Tifinagh",
    2**3: "Yijing Hexagram Symbols",
    2**4: "Syloti Nagri",
    2**5: "Linear B",
    2**6: "Ancient Greek Numbers",
    2**7: "Ugaritic",
    2**8: "Old Persian",
    2**9: "Shavian",
    2**10: "Osmanya",
    2**11: "Cypriot Syllabary",
    2**12: "Kharoshthi",
    2**13: "Tai Xuan Jing Symbols",
    2**14: "Cuneiform",
    2**15: "Counting Rod Numerals",
    2**16: "Sundanese",
    2**17: "Lepcha",
    2**18: "Ol Chiki",
    2**19: "Saurashtra",
    2**20: "Kayah Li",
    2**21: "Rejang",
    2**22: "Cham",
    2**23: "Ancient Symbols",
    2**24: "Phaistos Disc",
    2**25: "Carian",
    2**25: "Lycian/Lydian",
    2**26: "Domino/Mahjong Tiles",
}


def _getUnicodeRangeBits(copdepoints, unicoderange):
    cps = set(copdepoints)
    return sum([b for b in unicoderange if cps.intersection(unicoderange[b])])


def getUnicodeRange1Bits(copdepoints):
    return _getUnicodeRangeBits(copdepoints, UnicodeRange1)


def getUnicodeRange2Bits(copdepoints):
    rangeBits = _getUnicodeRangeBits(copdepoints, UnicodeRange2)
    if max(copdepoints) > 0xFFFF:
        rangeBits |= 1<<25
    return rangeBits


def getUnicodeRange3Bits(copdepoints):
    return _getUnicodeRangeBits(copdepoints, UnicodeRange3)


def getUnicodeRange4Bits(copdepoints):
    return _getUnicodeRangeBits(copdepoints, UnicodeRange4)


# Code Page Character Range
# see http://www.microsoft.com/typography/otspec/os2.htm#cpr


def getCodepageCodePoints(codepage):
    return set(
        [c for c in codepage.encoding_map.keys() if c and category(chr(c))[0] != "C"]
    )


CodePageRange1 = {
    2**0: cpg.data["cp1252"],  # Latin 1
    2**1: cpg.data["cp1250"],  # Latin 2: Eastern Europe
    2**2: cpg.data["cp1251"],  # Cyrillic
    2**3: cpg.data["cp1253"],  # Greek
    2**4: cpg.data["cp1254"],  # Turkish
    2**5: cpg.data["cp1255"],  # Hebrew
    2**6: cpg.data["cp1256"],  # Arabic
    2**7: cpg.data["cp1257"],  # Windows Baltic
    2**8: cpg.data["cp1258"],  # Vietnamese
    # 9-15                       # Reserved for Alternate ANSI
    2**16: cpg.data["cp874"],  # Thai
    2**17: cpg.data["cp932"],  # JIS/Japan
    2**18: cpg.data["cp936"],  # cp936, Chinese: Simplified chars--PRC and Singapore
    2**19: cpg.data["cp949"],  # Korean Wansung
    2**20: cpg.data["cp950"],  # Chinese: Traditional chars--Taiwan and Hong Kong
    2**21: cpg.data["cp1361"],  # cp1361 Korean Johab
    # 22-28                       # Reserved for Alternate ANSI & OEM
    2**29: cpg.data["mac-Roman"],  # Macintosh Character Set (US Roman)
    # 2**30                       # OEM Character Set
    # 2**31                       # Symbol Character Set
}

CodePageRange1bitToNameMap = {
    2**0: "Latin 1",
    2**1: "Latin 2: Eastern Europe",
    2**2: "Cyrillic",
    2**3: "Greek",
    2**4: "Turkish",
    2**5: "Hebrew",
    2**6: "Arabic",
    2**7: "Windows Baltic",
    2**8: "Vietnamese",
    2**9: "Reserved for Alternate ANSI",
    2**10: "Reserved for Alternate ANSI",
    2**11: "Reserved for Alternate ANSI",
    2**12: "Reserved for Alternate ANSI",
    2**13: "Reserved for Alternate ANSI",
    2**14: "Reserved for Alternate ANSI",
    2**15: "Reserved for Alternate ANSI",
    2**16: "Thai",
    2**17: "JIS/Japan",
    2**18: "cp936, Chinese: Simplified chars--PRC and Singapore",
    2**19: "Korean Wansung",
    2**20: "Chinese: Traditional chars--Taiwan and Hong Kong",
    2**21: "cp1361 Korean Johab",
    2**22: "Reserved for Alternate ANSI & OEM",
    2**23: "Reserved for Alternate ANSI & OEM",
    2**24: "Reserved for Alternate ANSI & OEM",
    2**25: "Reserved for Alternate ANSI & OEM",
    2**26: "Reserved for Alternate ANSI & OEM",
    2**27: "Reserved for Alternate ANSI & OEM",
    2**28: "Reserved for Alternate ANSI & OEM",
    2**29: "Macintosh Character Set (US Roman)",
    2**30: "OEM Character Set",
    2**31: "Symbol Character Set",
}

CodePageRange1reserved = [
    2**i for i in (9, 10, 11, 12, 13, 14, 15, 22, 23, 24, 25, 26, 27, 28)
]

CodePageRange2 = {
    # 32-47                      # Reserved for OEM
    2**16: cpg.data["cp869"],  # IBM Greek
    2**17: cpg.data["cp866"],  # MS-DOS Russian
    2**18: cpg.data["cp865"],  # MS-DOS Nordic
    2**19: cpg.data["cp864"],  # Arabic
    2**20: cpg.data["cp863"],  # MS-DOS Canadian French
    2**21: cpg.data["cp862"],  # Hebrew
    2**22: cpg.data["cp861"],  # MS-DOS Icelandic
    2**23: cpg.data["cp860"],  # MS-DOS Portuguese
    2**24: cpg.data["cp857"],  # IBM Turkish
    2**25: cpg.data["cp855"],  # IBM Cyrillic; primarily Russian
    2**26: cpg.data["cp852"],  # Latin 2
    2**27: cpg.data["cp775"],  # MS-DOS Baltic
    2**28: cpg.data["cp737"],  # Greek; former 437 G
    2**29: cpg.data["ISO 8859-6"],  # iso8859_6, Arabic; ASMO 708
    2**30: cpg.data["cp850"],  # WE/Latin 1
    2**31: cpg.data["cp437"],  # US
}

CodePageRange2bitToNameMap = {
    2**0: "Reserved for OEM",
    2**1: "Reserved for OEM",
    2**2: "Reserved for OEM",
    2**3: "Reserved for OEM",
    2**4: "Reserved for OEM",
    2**5: "Reserved for OEM",
    2**6: "Reserved for OEM",
    2**7: "Reserved for OEM",
    2**8: "Reserved for OEM",
    2**9: "Reserved for OEM",
    2**10: "Reserved for OEM",
    2**11: "Reserved for OEM",
    2**12: "Reserved for OEM",
    2**13: "Reserved for OEM",
    2**14: "Reserved for OEM",
    2**15: "Reserved for OEM",
    2**16: "IBM Greek",
    2**17: "MS-DOS Russian",
    2**18: "MS-DOS Nordic",
    2**19: "Arabic",
    2**20: "MS-DOS Canadian French",
    2**21: "Hebrew",
    2**22: "MS-DOS Icelandic",
    2**23: "MS-DOS Portuguese",
    2**24: "IBM Turkish",
    2**25: "IBM Cyrillic; primarily Russian",
    2**26: "Latin 2",
    2**27: "MS-DOS Baltic",
    2**28: "Greek; former 437 G",
    2**29: "iso8859_6, Arabic; ASMO 708",
    2**30: "WE/Latin 1",
    2**31: "US",
}

CodePageRange2reserved = [2**i for i in range(16)]


def _getCodePageRangeBits(copdepoints, codepagerange):
    cps = frozenset(copdepoints)
    return sum(
        [
            b
            for b in codepagerange
            if len(codepagerange[b]) > 0 and cps.issuperset(codepagerange[b])
        ]
    )


def getCodePageRange1Bits(copdepoints):
    return _getCodePageRangeBits(copdepoints, CodePageRange1)


def getCodePageRange2Bits(copdepoints):
    return _getCodePageRangeBits(copdepoints, CodePageRange2)


# -- Panose ---------------------------------------------------------------------

panoseFamilyKindToNameMap = {
    0: "Any",
    1: "No Fit",
    2: "Latin Text",
    3: "Latin Hand Written",
    4: "Latin Decorative",
    5: "Latin Symbol",
}

panoseSerifStyleToNameMap = {
    0: "Any",
    1: "No Fit",
    2: "Cove",
    3: "Obtuse Cove",
    4: "Square Cove",
    5: "Obtuse Square Cove",
    7: "Square",
    8: "Oval",
    9: "Exaggerated",
    10: "Triangle",
    11: "Normal Sans",
    12: "Obtuse Sans",
    13: "Perpendicular Sans",
    14: "Flared",
    15: "Rounded",
}

panoseWeightToNameMap = {
    0: "Any",
    1: "No Fit",
    2: "Very Light",
    3: "Light",
    4: "Thin",
    5: "Book",
    6: "Medium",
    7: "Demi",
    8: "Bold",
    9: "Heavy",
    10: "Black",
    11: "Extra Black",
}

panoseProportionToNameMap = {
    0: "Any",
    1: "No Fit",
    2: "Old Style",
    3: "Modern",
    4: "Even Width",
    5: "Extended",
    6: "Condensed",
    7: "Very Extended",
    8: "Very Condensed",
    9: "Monospaced",
}

panoseContrastToNameMap = {
    0: "Any",
    1: "No Fit",
    2: "No Contrast",
    3: "Very Low",
    4: "Low",
    5: "Medium Low",
    6: "Medium",
    7: "Medium High",
    8: "High",
    9: "Very High",
}

panoseStrokeVariationToNameMap = {
    0: "Any",
    1: "No Fit",
    2: "No Variation",
    3: "Gradual/Diagonal",
    4: "Gradual/Transitional",
    5: "Gradual/Vertical",
    6: "Gradual/Horizontal",
    7: "Rapid/Vertical",
    8: "Rapid/Horizontal",
    9: "Instant/Vertical",
    10: "Instant/Horizontal",
}

panoseArmStyleToNameMap = {
    0: "Any",
    1: "No Fit",
    2: "Straight Arms/Horizontal",
    3: "Straight Arms/Wedge",
    4: "Straight Arms/Vertical",
    5: "Straight Arms/Single Serif",
    6: "Straight Arms/Double Serif",
    7: "Non-Straight/Horizontal",
    8: "Non-Straight/Wedge",
    9: "Non-Straight/Vertical",
    10: "Non-Straight/Single Serif",
    11: "Non-Straight/Double Serif",
}

panoseLetterformToNameMap = {
    0: "Any",
    1: "No Fit",
    2: "Normal/Contact",
    3: "Normal/Weighted",
    4: "Normal/Boxed",
    5: "Normal/Flattened",
    6: "Normal/Rounded",
    7: "Normal/Off Center",
    8: "Normal/Square",
    9: "Oblique/Contact",
    10: "Oblique/Weighted",
    11: "Oblique/Boxed",
    12: "Oblique/Flattened",
    13: "Oblique/Rounded",
    14: "Oblique/Off Center",
    15: "Oblique/Square",
}

panoseMidlineToNameMap = {
    0: "Any",
    1: "No Fit",
    2: "Standard/Trimmed",
    3: "Standard/Pointed",
    4: "Standard/Serifed",
    5: "High/Trimmed",
    6: "High/Pointed",
    7: "High/Serifed",
    8: "Constant/Trimmed",
    9: "Constant/Pointed",
    10: "Constant/Serifed",
    11: "Low/Trimmed",
    12: "Low/Pointed",
    13: "Low/Serifed",
}

panoseXheightToNameMap = {
    0: "Any",
    1: "No Fit",
    2: "Constant/Small",
    3: "Constant/Standard",
    4: "Constant/Large",
    5: "Ducking/Small",
    6: "Ducking/Standard",
    7: "Ducking/Large",
}
