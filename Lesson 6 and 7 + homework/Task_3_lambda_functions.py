import functools

# Task 1. Напишіть програму на Python для знаходження перетину двох заданих масивів за допомогою лямбда.
list_1 = [1, 2, 1, 5, 8, 99, 99, 3, 4, 5, 6, 7, 8, 9]
list_2 = [1, 5, 21, 9, 43, 99]
same_numbers = filter(lambda x: x in list_1, list_2)
print(list(same_numbers))


# Task 2. Напишіть програму на Python, щоб перевірити, чи є заданий рядок числом, за допомогою лямбда
some_input = input('Enter something: ')
digit_check = lambda x: x.isdigit()
print(digit_check(some_input))


# Task 3. Напишіть програму на Python, щоб знайти список із максимальною та мінімальною довжиною за допомогою лямбда.
lis = [[1, 2], [1], [5, 8, 99, 99, 3, 4],  [5, 6, 7], [8, 9]]

min_len = functools.reduce(lambda x, y: x if len(x) < len(y) else y, lis)
max_len = functools.reduce(lambda x, y: x if len(x) > len(y) else y, lis)

print(f'Список із мінімальною довжиною {min_len}')
print(f'Список із максимальною довжиною {max_len}')


# Task 4. Напишіть програму на Python для обчислення добутку заданого списку чисел за допомогою лямбда.
lis = [1, 2, 1, 5, 8, 4, 3, 4, 5, 6, 7, 8, 1]
multiplication = functools.reduce(lambda a, b: a*b, lis)
print(multiplication)