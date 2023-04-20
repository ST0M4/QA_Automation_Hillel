# Task 1
class Dogs:
    def __init__(self, breed: str, size: str, age: int, gender):
        self.breed = breed
        self.size = size
        self.age = age
        self.gender = gender

    @staticmethod
    def info_func():
        print('This class collects info about your dog and print it')


Dogs.info_func()
dog_01 = Dogs('Stafford-shire Terrier', 'Medium', 3, 'Male')
dog_03 = Dogs(input('Enter dog breed: '), input('Enter dog size(Small, Medium, Large): '),
              int(input('Enter dog age: ')), input('Enter dog gender(Male/Female: '))
print(f"The dog's breed is {dog_01.breed}, it's a {dog_01.gender},{dog_01.size} size and {dog_01.age} years old")
print(f"The dog's breed is {dog_03.breed}, it's a {dog_03.gender},{dog_03.size} size and {dog_03.age} years old")

# Task 2


class Company:
    def __init__(self, name, workers):
        self.salary = None
        self.position = 5
        self.experience = None
        self.name = name
        self.workers = workers
        self.department = ['IT', 'HR', 'Accounting']

    def hr_dep(self, name, experience):
        self.name = name
        self.experience = experience
        if self.experience > 3:
            position = 'Head of HR department'
            return position
        else:
            position = 'Office HR'
            return position

    def description(self, name, department):
        mes = f'{name} is in {department}'
        return mes

    @classmethod
    def department_info(cls, dep_name):
        if dep_name == 'HR':
            mes = f'The head of {dep_name} is Tatyana. You can contact her in case any questions'
            return mes
        if dep_name == 'IT':
            mes = f'The head of {dep_name} is Vladislav. You can contact her in case any questions'
            return mes
        if dep_name == 'Accounting':
            mes = f'The head of {dep_name} is Olga. You can contact her in case any questions'
            return mes
        else:
            mes = f'The head of {dep_name} is Rostislav. You can contact her in case any questions'
            return mes


Uber = Company('Uber', 10)
print(Uber.name)
print(Uber.workers)
print(Uber.department)
print(Uber.department_info('Accounting'))
head_of_hr = Uber.hr_dep('Tatyana', 4)
print(head_of_hr)
worker = Uber.description('Igor', 'IT')
print(worker)
