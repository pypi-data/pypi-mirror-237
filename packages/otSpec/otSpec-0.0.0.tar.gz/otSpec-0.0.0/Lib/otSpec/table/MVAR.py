tagToInfoMap = {
    # Tag : (name, tableTag, attribute)
    "hasc": ("horizontal ascender", "OS/2", "sTypoAscender"),
    "hdsc": ("horizontal descender", "OS/2", "sTypoDescender"),
    "hlgp": ("horizontal line gap", "OS/2", "sTypoLineGap"),
    "hcla": ("horizontal clipping ascent", "OS/2", "usWinAscent"),
    "hcld": ("horizontal clipping descent", "OS/2", "usWinDescent"),
    "vasc": ("vertical ascender", "vhea", "ascent"),
    "vdsc": ("vertical descender", "vhea", "descent"),
    "vlgp": ("vertical line gap", "vhea", "lineGap"),
    "hcrs": ("horizontal caret rise", "hhea", "caretSlopeRise"),
    "hcrn": ("horizontal caret run", "hhea", "caretSlopeRun"),
    "hcof": ("horizontal caret offset", "hhea", "caretOffset"),
    "vcrs": ("vertical caret rise", "vhea", "caretSlopeRise"),
    "vcrn": ("vertical caret run", "vhea", "caretSlopeRun"),
    "vcof": ("vertical caret offset", "vhea", "caretOffset"),
    "xhgt": ("x height", "OS/2", "sxHeight"),
    "cpht": ("cap height", "OS/2", "sCapHeight"),
    "sbxs": ("subscript em x size", "OS/2", "ySubscriptXSize"),
    "sbys": ("subscript em y size", "OS/2", "ySubscriptYSize"),
    "sbxo": ("subscript em x offset", "OS/2", "ySubscriptXOffset"),
    "sbyo": ("subscript em y offset", "OS/2", "ySubscriptYOffset"),
    "spxs": ("superscript em x size", "OS/2", "ySuperscriptXSize"),
    "spys": ("superscript em y size", "OS/2", "ySuperscriptYSize"),
    "spxo": ("superscript em x offset", "OS/2", "ySuperscriptXOffset"),
    "spyo": ("superscript em y offset", "OS/2", "ySuperscriptYOffset"),
    "strs": ("strikeout size", "OS/2", "yStrikeoutSize"),
    "stro": ("strikeout offset", "OS/2", "yStrikeoutPosition"),
    "unds": ("underline size", "post", "underlineThickness"),
    "undo": ("underline offset", "post", "underlinePosition"),
    "gsp0": ("gaspRange[0]", "gasp", "gaspRange[0].rangeMaxPPEM"),
    "gsp1": ("gaspRange[1]", "gasp", "gaspRange[1].rangeMaxPPEM"),
    "gsp2": ("gaspRange[2]", "gasp", "gaspRange[2].rangeMaxPPEM"),
    "gsp3": ("gaspRange[3]", "gasp", "gaspRange[3].rangeMaxPPEM"),
    "gsp4": ("gaspRange[4]", "gasp", "gaspRange[4].rangeMaxPPEM"),
    "gsp5": ("gaspRange[5]", "gasp", "gaspRange[5].rangeMaxPPEM"),
    "gsp6": ("gaspRange[6]", "gasp", "gaspRange[6].rangeMaxPPEM"),
    "gsp7": ("gaspRange[7]", "gasp", "gaspRange[7].rangeMaxPPEM"),
    "gsp8": ("gaspRange[8]", "gasp", "gaspRange[8].rangeMaxPPEM"),
    "gsp9": ("gaspRange[9]", "gasp", "gaspRange[9].rangeMaxPPEM"),
}


def getMVARtagInfo(tag):
    return tagToInfoMap.get(tag, (None, None, None))


def getMVARtagName(tag):
    return getMVARtagInfo(tag)[0]


def getMVARtagTargetTable(tag):
    return getMVARtagInfo(tag)[1]


def getMVARtagTargetAttribute(tag):
    return getMVARtagInfo(tag)[2]
