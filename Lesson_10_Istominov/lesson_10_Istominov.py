from re import search


# Task 1
def show_domains_txt(file):
    file_to_read = open(file, 'r').read().replace('.', '')
    result = list(file_to_read.split("\n"))
    return print(result)


show_domains_txt("domains.txt")


# Task 2
with open('names.txt', 'w') as read_file:
    data = read_file.write('1 Andrii Ukraine\n2 Olga Hungary\n3 Matko Slovakia\n4 Eva Australia\n5 Francheska USA')
    read_file.close()


def show_names_txt(file_1):
    with open(file_1, 'r') as file:
        last_name = [element.split()[1] for element in file]
    return print(last_name)


show_names_txt('names.txt')

# Task 3
def show_authors_txt(file):
    with open(file, 'r') as authors_reader:
        authors_date_list = []
        for element in authors_reader:
            date = search(r'\d+(st|nd|rd|th) \w+ \d+', element)
            if date:
                authors_date_list.append({'date': date.group()})
    return print(authors_date_list)


show_authors_txt('authors.txt')
