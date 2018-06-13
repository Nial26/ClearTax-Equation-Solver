import re

input_json = {
    "op": "equal",
    "lhs": {
        "op": "add",
        "lhs": 1,
        "rhs": {
            "op": "multiply",
            "lhs": "x",
            "rhs": {
                "op": "add",
                "lhs" : 5,
                "rhs" : 10
            }
        }
    },
    "rhs": 21
}


def parse_eqn(node):
    if type(node) == int or type(node) == str:
        return str(node) 
    else:
        talk_to_symbol = {"add" : "+", "subtract": "-", "multiply" : "*", "divide" : "/", "equal" : "="}
        operation = node["op"]
        operation = talk_to_symbol[operation]
        return "(" + parse_eqn(node["lhs"]) + " " +  operation + " " + parse_eqn(node["rhs"]) + ")"



print(parse_eqn(input_json))