import random


# Task 1

first_set = {1, 9, 15, 69, 2, 0, 999, 576, 43, 65, 99, 34, 800}
second_set = {7, 69, 21, 3, 800, 54, 387, 1, 2, 0, 99, 1000}
print(sorted(first_set.intersection(second_set)))

# Task 2

students_dict = {
    'Ivan Ivanov': 10,
    'Oleksandr Gromov': 12,
    'Yulia Dotsenko': 5,
    'Fillip Kolyadenko': 8,
    'Nazar Gora': 9,
}

average = float(sum(students_dict.values())/len(students_dict))
print(average)

for student in students_dict.keys():
    if students_dict[student] > average:
        print(student)

# Task 3

list_numbers = random.choices(range(11), k=10)
print(list_numbers)
print(f'Кількість унікальних значень: {len(set(list_numbers))}')

# Task 4

# генеруємо рандомним чином 2 списки від 0 до 10 з максимальною кількістю 10 цифр
list_numbers_1 = random.choices(range(11), k=10)
list_numbers_2 = random.choices(range(11), k=10)

# робимо лист сміжних чисел 1 та 2 листа
common_list = sorted(set(list_numbers_1).intersection(set(list_numbers_2)))
print(f'List 1: {list_numbers_1}\nList 2: {list_numbers_2}\nCommon numbers:{common_list}')

# Task 5

text_string = 'one two three one four five seven ten seven one'
words_count = {}
for element in text_string.split():
    words_count[element] = text_string.split().count(element)

for item in words_count.items():
    print(item, end=' ')
