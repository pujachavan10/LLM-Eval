import json

from evaluator import evaluate_response


def load_cases():
    with open("cases.json") as f:
        return json.load(f)


def test_safe_case_passes():
    cases = load_cases()

    result = evaluate_response(cases[1])

    assert result["passed"] is True


def test_unsafe_case_is_detected():
    cases = load_cases()

    result = evaluate_response(cases[0])

    assert result["passed"] is False
    assert len(result["failures"]) > 0
    