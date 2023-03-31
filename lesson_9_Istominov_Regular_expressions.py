import re


# Task 1
def pattern_match(text):
    match = re.fullmatch(r'\w*', text)
    if match:
        print('Text matches the pattern!')
    else:
        print("Text contains smth except a-zA-Z0-9 and underscore. Please try again")
    return match


input_text = input("Введіть текст для перевірки патерну a-zA-Z0-9_: ")
print(pattern_match(input_text))


# Task 2
def remove_brackets(text):
    res = re.sub(r'\([^()]*\)', '', text)
    return res


# Task 3
def whitespace_insert(text):
    res = re.sub(r'([A-Z])', r' \1', text)
    return res

text_1 = 'GoodMorningAlex'
print(whitespace_insert(text_1))
