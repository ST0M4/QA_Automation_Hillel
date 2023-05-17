import csv


def add_row(filename: str, data):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def delete_row(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as updated_file:
        updated_file.writelines(lines[:-1])

