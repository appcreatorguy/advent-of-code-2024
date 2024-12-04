from result import Result, Ok, Err
from .utils import read_input_file_as_string
import re

def main():
    input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_2(input)
    print(f"{result.unwrap()}")

def solve_problem_2(input: list[str]) -> Result[any, str]:
    sum = 0
    # merge all lines into one string
    line = "".join(input)
    line = re.split(r"(don't\(\))|(do\(\))", line)
    line = list(filter(None, line))
    chunk = line.pop(0)
    muls = re.findall("mul\(\d{1,3},\d{1,3}\)", chunk, re.MULTILINE)
    for mul in muls:
        # extract digits
        a,b = map(int, re.findall("\d{1,3}", mul))
        sum += (a*b)
    while len(line) > 0:
        chunk = line.pop(0)
        if chunk == "don't()":
            continue
        elif chunk == "do()":
            chunk = line.pop(0)
            muls = re.findall("mul\(\d{1,3},\d{1,3}\)", chunk, re.MULTILINE)
            for mul in muls:
                # extract digits
                a,b = map(int, re.findall("\d{1,3}", mul))
                sum += (a*b)
    return Ok(sum)
