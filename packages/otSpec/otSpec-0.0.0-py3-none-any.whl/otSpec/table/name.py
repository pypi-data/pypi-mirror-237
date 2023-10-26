'''Naming Table
source: http://www.microsoft.com/typography/otspec/name.htm
'''
#=== Platform IDs =============================================================

PLATFORM_UNI    = 0
PLATFORM_MAC    = 1
PLATFORM_ISO    = 2 # deprecated
PLATFORM_WIN    = 3
PLATFORM_CUSTOM = 4

platformidToNameMap = {
PLATFORM_UNI    : "Unicode",
PLATFORM_MAC    : "Macintosh",
PLATFORM_ISO    : "ISO",
PLATFORM_WIN    : "Windows",
PLATFORM_CUSTOM : "Custom",
}

def getPlatformName(platformid):
	return platformidToNameMap.get(platformid)
#=== Encoding IDs =============================================================

# Unicode platform-specific encoding IDs (platform ID = 0)
UNI_10     = 0   # Unicode 1.0 semantics
UNI_11     = 1   # Unicode 1.1 semantics
UNI_ISO    = 2   # ISO/IEC 10646 semantics
UNI_2_BMP  = 3   # Unicode 2.0 and onwards semantics, Unicode BMP only (cmap subtable formats 0, 4, 6).
UNI_2_FULL = 4   # Unicode 2.0 and onwards semantics, Unicode full repertoire (cmap subtable formats 0, 4, 6, 10, 12).
UNI_V_S    = 5   # Unicode Variation Sequences (cmap subtable format 14).
UNI_FULL   = 6   # Unicode full repertoire (cmap subtable formats 0, 4, 6, 10, 12, 13).

unicodeEncodingidToNameMap = {
UNI_10     : "Unicode 1.0",
UNI_11     : "Unicode 1.1",
UNI_ISO    : "ISO/IEC 10646",
UNI_2_BMP  : "Unicode 2.0 BMP only",
UNI_2_FULL : "Unicode 2.0 full",
UNI_V_S    : "Unicode Variation Sequences",
UNI_FULL   : "Unicode full",
}

def getUnicodeEncodingName(unicodeencodingid):
	return unicodeEncodingidToNameMap.get(unicodeencodingid)

# Macintosh platform-specific encoding IDs (platform ID = 1)
MAC_ROMAN    = 0
MAC_JAPANESE = 1
# ... and some more, up to 32

macEncodingidToNameMap = {
MAC_ROMAN    : "Roman",
MAC_JAPANESE : "Japanese",
}

def getMacEncodingName(macEncodingID):
	return macEncodingidToNameMap.get(macEncodingID)

# Windows platform-specific encoding IDs (platform ID= 3)
WIN_SYM = 0 # Symbol
WIN_UNI = 1 # Unicode BMP (UCS-2)
WIN_JIS = 2 # ShiftJIS
WIN_PRC = 3 # PRC
WIN_BIG5 = 4 # Big5
WIN_WANSUNG = 5 # Wansung
WIN_JOHAB = 6 # Johab
# ... and some more, up to ID 10

winEncodingidToNameMap = {
WIN_SYM     : "Symbol",
WIN_UNI     : "Unicode BMP",
WIN_JIS     : "ShiftJIS",
WIN_PRC     : "PRC",
WIN_BIG5    : "Big5",
WIN_WANSUNG : "Wansung",
WIN_JOHAB   : "Johab",
}

def getWinEncodingName(winEncodingID):
	return winEncodingidToNameMap.get(winEncodingID)

#=== Language IDs =============================================================

# Macintosh language IDs (platform ID = 1)
MAC_ENGLISH = 0
MAC_FRENCH  = 1
MAC_GERMAN  = 2
# ... and some more, up to ID 150

# Windows Language IDs (platform ID = 3)
WIN_ENGLISH = 0x0409 # English United States

