import json
import solver as main
with open("test_cases.json") as f:
    tests = json.load(f)
    for i in tests:
        test_case = tests[i]
        if main.parse_eqn(test_case) == test_case["expected_output"]:
            print("[Equation Parsing] Test " + i + " Passed")
        else:
            print("(ERROR) [Equation Parsing] Test " + i + " Failed")

        if main.solve_to_infix(test_case) == test_case["solved_eqn_output"]:
            print("[Equation Solving] Test " + i + " Passed")
        else:
            print("(ERROR) [Equation Solving] Test " + i + " Failed")
