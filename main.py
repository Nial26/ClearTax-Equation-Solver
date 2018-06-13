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


def serialize_eqn(eqn):
    
    eqn = eqn[1:len(eqn)-1] #Remove the brackets at the beginning and at the end
    
    stack = []
    stack.append(eqn[0])
    lhs_begin = 0
    lhs_end = 0
    while len(stack) != 0 and (lhs_end < len(eqn) - 1):
        lhs_end += 1
        if eqn[lhs_end] == "(":
            stack.append("(")
        elif eqn[lhs_end] == ")":
            stack.pop()
    lhs = eqn[lhs_begin: lhs_end].strip()

    operation_begin = lhs_end + 1
    operation_end = operation_begin
    while eqn[operation_end] not in ["=", "+", "-", "*", "/"]:
        operation_end += 1
    operation = eqn[operation_begin: operation_end+1].strip()

    rhs = eqn[operation_end+1:].strip()

    print(lhs)
    print(operation)
    print(rhs)



#print(parse_eqn(input_json))
print(serialize_eqn("((1 + (x * (5 + 10))) = 21)"))