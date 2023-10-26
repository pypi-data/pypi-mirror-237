GPOS_LOOKUP_SINGLE           = 1
GPOS_LOOKUP_PAIR             = 2
GPOS_LOOKUP_CURSIVE          = 3
GPOS_LOOKUP_MARK_TO_BASE     = 4
GPOS_LOOKUP_MARK_TO_LIGATURE = 5
GPOS_LOOKUP_MARK_TO_MARK     = 6
GPOS_LOOKUP_CONTEXT          = 7
GPOS_LOOKUP_CHAINING_CONTEXT = 8
GPOS_LOOKUP_EXTENSION        = 9


LookupTypeToNameMap = {
	GPOS_LOOKUP_SINGLE           : 'Single adjustment',             # Adjust position of a single glyph
	GPOS_LOOKUP_PAIR             : 'Pair adjustment',               # Adjust position of a pair of glyphs
	GPOS_LOOKUP_CURSIVE          : 'Cursive attachment',            # Attach cursive glyphs
	GPOS_LOOKUP_MARK_TO_BASE     : 'Mark-To-Base attachment',       # Attach a combining mark to a base glyph
	GPOS_LOOKUP_MARK_TO_LIGATURE : 'Mark-To-Ligature attachment',   # Attach a combining mark to a ligature
	GPOS_LOOKUP_MARK_TO_MARK     : 'Mark-To-Mark attachment',       # Attach a combining mark to another mark
	GPOS_LOOKUP_CONTEXT          : 'Context positioning',           # Position one or more glyphs in context
	GPOS_LOOKUP_CHAINING_CONTEXT : 'Chained Context positioning',   # Position one or more glyphs in chained context
	GPOS_LOOKUP_EXTENSION        : 'Extension positioning',         # Extension mechanism for other positionings
}

def getLookupTypeName(lookupType:int,default: str = "Unregistered lookup type") -> str:
	return LookupTypeToNameMap.get(lookupType, default)


# Lookup flags (same as in GSUB)

RightToLeft         = 0x0001
IgnoreBaseGlyphs    = 0x0002
IgnoreLigatures     = 0x0004
IgnoreMarks         = 0x0008
UseMarkFilteringSet = 0x0010
MarkAttachmentType  = 0xFF00