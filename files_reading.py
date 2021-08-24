# reading & writing files

import pathlib

cwd = pathlib.Path.cwd()

path_file = cwd / "temp" / "file.txt"
# path_file.touch()
# file_for_path = path_file.open(mode="r", encoding="utf-8")
# print(file_for_path)
# file_for_path.close()

# path_file = "c:/Users/phill/Documents/Projects/pcs/temp/file.txt"
# file_for_path = open(path_file, mode="r", encoding="utf-8")
# file_for_path.close()

# pythonic way to open a file
# read all file at once
with path_file.open(mode="r", encoding="utf-8") as filePath:
    text = filePath.read()
    # print(text)

# read file line by line
# readline() return iterable
# with path_file.open(mode="r", encoding="utf-8") as filePath:
#     for line in filePath.readlines():
#         print(line, end="")

with path_file.open(mode="w", encoding="utf-8") as filePath:
    filePath.write("phil wrote this again")

with path_file.open(mode="a", encoding="utf-8") as filePath:
    filePath.write("\nphil wrote this too\n")

lines_of_text = [
    "Hello from Line 1\n",
    "Hello from Line 2\n",
    "Hello from Line 3\n"
]

with path_file.open(mode="a", encoding="utf-8") as filePath:
    filePath.writelines(lines_of_text)

