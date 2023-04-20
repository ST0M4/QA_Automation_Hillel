import random
from collections import Counter


# Task 1
def print_name(func):
    def inner(a, b):
        print(func.__name__)
        result = func(a, b)
        return result
    return inner


@print_name
def add_func(a, b):
    return a + b


@print_name
def mult_func(a, b):
    return a * b


print(add_func(2, 3))
print(mult_func(2, 3))

# Task 2
comprehension_list = [random.randint(1, 10) for item in range(100)]
c = Counter(comprehension_list)
# OR
count_list = {i: comprehension_list.count(i) for i in comprehension_list}
# print(comprehension_list)
print(c)
print(count_list)
