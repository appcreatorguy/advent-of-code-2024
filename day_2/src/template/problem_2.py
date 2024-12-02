from result import Result, Ok, Err
from .utils import read_input_file_as_string

def main():
    input = read_input_file_as_string().unwrap().splitlines()

    result = solve_problem_2(input)
    print(f"{result.unwrap()}")

def solve_problem_2(input: str) -> Result[any, str]:
    reports = [list(map(int, line.split())) for line in input]
    is_safe = lambda x : x.count(False) <= 1
    safe = []
    for report in reports:
        increasing = all(report[i] <= report[i+1] for i in range(len(report) - 1))
        decreasing = all(report[i] >= report[i+1] for i in range(len(report) - 1))
        within_range = all(1 <= abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))
        if (increasing or decreasing) and within_range:
            safe.append(True)
        else:
            found = False
            for x in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(x)
                increasing = all(report_copy[i] <= report_copy[i+1] for i in range(len(report_copy) - 1))
                decreasing = all(report_copy[i] >= report_copy[i+1] for i in range(len(report_copy) - 1))
                within_range = all(1 <= abs(report_copy[i] - report_copy[i+1]) <= 3 for i in range(len(report_copy) - 1))
                if (increasing or decreasing) and within_range:
                    found = True
                    continue
            safe.append(found)
    return Ok(safe.count(True))
                
