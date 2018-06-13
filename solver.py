import json


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
            # The variable could either be on the left side *or* the right side
            return has_x(node["lhs"]) or has_x(node["rhs"])
    else:
        # If you reached a leaf without hitting x, then you have hit an integer (because leaves could only be x or ints) so this branch doesn't have x
        return False


def solve_eqn(lhs, rhs):
    # Imminent operation is the operation that is about to happen or the one with highest precedence going from left->right for ex: 1+(2*3), here + is the imminent operation
    imminent_operation = lhs["op"]
    opposite_operation = {"add": "subtract", "subtract": "add",
                          "multiply": "divide", "divide": "multiply"}

    # If either the LHS or the RHS of the current LHS has the variable  x, then don't simplify the remaining part just dump the whole thing to the RHS with just the opposite operation of the current operation
    if lhs["lhs"] == "x":
        rhs = '{"lhs": ' + rhs + ',"op":"' + \
            opposite_operation[imminent_operation] + \
            '", "rhs":' + str(lhs["rhs"]) + '}'
        return rhs
    elif lhs["rhs"] == "x":
        rhs = '{"lhs": ' + rhs + ',"op":"' + \
            opposite_operation[imminent_operation] + \
            '", "rhs":' + str(lhs["lhs"]) + '}'
        return rhs

    # Else both LHS and RHS are composite nodes then just dump the side without x completely to the other side, then solve the one with x
    else:
        the_side_without_x = "rhs" if has_x(lhs["lhs"]) else "lhs"
        the_side_with_x = "lhs" if has_x(lhs["lhs"]) else "rhs"
        rhs = '{"lhs": ' + rhs + ',"op":"' + \
            opposite_operation[imminent_operation] + \
            '", "rhs": ' + str(lhs[the_side_without_x]) + '}'
        return solve_eqn(lhs[the_side_with_x], rhs)


def solve_to_infix(eqn):
    '''
    An utility function that calls the solver and the parser to solve for x
    '''
    solved_eqn = solve_eqn(eqn["lhs"], str(eqn["rhs"]))
    solved_eqn = solved_eqn.replace("'", r'"')
    temp = json.loads(solved_eqn)
    return (parse_eqn(temp))


def evaluate_solution(eqn):
    '''
    Returns the solution for an equation given in serialized JSON
    '''
    solving_eqn = solve_to_infix(eqn)
    return eval(solving_eqn)  # I know this is a lol way to evaluate an expression, but I would have done pretty much what this does but badly, I know there is a way to use stacks and keep track of things and evaluate it but this is good enough ¯\_(ツ)_/¯
