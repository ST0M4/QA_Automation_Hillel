import csv


# Task 1
def read_csv(file_name):
    with open(file_name, mode='r') as file:
        read_file = csv.reader(file, delimiter=',')
        result = []
        for el in read_file:
            result.append(el)
        return result


def write_csv(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        write_file = csv.writer(file)
        for row in data:
            write_file.writerow(row)


sample_data = [['name', 'age', 'country', 'occupation'], ['Alex', 23, 'Ukraine', 'Python developer']]
additional_data = [['Maria', 19, 'Ukraine', 'Accountant'], ['Steve', 29, 'USA', 'Product owner']]
write_csv('Test_file.csv', sample_data)
variable = read_csv('Test_file.csv')
for element in additional_data:
    variable.append(element)
write_csv('Test_file_2.csv', variable)


# Task 2
def square_gen():
    counter = 0
    while counter <= 100000:
        yield counter ** 2
        counter += 1


generator = square_gen()
while True:
    try:
        print(next(generator))
    except StopIteration:
        print('Iteration completed')
        break
