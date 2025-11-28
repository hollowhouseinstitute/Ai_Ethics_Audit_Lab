from explainability_tests import test_feature_transparency

def test_explainability_missing_keys():
    config = {"input_features": ["text"], "target": "classification"}
    result = test_feature_transparency(config)

    assert "missing_explainability_items" in result
    assert "preprocessing" in result["missing_explainability_items"]
