# Equation Solver

A Module to de-serialize mathematical equations, solve them and evaluate them!               
The solver mainly has 2 components
1. The parser (`parse_eqn`) which is used to convert from the JSON notation to infix form
2. The actual solver (`solve_eqn`) which solves the equation and *returns the solved equation in the serialized form itself*. 

So if you want your solved equation in infix form, just pass it through the parser again, but there is an utility function `solve_to_infix`, that does this for you. There is also an evaluator (`evaluate_solution`) which evaluates the solution given a serialized equation

## Running the given test case

`python main.py`

## Running tests for other Inputs

`python tester.py`

### Miscellaneous
Please feel free to contact me for any issues or bugs!