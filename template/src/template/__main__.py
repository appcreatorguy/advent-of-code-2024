import sys
from template import problem_1, problem_2

is_testing = (len(sys.argv) > 1) and (sys.argv[1] != "tests" or sys.argv[2] != "vscode_pytest")
if not is_testing:
    print("Usage: python3 -m template <input_file_name>")
    sys.exit(1)
elif sys.argv[1] == "1":
    problem_1.main()
elif sys.argv[1] == "2":
    problem_2.main()

