from otSpec.tag import language


def test_isValidLanguageTag():
    assert language.isValidLanguageTag("DEU ") == True    
    assert language.isValidLanguageTag("XXX") == False


def test_getLanguageName():
    assert language.getLanguageName("DEU ") == "German"    
    assert language.getLanguageName("xxx") == "Unregistered language"