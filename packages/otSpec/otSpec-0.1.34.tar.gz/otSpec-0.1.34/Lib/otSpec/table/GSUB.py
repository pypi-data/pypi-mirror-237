GSUB_LOOKUP_SINGLE = 1
GSUB_LOOKUP_MULTIPLE = 2
GSUB_LOOKUP_ALTERNATE = 3
GSUB_LOOKUP_LIGATURE = 4
GSUB_LOOKUP_CONTEXT = 5
GSUB_LOOKUP_CHAINING_CONTEXT = 6
GSUB_LOOKUP_EXTENSION = 7
GSUB_LOOKUP_REVERSE_CHAINING_CONTEXT = 8

LookupTypeToNameMap = {
    GSUB_LOOKUP_SINGLE: "Single",  #                     Replace one glyph with one glyph
    GSUB_LOOKUP_MULTIPLE: "Multiple",  #                 Replace one glyph with more than one glyph
    GSUB_LOOKUP_ALTERNATE: "Alternate",  #               Replace one glyph with one of many glyphs
    GSUB_LOOKUP_LIGATURE: "Ligature",  #                 Replace multiple glyphs with one glyph
    GSUB_LOOKUP_CONTEXT: "Context",  #                   Replace one or more glyphs in context
    GSUB_LOOKUP_CHAINING_CONTEXT: "Chaining context",  # Replace one or more glyphs in chained context
    GSUB_LOOKUP_EXTENSION: "Extension",  #               Extension mechanism for other substitutions
    GSUB_LOOKUP_REVERSE_CHAINING_CONTEXT: "Reverse chaining context single",  # Applied in reverse order, replace single glyph in chaining context
}


def getLookupTypeName(lookupType):
    return LookupTypeToNameMap.get(lookupType)


# Lookup flags (same as in GPOS)

RightToLeft = 0x0001
IgnoreBaseGlyphs = 0x0002
IgnoreLigatures = 0x0004
IgnoreMarks = 0x0008
UseMarkFilteringSet = 0x0010
MarkAttachmentType = 0xFF00
