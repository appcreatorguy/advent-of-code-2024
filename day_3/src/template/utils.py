from result import Ok, Err, Result, is_ok, is_err
import sys

def get_input_file_name_from_args() -> Result[str, str]:
    if len(sys.argv) != 3:
        return Err("Usage: python3 -m template <input_file_name>")
    return Ok(sys.argv[2])

def read_input_file_as_string() -> Result[str, str]:
    file_name = get_input_file_name_from_args()
    if is_err(file_name):
        return Err(file_name.unwrap_err())
    try:
        with open(file_name.unwrap(), "r") as f:
            return Ok(f.read())
    except FileNotFoundError:
        return Err("File not found: {}".format(file_name.unwrap()))
