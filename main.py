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

def parse_eqn(node):
    '''
    Function to parse a serialized json equation and 
    bring to a pretty printable format (Also known as an infix expression)
    '''
    if type(node) == int or type(node) == str:  # The leaf nodes can only be 'x' or integers
        return str(node)
    else:
        talk_to_symbol = {"add": "+", "subtract": "-",
                          "multiply": "*", "divide": "/", "equal": "="}
        operation = node["op"]
        operation = talk_to_symbol[operation]
        return "(" + parse_eqn(node["lhs"]) + " " + operation + " " + parse_eqn(node["rhs"]) + ")"

def has_x(node):
    '''
    A function to check if a given tree has the variable x
    This is a helper function used in the solver function
    '''
    if type(node) != int:
        if node["lhs"] == "x" or node["rhs"] == "x":
            return True
        else:
            return has_x(node["lhs"]) or has_x(node["rhs"])  #The variable could either be on the left side *or* the right side
    else:
        return False #If you reached a leaf without hitting x, then you have hit an integer (because leaves could only be x or ints) so this branch doesn't have x

def solve_eqn(lhs, rhs):
    imminent_operation = lhs["op"] #Imminent operation is the operation that is about to happen or the one with highest precedence going from left->right for ex: 1+(2*3), here + is the imminent operation
    opposite_operation = {"add": "subtract", "subtract": "add",
                          "multiply": "divide", "divide": "multiply"}
    
    #If either the LHS or the RHS of the current LHS has the variable  x, then don't simplify the remaining part just dump the whole thing to the RHS with just the opposite operation of the current operation
    if lhs["lhs"] == "x":
        rhs = '{"lhs": ' + rhs + ',"op":"'+ opposite_operation[imminent_operation] + '", "rhs":' + str(lhs["rhs"]) + '}'
        return rhs
    elif lhs["rhs"] == "x":
        rhs = '{"lhs": ' + rhs + ',"op":"'+ opposite_operation[imminent_operation] + '", "rhs":' + str(lhs["lhs"]) + '}'
        return rhs

    #Otherwise if the LHS or RHS of the current LHS has an integer dump that to the other side with reversed operation
    elif type(lhs["lhs"]) == int:
        rhs = '{"lhs": ' + rhs + ',"op":"'+ opposite_operation[imminent_operation] + '", "rhs":' + str(lhs["lhs"]) + '}'
        return solve_eqn(lhs["rhs"], rhs)
    elif type(lhs["rhs"]) == int:
        rhs = '{"lhs": ' + rhs + ',"op":"'+ opposite_operation[imminent_operation] + '", "rhs":' + str(lhs["rhs"]) + '}'
        return solve_eqn(lhs["lhs"], rhs)

    #If all else fails both LHS and RHS are composite nodes then just dump the side without x completely to the other side
    else:
        the_side_without_x = "rhs" if has_x(lhs["lhs"]) else "lhs"
        the_side_with_x = "lhs" if has_x(lhs["lhs"]) else "rhs"
        rhs = '{"lhs": ' + rhs + ',"op":"'+ opposite_operation[imminent_operation] + '", "rhs": ' + str(lhs[the_side_without_x])  + '}'
        return solve_eqn(lhs[the_side_with_x], rhs)



complex_input = {
    "op": "equal",
    "lhs": {
        "op":"multiply",
        "lhs":{
            "op":"subtract",
            "lhs":{
                "op": "multiply",
                "lhs":{
                    "op": "add",
                    "lhs": 1,
                    "rhs":{
                        "op":"divide",
                        "lhs":{
                            "op":"multiply",
                            "lhs": {
                                "op": "add",
                                "lhs": "x",
                                "rhs": 3
                            },
                            "rhs":{
                                "op": "add",
                                "lhs": 5,
                                "rhs": {
                                    "op": "divide",
                                    "lhs":3,
                                    "rhs":7
                                }
                            }
                        },
                        "rhs":3
                    }
                },
                "rhs": 4
            },
            "rhs":73
        },
        "rhs": 5

    },
    "rhs": 7
}

print(parse_eqn(complex_input))
mew = {"lhs": {"lhs": {"lhs": {"lhs": {"lhs": {"lhs": {"lhs": 7,"op":"divide", "rhs": 5},"op":"add", "rhs": 73},"op":"divide", "rhs": 4},"op":"subtract", "rhs": 1},"op":"multiply", "rhs":
3},"op":"divide", "rhs": {'op': 'add', 'lhs': 5, 'rhs': {'op': 'divide', 'lhs': 3, 'rhs': 7}}},"op":"subtract", "rhs":3}
print(solve_eqn(complex_input["lhs"], str(complex_input["rhs"])))
print(parse_eqn(mew))