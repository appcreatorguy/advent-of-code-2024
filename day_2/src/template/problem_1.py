from result import Result, Ok, Err
from .utils import read_input_file_as_string

def main():
    input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_1(input)
    print(f"{result.unwrap()}")

def solve_problem_1(input: list[str]) -> Result[any, str]:
    reports = [list(map(int, line.split())) for line in input]
    safe = [((all([report[i] < report[i+1] for i in range(len(report) - 1)]) or all([report[i] > report[i+1] for i in range(len(report) - 1)])) and all([abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1)])) for report in reports]
    return Ok(safe.count(True))
