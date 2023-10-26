from __future__ import annotations

from typing import Any

featureTagToNameMap = {
    "aalt": "Access All Alternates",
    "abvf": "Above-base Forms",
    "abvm": "Above-base Mark Positioning",
    "abvs": "Above-base Substitutions",
    "afrc": "Alternative Fractions",
    "akhn": "Akhands",
    "blwf": "Below-base Forms",
    "blwm": "Below-base Mark Positioning",
    "blws": "Below-base Substitutions",
    "calt": "Contextual Alternates",
    "case": "Case-Sensitive Forms",
    "ccmp": "Glyph Composition / Decomposition",
    "cfar": "Conjunct Form After Ro",
    "cjct": "Conjunct Forms",
    "clig": "Contextual Ligatures",
    "cpct": "Centered CJK Punctuation",
    "cpsp": "Capital Spacing",
    "cswh": "Contextual Swash",
    "curs": "Cursive Positioning",
    "cv01": "Character Variants 01",
    "cv02": "Character Variants 02",
    "cv03": "Character Variants 03",
    "cv04": "Character Variants 04",
    "cv05": "Character Variants 05",
    "cv06": "Character Variants 06",
    "cv07": "Character Variants 07",
    "cv08": "Character Variants 08",
    "cv09": "Character Variants 09",
    "cv10": "Character Variants 10",
    "cv11": "Character Variants 11",
    "cv12": "Character Variants 12",
    "cv13": "Character Variants 13",
    "cv14": "Character Variants 14",
    "cv15": "Character Variants 15",
    "cv16": "Character Variants 16",
    "cv17": "Character Variants 17",
    "cv18": "Character Variants 18",
    "cv19": "Character Variants 19",
    "cv20": "Character Variants 20",
    "cv21": "Character Variants 21",
    "cv22": "Character Variants 22",
    "cv23": "Character Variants 23",
    "cv24": "Character Variants 24",
    "cv25": "Character Variants 25",
    "cv26": "Character Variants 26",
    "cv27": "Character Variants 27",
    "cv28": "Character Variants 28",
    "cv29": "Character Variants 29",
    "cv30": "Character Variants 30",
    "cv31": "Character Variants 31",
    "cv32": "Character Variants 32",
    "cv33": "Character Variants 33",
    "cv34": "Character Variants 34",
    "cv35": "Character Variants 35",
    "cv36": "Character Variants 36",
    "cv37": "Character Variants 37",
    "cv38": "Character Variants 38",
    "cv39": "Character Variants 39",
    "cv40": "Character Variants 40",
    "cv41": "Character Variants 41",
    "cv42": "Character Variants 42",
    "cv43": "Character Variants 43",
    "cv44": "Character Variants 44",
    "cv45": "Character Variants 45",
    "cv46": "Character Variants 46",
    "cv47": "Character Variants 47",
    "cv48": "Character Variants 48",
    "cv49": "Character Variants 49",
    "cv50": "Character Variants 50",
    "cv51": "Character Variants 51",
    "cv52": "Character Variants 52",
    "cv53": "Character Variants 53",
    "cv54": "Character Variants 54",
    "cv55": "Character Variants 55",
    "cv56": "Character Variants 56",
    "cv57": "Character Variants 57",
    "cv58": "Character Variants 58",
    "cv59": "Character Variants 59",
    "cv60": "Character Variants 60",
    "cv61": "Character Variants 61",
    "cv62": "Character Variants 62",
    "cv63": "Character Variants 63",
    "cv64": "Character Variants 64",
    "cv65": "Character Variants 65",
    "cv66": "Character Variants 66",
    "cv67": "Character Variants 67",
    "cv68": "Character Variants 68",
    "cv69": "Character Variants 69",
    "cv70": "Character Variants 70",
    "cv71": "Character Variants 71",
    "cv72": "Character Variants 72",
    "cv73": "Character Variants 73",
    "cv74": "Character Variants 74",
    "cv75": "Character Variants 75",
    "cv76": "Character Variants 76",
    "cv77": "Character Variants 77",
    "cv78": "Character Variants 78",
    "cv79": "Character Variants 79",
    "cv80": "Character Variants 80",
    "cv81": "Character Variants 81",
    "cv82": "Character Variants 82",
    "cv83": "Character Variants 83",
    "cv84": "Character Variants 84",
    "cv85": "Character Variants 85",
    "cv86": "Character Variants 86",
    "cv87": "Character Variants 87",
    "cv88": "Character Variants 88",
    "cv89": "Character Variants 89",
    "cv90": "Character Variants 90",
    "cv91": "Character Variants 91",
    "cv92": "Character Variants 92",
    "cv93": "Character Variants 93",
    "cv94": "Character Variants 94",
    "cv95": "Character Variants 95",
    "cv96": "Character Variants 96",
    "cv97": "Character Variants 97",
    "cv98": "Character Variants 98",
    "cv99": "Character Variants 99",
    "c2pc": "Petite Capitals From Capitals",
    "c2sc": "Small Capitals From Capitals",
    "dist": "Distances",
    "dlig": "Discretionary Ligatures",
    "dnom": "Denominators",
    "dtls": "Dotless Forms",
    "expt": "Expert Forms",
    "falt": "Final Glyph on Line Alternates",
    "fin2": "Terminal Forms #2",
    "fin3": "Terminal Forms #3",
    "fina": "Terminal Forms",
    "frac": "Fractions",
    "fwid": "Full Widths",
    "half": "Half Forms",
    "haln": "Halant Forms",
    "halt": "Alternate Half Widths",
    "hist": "Historical Forms",
    "hkna": "Horizontal Kana Alternates",
    "hlig": "Historical Ligatures",
    "hngl": "Hangul",  # (DEPRECATED in 2016)
    "hojo": "Hojo Kanji Forms (JIS X 0212-1990 Kanji Forms)",
    "hwid": "Half Widths",
    "init": "Initial Forms",
    "isol": "Isolated Forms",
    "ital": "Italics",
    "jalt": "Justification Alternates",
    "jp78": "JIS78 Forms",
    "jp83": "JIS83 Forms",
    "jp90": "JIS90 Forms",
    "jp04": "JIS2004 Forms",
    "kern": "Kerning",
    "lfbd": "Left Bounds",
    "liga": "Standard Ligatures",
    "ljmo": "Leading Jamo Forms",
    "lnum": "Lining Figures",
    "locl": "Localized Forms",
    "ltra": "Left-to-right alternates",
    "ltrm": "Left-to-right mirrored forms",
    "mark": "Mark Positioning",
    "med2": "Medial Forms #2",
    "medi": "Medial Forms",
    "mgrk": "Mathematical Greek",
    "mkmk": "Mark to Mark Positioning",
    "mset": "Mark Positioning via Substitution",
    "nalt": "Alternate Annotation Forms",
    "nlck": "NLC Kanji Forms",
    "nukt": "Nukta Forms",
    "numr": "Numerators",
    "onum": "Oldstyle Figures",
    "opbd": "Optical Bounds",
    "ordn": "Ordinals",
    "ornm": "Ornaments",
    "palt": "Proportional Alternate Widths",
    "pcap": "Petite Capitals",
    "pkna": "Proportional Kana",
    "pnum": "Proportional Figures",
    "pref": "Pre-Base Forms",
    "pres": "Pre-base Substitutions",
    "pstf": "Post-base Forms",
    "psts": "Post-base Substitutions",
    "pwid": "Proportional Widths",
    "qwid": "Quarter Widths",
    "rand": "Randomize",
    "rclt": "Required Contextual Alternates",
    "rkrf": "Rakar Forms",
    "rlig": "Required Ligatures",
    "rphf": "Reph Forms",
    "rtbd": "Right Bounds",
    "rtla": "Right-to-left alternates",
    "rtlm": "Right-to-left mirrored forms",
    "ruby": "Ruby Notation Forms",
    "rvrn": "Required Variation Alternates",
    "salt": "Stylistic Alternates",
    "sinf": "Scientific Inferiors",
    "size": "Optical size",
    "smcp": "Small Capitals",
    "smpl": "Simplified Forms",
    "ss01": "Stylistic Set 1",
    "ss02": "Stylistic Set 2",
    "ss03": "Stylistic Set 3",
    "ss04": "Stylistic Set 4",
    "ss05": "Stylistic Set 5",
    "ss06": "Stylistic Set 6",
    "ss07": "Stylistic Set 7",
    "ss08": "Stylistic Set 8",
    "ss09": "Stylistic Set 9",
    "ss10": "Stylistic Set 10",
    "ss11": "Stylistic Set 11",
    "ss12": "Stylistic Set 12",
    "ss13": "Stylistic Set 13",
    "ss14": "Stylistic Set 14",
    "ss15": "Stylistic Set 15",
    "ss16": "Stylistic Set 16",
    "ss17": "Stylistic Set 17",
    "ss18": "Stylistic Set 18",
    "ss19": "Stylistic Set 19",
    "ss20": "Stylistic Set 20",
    "ssty": "Math script style alternates",
    "stch": "Stretching Glyph Decomposition",
    "subs": "Subscript",
    "sups": "Superscript",
    "swsh": "Swash",
    "titl": "Titling",
    "tjmo": "Trailing Jamo Forms",
    "tnam": "Traditional Name Forms",
    "tnum": "Tabular Figures",
    "trad": "Traditional Forms",
    "twid": "Third Widths",
    "unic": "Unicase",
    "valt": "Alternate Vertical Metrics",
    "vatu": "Vattu Variants",
    "vert": "Vertical Writing",
    "vhal": "Alternate Vertical Half Metrics",
    "vjmo": "Vowel Jamo Forms",
    "vkna": "Vertical Kana Alternates",
    "vkrn": "Vertical Kerning",
    "vpal": "Proportional Alternate Vertical Metrics",
    "vrt2": "Vertical Alternates and Rotation",
    "zero": "Slashed Zero",
}

