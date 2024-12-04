from result import Result, Ok, Err
from .utils import read_input_file_as_string
import re

def main():
    input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_1(input)
    print(f"{result.unwrap()}")

def solve_problem_1(input: list[str]) -> Result[any, str]:
    sum = 0
    for line in input:
        muls = re.findall("mul\(\d{1,3},\d{1,3}\)", line, re.MULTILINE)
        for mul in muls:
            # extract digits
            a,b = map(int, re.findall("\d{1,3}", mul))
            sum += (a*b)
    return Ok(sum)