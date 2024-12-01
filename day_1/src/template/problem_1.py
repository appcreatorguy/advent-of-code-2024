from result import Result, Ok, Err
from .utils import read_input_file_as_string

def main():
    input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_1(input)
    print(f"{result.unwrap()}")

def solve_problem_1(input: list[str]) -> Result[any, str]:
    answer = sum([(max(x)-min(x)) for x in [list(pair) for pair in zip(*[sorted(list(x)) for x in zip(*[list(map(int, line.split("   "))) for line in input])])]])
    return Ok(answer)