LanguageIdToNameMap = {
	0x0436 : "Afrikaans - South Africa",
	0x041C : "Albanian - Albania",
	0x0484 : "Alsatian - France",
	0x045E : "Amharic - Ethiopia",
	0x1401 : "Arabic - Algeria",
	0x3C01 : "Arabic - Bahrain",
	0x0C01 : "Arabic - Egypt",
	0x0801 : "Arabic - Iraq",
	0x2C01 : "Arabic - Jordan",
	0x3401 : "Arabic - Kuwait",
	0x3001 : "Arabic - Lebanon",
	0x1001 : "Arabic - Libya",
	0x1801 : "Arabic - Morocco",
	0x2001 : "Arabic - Oman",
	0x4001 : "Arabic - Qatar",
	0x0401 : "Arabic - Saudi Arabia",
	0x2801 : "Arabic - Syria",
	0x1C01 : "Arabic - Tunisia",
	0x3801 : "Arabic - U.A.E.",
	0x2401 : "Arabic - Yemen",
	0x042B : "Armenian - Armenia",
	0x044D : "Assamese - India",
	0x082C : "Azeri (Cyrillic) - Azerbaijan",
	0x042C : "Azeri (Latin) - Azerbaijan",
	0x046D : "Bashkir - Russia",
	0x042D : "Basque - Basque",
	0x0423 : "Belarusian - Belarus",
	0x0845 : "Bengali - Bangladesh",
	0x0445 : "Bengali - India",
	0x201A : "Bosnian (Cyrillic) - Bosnia and Herzegovina",
	0x141A : "Bosnian (Latin) - Bosnia and Herzegovina",
	0x047E : "Breton - France",
	0x0402 : "Bulgarian - Bulgaria",
	0x0403 : "Catalan - Catalan",
	0x0C04 : "Chinese - Hong Kong S.A.R.",
	0x1404 : "Chinese - Macao S.A.R.",
	0x0804 : "Chinese - People's Republic of China",
	0x1004 : "Chinese - Singapore",
	0x0404 : "Chinese - Taiwan",
	0x0483 : "Corsican - France",
	0x041A : "Croatian - Croatia",
	0x101A : "Croatian (Latin) - Bosnia and Herzegovina",
	0x0405 : "Czech - Czech Republic",
	0x0406 : "Danish - Denmark",
	0x048C : "Dari - Afghanistan",
	0x0465 : "Divehi - Maldives",
	0x0813 : "Dutch - Belgium",
	0x0413 : "Dutch - Netherlands",
	0x0C09 : "English - Australia",
	0x2809 : "English - Belize",
	0x1009 : "English - Canada",
	0x2409 : "English - Caribbean",
	0x4009 : "English - India",
	0x1809 : "English - Ireland",
	0x2009 : "English - Jamaica",
	0x4409 : "English - Malaysia",
	0x1409 : "English - New Zealand",
	0x3409 : "English - Republic of the Philippines",
	0x4809 : "English - Singapore",
	0x1C09 : "English - South Africa",
	0x2C09 : "English - Trinidad and Tobago",
	0x0809 : "English - UK",
	0x0409 : "English - US",
	0x3009 : "English - Zimbabwe",
	0x0425 : "Estonian - Estonia",
	0x0438 : "Faroese - Faroe Islands",
	0x0464 : "Filipino - Philippines",
	0x040B : "Finnish - Finland",
	0x080C : "French - Belgium",
	0x0C0C : "French - Canada",
	0x040C : "French - France",
	0x140c : "French - Luxembourg",
	0x180C : "French - Principality of Monaco",
	0x100C : "French - Switzerland",
	0x0462 : "Frisian - Netherlands",
	0x0456 : "Galician - Galician",
	0x0437 : "Georgian - Georgia",
	0x0C07 : "German - Austria",
	0x0407 : "German - Germany",
	0x1407 : "German - Liechtenstein",
	0x1007 : "German - Luxembourg",
	0x0807 : "German - Switzerland",
	0x0408 : "Greek - Greece",
	0x046F : "Greenlandic - Greenland",
	0x0447 : "Gujarati - India",
	0x0468 : "Hausa (Latin) - Nigeria",
	0x040D : "Hebrew - Israel",
	0x0439 : "Hindi - India",
	0x040E : "Hungarian - Hungary",
	0x040F : "Icelandic - Iceland",
	0x0470 : "Igbo - Nigeria",
	0x0421 : "Indonesian - Indonesia",
	0x045D : "Inuktitut - Canada",
	0x085D : "Inuktitut (Latin) - Canada",
	0x083C : "Irish - Ireland",
	0x0434 : "isiXhosa - South Africa",
	0x0435 : "isiZulu - South Africa",
	0x0410 : "Italian - Italy",
	0x0810 : "Italian - Switzerland",
	0x0411 : "Japanese - Japan",
	0x044B : "Kannada - India",
	0x043F : "Kazakh - Kazakhstan",
	0x0453 : "Khmer - Cambodia",
	0x0486 : "K'iche - Guatemala",
	0x0487 : "Kinyarwanda - Rwanda",
	0x0441 : "Kiswahili - Kenya",
	0x0457 : "Konkani - India",
	0x0412 : "Korean - Korea",
	0x0440 : "Kyrgyz - Kyrgyzstan",
	0x0454 : "Lao - Lao P.D.R.",
	0x0426 : "Latvian - Latvia",
	0x0427 : "Lithuanian - Lithuania",
	0x082E : "Lower Sorbian - Germany",
	0x046E : "Luxembourgish - Luxembourg",
	0x042F : "Macedonian (FYROM) - Former Yugoslav Republic of Macedonia",
	0x083E : "Malay - Brunei Darussalam",
	0x043E : "Malay - Malaysia",
	0x044C : "Malayalam - India",
	0x043A : "Maltese - Malta",
	0x0481 : "Maori - New Zealand",
	0x047A : "Mapudungun - Chile",
	0x044E : "Marathi - India",
	0x047C : "Mohawk - Mohawk",
	0x0450 : "Mongolian (Cyrillic) - Mongolia",
	0x0850 : "Mongolian (Traditional) - People's Republic of China",
	0x0461 : "Nepali - Nepal",
	0x0414 : "Norwegian (Bokmal) - Norway",
	0x0814 : "Norwegian (Nynorsk) - Norway",
	0x0482 : "Occitan - France",
	0x0448 : "Odia (formerly Oriya) - India",
	0x0463 : "Pashto - Afghanistan",
	0x0415 : "Polish - Poland",
	0x0416 : "Portuguese - Brazil",
	0x0816 : "Portuguese - Portugal",
	0x0446 : "Punjabi - India",
	0x046B : "Quechua - Bolivia",
	0x086B : "Quechua - Ecuador",
	0x0C6B : "Quechua - Peru",
	0x0418 : "Romanian - Romania",
	0x0417 : "Romansh - Switzerland",
	0x0419 : "Russian - Russia",
	0x243B : "Sami (Inari) - Finland",
	0x103B : "Sami (Lule) - Norway",
	0x143B : "Sami (Lule) - Sweden",
	0x0C3B : "Sami (Northern) - Finland",
	0x043B : "Sami (Northern) - Norway",
	0x083B : "Sami (Northern) - Sweden",
	0x203B : "Sami (Skolt) - Finland",
	0x183B : "Sami (Southern) - Norway",
	0x1C3B : "Sami (Southern) - Sweden",
	0x044F : "Sanskrit - India",
	0x1C1A : "Serbian (Cyrillic) - Bosnia and Herzegovina",
	0x0C1A : "Serbian (Cyrillic) - Serbia",
	0x181A : "Serbian (Latin) - Bosnia and Herzegovina",
	0x081A : "Serbian (Latin) - Serbia",
	0x046C : "Sesotho sa Leboa - South Africa",
	0x0432 : "Setswana - South Africa",
	0x045B : "Sinhala - Sri Lanka",
	0x041B : "Slovak - Slovakia",
	0x0424 : "Slovenian - Slovenia",
	0x2C0A : "Spanish - Argentina",
	0x400A : "Spanish - Bolivia",
	0x340A : "Spanish - Chile",
	0x240A : "Spanish - Colombia",
	0x140A : "Spanish - Costa Rica",
	0x1C0A : "Spanish - Dominican Republic",
	0x300A : "Spanish - Ecuador",
	0x440A : "Spanish - El Salvador",
	0x100A : "Spanish - Guatemala",
	0x480A : "Spanish - Honduras",
	0x080A : "Spanish - Mexico",
	0x4C0A : "Spanish - Nicaragua",
	0x180A : "Spanish - Panama",
	0x3C0A : "Spanish - Paraguay",
	0x280A : "Spanish - Peru",
	0x500A : "Spanish - Puerto Rico",
	0x0C0A : "Spanish (Modern Sort) - Spain",
	0x040A : "Spanish (Traditional Sort) - Spain",
	0x540A : "Spanish - United States",
	0x380A : "Spanish - Uruguay",
	0x200A : "Spanish - Venezuela",
	0x081D : "Sweden - Finland",
	0x041D : "Swedish - Sweden",
	0x045A : "Syriac - Syria",
	0x0428 : "Tajik (Cyrillic) - Tajikistan",
	0x085F : "Tamazight (Latin) - Algeria",
	0x0449 : "Tamil - India",
	0x0444 : "Tatar - Russia",
	0x044A : "Telugu - India",
	0x041E : "Thai - Thailand",
	0x0451 : "Tibetan - PRC",
	0x041F : "Turkish - Turkey",
	0x0442 : "Turkmen - Turkmenistan",
	0x0480 : "Uighur - PRC",
	0x0422 : "Ukrainian - Ukraine",
	0x042E : "Upper Sorbian - Germany",
	0x0420 : "Urdu - Islamic Republic of Pakistan",
	0x0843 : "Uzbek (Cyrillic) - Uzbekistan",
	0x0443 : "Uzbek (Latin) - Uzbekistan",
	0x042A : "Vietnamese - Vietnam",
	0x0452 : "Welsh - United Kingdom",
	0x0488 : "Wolof - Senegal",
	0x0485 : "Yakut - Russia",
	0x0478 : "Yi - PRC",
	0x046A : "Yoruba - Nigeria",
	}

