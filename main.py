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
                "lhs": 5,
                "rhs": 10
            }
        }
    },
    "rhs": 21
}

lollable_input = {
    "op": "equal",
    "lhs": {
        "op": "add",
        "lhs": 1,
        "rhs": {
            "op": "multiply",
            "rhs": {"op": "add",
                    "lhs": "x",
                    "rhs": 10},
            "lhs": {
                "op": "add",
                "lhs": 5,
                "rhs": 10
            }
        }
    },
    "rhs": 21
}


def parse_eqn(node):
    if type(node) == int or type(node) == str:  # The end nodes can only be x or integers
        return str(node)
    else:
        talk_to_symbol = {"add": "+", "subtract": "-",
                          "multiply": "*", "divide": "/", "equal": "="}
        operation = node["op"]
        operation = talk_to_symbol[operation]
        return "(" + parse_eqn(node["lhs"]) + " " + operation + " " + parse_eqn(node["rhs"]) + ")"



inputi_json = {
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


def solve_eqn(lhs, rhs):
    imminent_operation = lhs["op"]
    opposite_operation = {"add": "subtract", "subtract": "add",
                          "multiply": "divide", "divide": "multiply"}
    if lhs["lhs"] == "x":
        rhs = '{"lhs": ' + rhs + ',"op":"'+ opposite_operation[imminent_operation] + '", "rhs":' + str(lhs["rhs"]) + '}'
        return rhs
    elif lhs["rhs"] == "x":
        rhs = '{"lhs": ' + rhs + ',"op":"'+ opposite_operation[imminent_operation] + '", "rhs":' + str(lhs["lhs"]) + '}'
        return rhs
    elif type(lhs["lhs"]) == int:
        rhs = '{"lhs": ' + rhs + ',"op":"'+ opposite_operation[imminent_operation] + '", "rhs":' + str(lhs["lhs"]) + '}'
        return solve_eqn(lhs["rhs"], rhs)
    elif type(lhs["rhs"]) == int:
        rhs = '{"lhs": ' + rhs + ',"op":"'+ opposite_operation[imminent_operation] + '", "rhs":' + str(lhs["rhs"]) + '}'
        return solve_eqn(lhs["lhs"], rhs)
    else:
        # the_side_without_x
        rhs = '{"lhs": ' + rhs + ',"op":"'+ opposite_operation[imminent_operation] + '", "rhs":"blah"}'
        return rhs


# print(parse_eqn(input_json))
print(solve_eqn(input_json["lhs"], str(input_json["rhs"])))

mew = {"lhs": {"lhs": 21,"op":"subtract", "rhs":1},"op":"divide", "rhs":{'lhs': 5, 'op': 'add', 'rhs': 10}}
print(parse_eqn(mew))