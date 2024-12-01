from result import Result, Ok, Err
from .utils import read_input_file_as_string

def main():
    input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_2(input)
    print(f"{result.unwrap()}")

def solve_problem_2(input: list[str]) -> Result[any, str]:
    lists = [list(x) for x in zip(*[list(map(int, line.split("   "))) for line in input])]
    answer = sum([x * lists[1].count(x) for x in lists[0]])
    return Ok(answer)
