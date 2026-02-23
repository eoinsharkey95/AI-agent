from functions.get_files_info import get_files_info

test_cases = [
    ("calculator", "."),
    ("calculator", "pkg"),
    ("calculator", "/bin"),
    ("calculator", "../")
]

for test in test_cases:
    if test[1] == ".":
        test_dir = "current"
    else:
        test_dir = test[1]


    print(f"Result for '{test_dir}' directory:")
    print(get_files_info(test[0],test[1]))
    print("")