LanguageNameToIdMap = dict((LanguageIdToNameMap[i], i) for i in LanguageIdToNameMap)

def getLanguageName(languageID):
	return LanguageIdToNameMap.get(languageID)

def getLanguageID(languageName):
	return LanguageNameToIdMap.get(languageName)
	
#=== NAME IDs =================================================================
ID_COPYRIGHT             = 0 
ID_FAMILY                = 1 
ID_SUBFAMILY             = 2 
ID_FONT_IDENTIFIER       = 3 
ID_FULL_NAME             = 4 
ID_VERSION               = 5 
ID_POSTSCRIPT_NAME       = 6 
ID_TRADEMARK             = 7 
ID_MANUFACTURER          = 8 
ID_DESIGNER              = 9 
ID_DESCRIPTION           = 10
ID_VENDOR_URL            = 11
ID_DESIGNER_URL          = 12
ID_LICENSE               = 13
ID_LICENSE_URL           = 14
# RESERVED               = 15
ID_OT_FAMILY             = 16 # lagacy
ID_OT_SUBFAMILY          = 17 # lagacy
ID_TYPOGRAPHIC_FAMILY    = 16
ID_TYPOGRAPHIC_SUBFAMILY = 17
ID_COMPATIBLE_FULL_NAME  = 18
ID_SAMPLE_TEXT           = 19
ID_POSTSCRIPT_CID_NAME   = 20
ID_WWS_FAMILY            = 21
ID_WWS_SUBFAMILY         = 22
ID_LIGHT_BG_PALETTE      = 23
ID_DARK_BG_PALETTE       = 24
ID_VAR_PS_NAME_PREFIX    = 25

