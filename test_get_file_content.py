from functions.get_file_content import get_file_content

test_cases = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py")

]

for test in test_cases:
    if test[0] == ".":
        test_dir = "current"
    else:
        test_dir = test[0]

    print(test[0], test[1])
    print(f"Result for '{test_dir}' directory:")
    print(get_file_content(test[0],test[1]))
    print("")
