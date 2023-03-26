import random
import string


# Task 2
names_list = ["king", "yeager", "black", "ludwig", "sapsan", "alpha", "bravo"]
domains_list = ["net", "com", "ua", "de", "eu"]


def generate_email(names, domains):
    name = random.choice(names)
    domain = random.choice(domains)
    rand_number = random.randint(100, 999)
    rand_str = ''.join(random.sample(string.ascii_lowercase, random.randint(5, 7)))
    return f'{name}.{rand_number}@{rand_str}.{domain}'


email = generate_email(domains=domains_list, names=names_list)
print(email)
