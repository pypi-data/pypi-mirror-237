from otSpec.tag import script


def test_isValidScriptTag():
    assert script.isValidScriptTag("latn") == True    
    assert script.isValidScriptTag("xxxx") == False


def test_getScriptName():
    assert script.getScriptName("latn") == "Latin"    
    assert script.getScriptName("xxxx") == "Unregistered script"