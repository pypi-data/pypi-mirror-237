tableTagToNameMap = { 
											'cmap' : 'Character to glyph mapping',
											'head' : 'Font header',
											'hhea' : 'Horizontal header',
											'hmtx' : 'Horizontal metrics',
											'maxp' : 'Maximum profile',
											'name' : 'Naming table',
											'OS/2' : 'OS/2 and Windows specific metrics',
											'post' : 'PostScript information',
											'cvt ' : 'Control Value Table',
											'fpgm' : 'Font program',
											'glyf' : 'Glyph data',
											'loca' : 'Index to location',
											'prep' : 'CVT Program',
											'CFF ' : 'Compact font format 1.0',
											'CFF2' : 'Compact font format 2.0',
											'VORG' : 'Vertical Origin',
											'SVG ' : 'Scalable-Vector-Graphics table',
											'EBDT' : 'Embedded bitmap data',
											'EBLC' : 'Embedded bitmap location data',
											'EBSC' : 'Embedded bitmap scaling data',
											'CBDT' : 'Color bitmap data',
											'CBLC' : 'Color bitmap location data',
											'COLR' : 'Color table',
											'CPAL' : 'Color palette table',
											'sbix' : 'Standard bitmap graphics',
											'BASE' : 'Baseline data',
											'GDEF' : 'Glyph definition data',
											'GPOS' : 'Glyph positioning data',
											'GSUB' : 'Glyph substitution data',
											'JSTF' : 'Justification data',
											'MATH' : 'Math layout data',
											'DSIG' : 'Digital signature',
											'gasp' : 'Grid-fitting/Scan-conversion',
											'hdmx' : 'Horizontal device metrics',
											'kern' : 'Kerning',
											'LTSH' : 'Linear threshold data',
											'MERG' : 'Merge',
											'meta' : 'Metadata',
											'STAT' : 'Style attributes',
											'avar' : 'Axis variations',
											'cvar' : 'CVT variations',
											'fvar' : 'Font variations',
											'gvar' : 'Glyph variations',
											'HVAR' : 'Horizontal metrics variations',
											'MVAR' : 'Metrics variations',
											'VVAR' : 'Vertical metrics variations',
											'PCLT' : 'PCL 5 data',
											'VDMX' : 'Vertical device metrics',
											'vhea' : 'Vertical Metrics header',
											'vmtx' : 'Vertical Metrics',
											# Apple tables
											'acnt' : 'Accent attachment table',
											'ankr' : 'Anchor point table',
											'bdat' : 'Bitmap data table',
											'bhed' : 'Bitmap header table',
											'bloc' : 'Bitmap location table',
											'bsln' : 'Baseline table',
											'fdsc' : 'Font descriptors table',
											'opbd' : 'AAT optical bounds table',
											'feat' : 'AAT Feature name table',
											'mort' : 'AAT glyph metamorphosis',
											'morx' : 'AAT extended glyph metamorphosis',
											'prop' : 'AAT glyph properties table',
											'fmtx' : 'Font metrics table',
											'fond' : 'FOND resources',
											# Graphite tables
											'Feat' : 'Graphite feature table', 
											'Glat' : 'Graphite glyph attribute table', 
											'Gloc' : 'Graphite glyph id to location table', 
											'Silf' : 'Graphite rules and actions', 
											'Sill' : 'Graphite language to feature'
											
											}


tableTags = sorted(tableTagToNameMap.keys())

RequiredTables = ('cmap', 'head', 'hhea', 'hmtx', 'maxp', 'name', 'OS/2', 
                  'post')

TrueTypeOutlineTables = ('cvt ', 'fpgm', 'glyf', 'loca', 'prep', 'gasp')

PostScriptOutlineTables = ('CFF ', 'CFF2', 'VORG')

BitmapGlyphTables = ('EBDT', 'EBLC', 'EBSC', 'CBDT', 'CBLC', 'sbix')

AdvancedTypographicTables = ('BASE', 'GDEF', 'GPOS', 'GSUB', 'JSTF', 'MATH')

FontVariationTables = ('avar', 'cvar', 'fvar', 'gvar', 'HVAR', 'MVAR', 'VVAR', 
                       'STAT', )

ColorFontTables = ('COLR', 'CPAL', 'CBDT', 'CBLC', 'sbix', 'SVG ')

def isValidTableTag(tag):
	'''Returns True if tag is in tableTagToNameMap'''
	return tag in tableTags
	
def getTableName(tag):
	'''Returns friendly table name for the given tag'''
	tag = tag.strip()
	while len(tag) < 4:
		tag += ' '
	return tableTagToNameMap.get(tag)
