import json
from evaluator import evaluate_response


with open("cases.json") as f:
    cases = json.load(f)


for case in cases:
    result = evaluate_response(case)

    print(f"\nCase: {case['id']}")
    print(f"Passed: {result['passed']}")
    print(f"Score: {result['score']}/100")

    if result["failures"]:
        for failure in result["failures"]:
            print(f"- {failure}")