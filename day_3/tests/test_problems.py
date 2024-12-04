from result import Ok, Err, Result, is_ok, is_err

from template.problem_1 import solve_problem_1
from template.problem_2 import solve_problem_2

def test_problem_1():
    input = open("./example.txt", "r")

    result = solve_problem_1(input).unwrap()
    
    assert result == 161

def test_problem_2():
    input = open("./example2.txt", "r")

    result = solve_problem_2(input).unwrap()
    
    assert result == 48