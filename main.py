import solver as s

input_json = {
    "op": "equal",
    "lhs": {
        "op": "add",
        "lhs": 1,
        "rhs": {
            "op": "multiply",
            "lhs": "x",
            "rhs": 10
        }
    },
    "rhs": 21
}

# Pretty Print the Equation
print(s.parse_eqn(input_json))

# Transform and Solve for x
print(s.solve_to_infix(input_json))

# Evaluate the expression and find the value of x
print(s.evaluate_solution(input_json))
