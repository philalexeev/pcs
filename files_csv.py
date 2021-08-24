import pathlib

cwd = pathlib.Path.cwd()

path_file = cwd / "temp" / "temperatures.csv"

# temperature_data = [68, 65, 68, 70, 74, 72]

# with path_file.open(mode="w", encoding="utf-8") as file:
#     file.write(str(temperature_data[0]))
#     for temp in temperature_data[1:]:
#         file.write(f",{temp}")

# with path_file.open(mode="r", encoding="utf-8") as file:
#     text = file.read()

# print(text.split(','))
# print([int(num) for num in text.split(',')])

# the same code with using csv module below

import csv

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73]
]

# file = path_file.open(mode="w", encoding="utf-8", newline="")

# writer = csv.writer(file)

# for temp in daily_temperatures:
#     writer.writerow(temp)

# file.close()

with path_file.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    # for temp in daily_temperatures:
    #     writer.writerow(temp)
    writer.writerows(daily_temperatures)

dt = []
with path_file.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        int_row = [int(value) for value in row]
        dt.append(int_row)

print(dt)


em_file_path = cwd / "temp" / "employees.csv"

with em_file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

people = [
    {"name": "Veronica", "age": 29},
    {"name": "Audrey", "age": 32},
    {"name": "Sam", "age": 24}
]

with em_file_path.open(mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(people)

