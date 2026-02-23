from functions.run_python_file import run_python_file

test_cases = [
    ("calculator", "main.py", None),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py", None),
    ("calculator", "../main.py", None),
    ("calculator", "nonexistent.py", None),
    ("calculator", "lorem.txt", None)

]

for test in test_cases:
    if test[0] == ".":
        test_dir = "current"
    else:
        test_dir = test[0]

    print(test[0], test[1])
    print(f"Result for '{test_dir}' directory:")
    print(run_python_file(test[0],test[1], test[2]))
    print("")
