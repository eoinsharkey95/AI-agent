from functions.write_file import write_file

test_cases = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed")

]

for test in test_cases:
    if test[0] == ".":
        test_dir = "current"
    else:
        test_dir = test[0]

    print(test[0], test[1])
    print(f"Result for '{test_dir}' directory:")
    print(write_file(test[0], test[1], test[2]))
    print("")
