from os import path
import pathlib

path1 = pathlib.Path(r"e:/realpython/realpython.epub")
print(path1)

home = pathlib.Path.home()
print(home)

cwd = pathlib.Path.cwd()
print(cwd)

print(cwd / "modules" / "main.py")
# Using '/' operator to extend existing path

rel_path = pathlib.Path('realpython/pythonbasics.epub')
print(f'rel_path is {rel_path}')
print(rel_path.is_absolute())
# check if path is absolute

file_path1 = home / pathlib.Path('docs/file.txt')
print(f'file_path is {file_path1}')

rel_path2 = pathlib.Path('/realpython')
abs_path2 = rel_path2.resolve()
print(f"abs_path2 is {abs_path2}")
# resolve returns an absolute path

print(list(path1.parents))
# .parents returns an iterable containing a list

for item in path1.parents:
    print(item)

print(path1.parent)
# return the first parent directory

print(abs_path2.anchor)
# if the path is absolute return the root directory, otherwise empty string

print(file_path1.name)
# return the name of the file or directory that the path points to

# file.txt ('file' part is called STEM, 'txt' part is called SUFFIX)

print(file_path1.stem)
print(file_path1.suffix)

print(file_path1.exists())
# check file existance

abs_path3 = pathlib.Path('e:/realpython/pythonbasics.epub')
print(abs_path3.is_file())
# check whether a file path refers to a file

abs_path4 = pathlib.Path('e:/realpython')
print(abs_path4.is_dir())
# check whether a file path refers to a directory

print()
# common operations

new_dir = pathlib.Path('./temp')
new_dir.mkdir(exist_ok=True)
# create the directory on the 'new_dir' path
# exist_ok=True means creation happens if folder doesn't exist

print(new_dir.exists())
print(new_dir.is_dir())

nested_dir = pathlib.Path('./temp2/nestdir')
nested_dir.mkdir(parents=True, exist_ok=True)
# create all dirs in the path if doesn't exist

temp_file_path = new_dir / 'file.txt'
temp_file_path.touch()
# create a file

print(temp_file_path.exists())
print(temp_file_path.is_file())

for path in pathlib.Path('./').iterdir():
    print(path)
# iterdir iterates over the directory and return iterable

for path in pathlib.Path('./temp').glob('*.txt'):
    print(path)
# .glob search all files for the pattern *.txt in the dir and return iterable

paths = [
    cwd / "temp" / "program1.py",
    cwd / "temp" / "program2.py",
    cwd / "temp" / "folder_a" / "program3.py",
    cwd / "temp" / "folder_a" / "folder_b" / "image1.jpg",
    cwd / "temp" / "folder_a" / "folder_b" / "image2.png"
]

# for path in paths:
    # path.touch()

print()
print(list((cwd / "temp").glob('*.py')))

print()
print(list((cwd / "temp").glob('*1*.py')))

print()
print(list((cwd / "temp").glob('program?.py')))

print()
print(list((cwd / "temp").glob('program[13].py')))

print()
# print(list((cwd / "temp").glob('**/*.py')))
print(list((cwd / "temp").rglob('*.py')))

# from_file_path.replace(target_file_path)
# move file to another place, rename dir or file

# path_file.unlink()
# path_file.unlink(missing_ok=True)
# remove the file
# missing_ok param doesn't raise an exceptioion if file doesn't exist

# path_folder.rmdir()
# remove a directory

# for path in folder_path.iterdir():
#     path.unlink()

# import shutil
# shutil.rmtree(cwd / "temp" / "folder_a")
# rmtree remove all the tree
