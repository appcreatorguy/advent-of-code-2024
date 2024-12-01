from result import Result, Ok, Err
from .utils import read_input_file_as_string

def main():
    input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_1(input)
    print(f"{result.unwrap()}")

def solve_problem_1(input: str) -> Result[any, str]:
    return Ok(0)
