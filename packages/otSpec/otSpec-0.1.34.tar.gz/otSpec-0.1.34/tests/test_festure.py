from otSpec.tag import feature


def test_isValidFeatureTag():
    assert feature.isValidFeatureTag("dlig") == True    
    assert feature.isValidFeatureTag("xlig") == False


def test_getFeatureName():
    assert feature.getFeatureName("dlig") == "Discretionary Ligatures"    
    assert feature.getFeatureName("xlig") == "Unregistered feature"