NameIdToNameMap = {
	ID_COPYRIGHT             : 'Copyright notice',
	ID_FAMILY                : 'Font Family Name',
	ID_SUBFAMILY             : 'Font Subfamily Name',
	ID_FONT_IDENTIFIER       : 'Unique Font Identifier',
	ID_FULL_NAME             : 'Full Font Name',
	ID_VERSION               : 'Version String',
	ID_POSTSCRIPT_NAME       : 'Postscript Name',
	ID_TRADEMARK             : 'Trademark',
	ID_MANUFACTURER          : 'Manufacturer Name',
	ID_DESIGNER              : 'Designer',
	ID_DESCRIPTION           : 'Description',
	ID_VENDOR_URL            : 'URL Vendor',
	ID_DESIGNER_URL          : 'URL Designer',
	ID_LICENSE               : 'License Description',
	ID_LICENSE_URL           : 'License Info URL',
	ID_TYPOGRAPHIC_FAMILY    : 'Typographic Family Name',
	ID_TYPOGRAPHIC_SUBFAMILY : 'Typographic Subfamily Name',
	ID_COMPATIBLE_FULL_NAME  : 'Compatible Full Name',
	ID_SAMPLE_TEXT           : 'Sample Text',
	ID_POSTSCRIPT_CID_NAME   : 'PostScript CID Name',
	ID_WWS_FAMILY            : 'WWS Family Name',
	ID_WWS_SUBFAMILY         : 'WWS Subfamily Name',
	ID_LIGHT_BG_PALETTE      : 'Light Backgound Palette',
	ID_DARK_BG_PALETTE       : 'Dark Backgound Palette',
	ID_VAR_PS_NAME_PREFIX    : 'Variations PostScript Name Prefix',
}

def getNameDescription(nameID):
	return NameIdToNameMap.get(nameID)