featureTags = sorted(featureTagToNameMap.keys())

featureInfo = {
    "aalt": """This feature makes all variations of a selected character
          accessible.""",
    "abvf": """Substitutes the above-base form of a vowel""",
    "abvm": """Positions marks above base glyphs.""",
    "abvs": """Substitutes a ligature for a base glyph and mark that's above it. """,
    "afrc": """Replaces figures separated by a slash with an alternative form.""",
    "akhn": """Preferentially substitutes a sequence of characters with a ligature.""",
    "blwf": """Substitutes the below-base form of a consonant in conjuncts.""",
    "blwm": """Positions marks below base glyphs.""",
    "blws": """Produces ligatures that comprise of base glyph and below-base
          forms.""",
    "calt": """In specified situations, replaces default glyphs with alternate
          forms which provide better joining behavior.""",
    "case": """Shifts various punctuation marks up to a position that works better
          with all-capital sequences or sets of lining figures; also changes
          oldstyle figures to lining figures.""",
    "ccmp": """To minimize the number of glyph alternates, it is sometimes desired
          to decompose a character into two glyphs. Additionally, it may
          be preferable to compose two characters into a single glyph for
          better glyph processing. This feature permits such
          composition/decompostion.""",
    "cfar": """Substitutes alternate below-base or post-base forms in Khmer script
          when occurring after conjoined Ro (“Coeng Ra”).""",
    "cjct": """Produces conjunct forms of consonants in Indic scripts. This is
          similar to the Akhands feature, but is applied at a different
          sequential point in the process of shaping an Indic syllable.""",
    "clig": """Replaces a sequence of glyphs with a single glyph which is preferred
          for typographic purposes. Unlike other ligature features, clig
          specifies the context in which the ligature is recommended. This
          capability is important in some script designs and for swash
          ligatures.""",
    "cpct": """Centers specific punctuation marks for those fonts that do not
          include centered and non-centered forms.""",
    "cpsp": """Globally adjusts inter-glyph spacing for all-capital text. Most
          typefaces contain capitals and lowercase characters, and the
          capitals are positioned to work with the lowercase. When capitals
          are used for words, they need more space between them for legibility
          and esthetics.""",
    "cswh": """This feature replaces default character glyphs with corresponding
          swash glyphs in a specified context.""",
    "curs": """In cursive scripts like Arabic, this feature cursively positions
          adjacent glyphs.""",
    "c2pc": """This feature turns capital characters into petite capitals.""",
    "c2sc": """This feature turns capital characters into small capitals.""",
    "dist": """Provides a means to control distance between glyphs.""",
    "dlig": """Replaces a sequence of glyphs with a single glyph which is preferred
          for typographic purposes. This feature covers those ligatures which
          may be used for special effect, at the user's preference.""",
    "dnom": """Replaces selected figures which follow a slash with denominator
          figures.""",
    "expt": """This feature replaces standard forms in Japanese fonts with
          corresponding forms preferred by typographers. """,
    "falt": """Replaces line final glyphs with alternate forms specifically
          designed for this purpose (they would have less or more advance
          width as need may be), to help justification of text.""",
    "fin2": """Replaces the Alaph glyph at the end of Syriac words with its
          appropriate form, when the preceding base character cannot be joined
          to, and that preceding base character is not a Dalath, Rish, or
          dotless Dalath-Rish.""",
    "fin3": """Replaces Alaph glyphs at the end of Syriac words when the preceding
          base character is a Dalath, Rish, or dotless Dalath-Rish.""",
    "fina": """Replaces glyphs at the ends of words with alternate forms designed
          for this use. This is common in Latin connecting scripts, and
          required in various non-Latins like Arabic.""",
    "frac": """Replaces figures separated by a slash with 'common' (diagonal)
          fractions.""",
    "fwid": """Replaces glyphs set on other widths with glyphs set on full
          (usually em) widths.""",
    "half": """Produces the half forms of consonants in Indic scripts.""",
    "haln": """Produces the halant forms of consonants in Indic scripts.""",
    "halt": """Respaces glyphs designed to be set on full-em widths, fitting them
          onto half-em widths.""",
    "hist": """Some letterforms were in common use in the past, but appear
          anachronistic today. The best-known example is the long form of s;
          others would include the old Fraktur k. Some fonts include the
          historical forms as alternates, so they can be used for a 'period'
          effect. """,
    "hkna": """Replaces standard kana with forms that have been specially designed
          for only horizontal writing.""",
    "hlig": """Some ligatures were in common use in the past, but appear
          anachronistic today. Some fonts include the historical forms as
          alternates, so they can be used for a 'period' effect.""",
    "hngl": """Replaces hanja (Chinese-style) Korean characters with the
          corresponding hangul (syllabic) characters.""",
    "hojo": """The 'hojo' feature is used to access the JIS X 0212-1990 glyphs for
          the cases when the JIS X 0213:2004 form is encoded.""",
    "hwid": """Replaces glyphs on proportional widths, or fixed widths other than
          half an em, with glyphs on half-em (en) widths.""",
    "init": """Replaces glyphs at the beginnings of words with alternate forms
          designed for this use. This is common in Latin connecting scripts,
          and required in various non-Latins like Arabic.""",
    "isol": """Replaces the nominal form of glyphs with their isolated forms.""",
    "ital": """Some fonts (such as Adobe's Pro Japanese fonts) will have both Roman
          and Italic forms of some characters in a single font. This feature
          replaces the Roman glyphs with the corresponding Italic glyphs.""",
    "jalt": """Improves justification of text by replacing glyphs with alternate
          forms specifically designed for this purpose (they would have less
          or more advance width as need may be). """,
    "jp78": """This feature replaces default (JIS90) Japanese glyphs with the
          corresponding forms from the JIS C 6226-1978 (JIS78) specification.""",
    "jp83": """This feature replaces default (JIS90) Japanese glyphs with the
          corresponding forms from the JIS X 0208-1983 (JIS83) specification.""",
    "jp90": """This feature replaces Japanese glyphs from the JIS78 or JIS83
          specifications with the corresponding forms from the
          JIS X 0208-1990 (JIS90) specification.""",
    "jp04": """The National Language Council (NLC) of Japan has defined new glyph
          shapes for a number of JIS characters, which were incorporated into
          JIS X 0213:2004 as new prototypical forms. The 'jp04' feature is a
          subset of the 'nlck' feature, and is used to access these
          prototypical glyphs in a manner that maintains the integrity of
          JIS X 0213:2004.""",
    "kern": """Adjusts amount of space between glyphs, generally to provide
          optically consistent spacing between glyphs.""",
    "lfbd": """Aligns glyphs by their apparent left extents at the left ends of
          horizontal lines of text, replacing the default behavior of aligning
          glyphs by their origins. This feature is called by the Optical
          Bounds (opbd) feature.""",
    "liga": """Replaces a sequence of glyphs with a single glyph which is preferred
          for typographic purposes. This feature covers the ligatures which
          the designer/manufacturer judges should be used in normal conditions.""",
    "ljmo": """Substitutes the leading jamo form of a cluster. """,
    "lnum": """This feature changes selected figures from oldstyle to the default
          lining form.""",
    "locl": """This feature enables localized forms of glyphs to be substituted for
          default forms.""",
    "mark": """Positions mark glyphs with respect to base glyphs.""",
    "med2": """Replaces Alaph glyphs in the middle of Syriac words when the
          preceding base character cannot be joined to.""",
    "medi": """Replaces glyphs in the middles of words (i.e. following a beginning
          and preceding an end) with alternate forms designed for this use.
          Note: This is different from the default form, which is designed for
          stand-alone use. This is common in Latin connecting scripts, and
          required in various non-Latins like Arabic.""",
    "mgrk": """Replaces standard typographic forms of Greek glyphs with
          corresponding forms commonly used in mathematical notation
          (which are a subset of the Greek alphabet).""",
    "mkmk": """Positions marks with respect to other marks. Required in various
          non-Latin scripts like Arabic.""",
    "mset": """Positions Arabic combining marks using glyph substitution""",
    "nalt": """Replaces default glyphs with various notational forms (e.g. glyphs
          placed in open or solid circles, squares, parentheses, diamonds or
          rounded boxes).""",
    "nlck": """The National Language Council (NLC) of Japan has defined new glyph
          shapes for a number of JIS characters in 2000. The 'nlck' feature is
          used to access those glyphs.""",
    "nukt": """Produces Nukta forms in Indic scripts.""",
    "numr": """Replaces selected figures which precede a slash with numerator
          figures, and replaces the typographic slash with the fraction slash.""",
    "onum": """This feature changes selected figures from the default lining style
          to oldstyle form.""",
    "opbd": """Aligns glyphs by their apparent left or right extents in horizontal
          setting, or apparent top or bottom extents in vertical setting,
          replacing the default behavior of aligning glyphs by their origins.""",
    "ordn": """Replaces default alphabetic glyphs with the corresponding ordinal
          forms for use after figures.""",
    "ornm": """This feature gives the user access to ornament glyphs (e.g. fleurons,
          dingbats and border elements) in the font. """,
    "palt": """Respaces glyphs designed to be set on full-em widths, fitting them
          onto individual (more or less proportional) horizontal widths.""",
    "pcap": """This feature turns lowercase characters into petite capitals. Forms
          related to petite capitals, such as specially designed figures, may
          be included.""",
    "pkna": """Replaces glyphs, kana and kana-related, set on uniform widths (half
          or full-width) with proportional glyphs.""",
    "pnum": """Replaces figure glyphs set on uniform (tabular) widths with
          corresponding glyphs set on glyph-specific (proportional) widths.""",
    "pref": """Substitutes the pre-base form of a consonant.""",
    "pres": """Produces the pre-base forms of conjuncts in Indic scripts.""",
    "pstf": """Substitutes the post-base form of a consonant.""",
    "psts": """Substitutes a sequence of a base glyph and post-base glyph, with its
          ligaturised form. """,
    "pwid": """Replaces glyphs set on uniform widths (typically full or half-em)
          with proportionally spaced glyphs. """,
    "qwid": """Replaces glyphs on other widths with glyphs set on widths of one
          quarter of an em (half an en).""",
    "rand": """In order to emulate the irregularity and variety of handwritten
          text, this feature allows multiple alternate forms to be used.""",
    "rlig": """Replaces a sequence of glyphs with a single glyph which is preferred
          for typographic purposes. This feature covers those ligatures, which
          the script determines as required to be used in normal conditions.""",
    "rkrf": """Produces conjoined forms for consonants with rakar in Devanagari and
          Gujarati scripts.""",
    "rphf": """In the Devanagari (Indic) script, the consonant Ra possesses a reph
          form. When the Ra is a syllable initial consonant and is followed by
          the virama, it is repositioned after the post base vowel sign within
          the syllable, and also substituted with a mark that sits above the
          base glyph.""",
    "rtbd": """Aligns glyphs by their apparent right extents at the right ends of
          horizontal lines of text, replacing the default behavior of aligning
          glyphs by their origins. This feature is called by the Optical
          Bounds (opbd) feature.""",
    "rtla": """This feature applies glyphic variants (other than mirrored forms)
          appropriate for right-to-left text.""",
    "rtlm": """This feature applies mirrored forms appropriate for right-to-left
          text other than for those characters that would be covered by the
          character-level mirroring step performed by an OpenType layout
          engine.""",
    "ruby": """Japanese typesetting often uses smaller kana glyphs, generally in
          superscripted form, to clarify the meaning of kanji which may be
          unfamiliar to the reader. These are called ruby, from the old
          typesetting term for four-point-sized type. This feature identifies
          glyphs in the font which have been designed for this use,
          substituting them for the default designs.""",
    "rvrn": """This feature is used in fonts that support OpenType Font Variations
          in order to select alternate glyphs for particular variation
          instances.""",
    "salt": """Many fonts contain alternate glyph designs for a purely esthetic
          effect; these don't always fit into a clear category like swash or
          historical. This feature replaces the default forms with the
          stylistic alternates.""",
    "sinf": """Replaces lining or oldstyle figures with inferior figures (smaller
          glyphs which sit lower than the standard baseline, primarily for
          chemical or mathematical notation). May also replace lowercase
          characters with alphabetic inferiors.""",
    "size": """This feature stores two kinds of information about the optical size
          of the font: design size (the point size for which the font is
          optimized) and size range (the range of point sizes which the font
          can serve well), as well as other information which helps
          applications use the size range. The design size is useful for
          determining proper tracking behavior. The size range is useful in
          families which have fonts covering several ranges. Additional values
          serve to identify the set of fonts which share related size ranges,
          and to identify their shared name. Note that sizes refer to nominal
          final output size, and are independent of viewing magnification or
          resolution.""",
    "smcp": """This feature turns lowercase characters into small capitals. This
          corresponds to the common SC font layout. It is generally used for
          display lines set in Large and small caps, such as titles. Forms
          related to small capitals, such as oldstyle figures, may be included.""",
    "smpl": """Replaces 'traditional' Chinese or Japanese forms with the
          corresponding 'simplified' forms.""",
    "ss01": """Glyphs in stylistic sets may be designed to harmonise visually,
          interract in particular ways, or otherwise work together.""",
    "subs": """The "subs" feature may replace a default glyph with a subscript
          glyph.""",
    "sups": """Replaces lining or oldstyle figures with superior figures (primarily
          for footnote indication), and may replace lowercase letters with
          superior letters (primarily for abbreviated French titles).""",
    "swsh": """This feature replaces default character glyphs with corresponding
          swash glyphs.""",
    "titl": """This feature replaces the default glyphs with corresponding forms
          designed specifically for titling. These may be all-capital and/or
          larger on the body, and adjusted for viewing at larger sizes.""",
    "tjmo": """Substitutes the trailing jamo form of a cluster.""",
    "tnam": """Replaces 'simplified' Japanese kanji forms with the corresponding
          'traditional' forms.""",
    "tnum": """Replaces figure glyphs set on proportional widths with corresponding
          glyphs set on uniform (tabular) widths.""",
    "trad": """Replaces 'simplified' Chinese hanzi or Japanese kanji forms with the
          corresponding 'traditional' forms.""",
    "twid": """Replaces glyphs on other widths with glyphs set on widths of one
          third of an em. The characters involved are normally figures and
          some forms of punctuation.""",
    "unic": """This feature maps upper- and lowercase letters to a mixed set of
          lowercase and small capital forms, resulting in a single case
          alphabet. Substitutions might also include specially designed
          figures.""",
    "valt": """Repositions glyphs to visually center them within full-height
          metrics, for use in vertical setting. """,
    "vatu": """In an Indic consonant conjunct, substitutes a ligature glyph for a
          base consonant and a following vattu (below-base) form of a
          conjoining consonant, or for a half form of a consonant and a
          following vattu form. """,
    "vert": """Replaces default forms with variants adjusted for vertical writing
          when in vertical writing mode.""",
    "vhal": """Respaces glyphs designed to be set on full-em heights, fitting them
          onto half-em heights.""",
    "vjmo": """Substitutes the vowel jamo form of a cluster.""",
    "vkna": """Replaces standard kana with forms that have been specially designed
          for only vertical writing.""",
    "vkrn": """Adjusts amount of space between glyphs, generally to provide
          optically consistent spacing between glyphs.""",
    "vpal": """Respaces glyphs designed to be set on full-em heights, fitting them
          onto individual (more or less proportional) vertical heights.""",
    "vrt2": """Replaces some fixed-width (half-, third- or quarter-width) or
          proportional-width glyphs (mostly Latin or katakana) with forms
          suitable for vertical writing (that is, rotated 90 degrees
          clockwise). """,
    "zero": """Some fonts contain both a default form of zero, and an alternative
          form which uses a diagonal slash through the counter. This feature
          allows the user to change from the default 0 to a slashed form.""",
}


def isValidFeatureTag(tag: str) -> bool:
    """Returns True if tag is in featureTagToNameMap"""
    return tag in featureTags


def getFeatureName(tag: str, default: str = "Unregistered feature") -> str:
    """Returns friendly feature name for the given tag.

    Sample

    .. doctest::

        >>> getFeatureName("dlig")
        Discretionary Ligatures

    """
    return featureTagToNameMap.get(tag, default)
