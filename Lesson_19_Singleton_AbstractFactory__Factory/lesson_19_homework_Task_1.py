# Task 1
def singleton(_class):
    def inner(*args):
        if not hasattr(_class, 'instance'):
            setattr(_class, 'instance', _class(*args))
        return getattr(_class, 'instance')
    return inner


@singleton
class Passport:
    def __init__(self, name, serial_num, issued):
        self.__name = name
        self.__serial_num = serial_num
        self.__issued = issued

    def show_info(self):
        print(f'Passport belongs to {self.__name}, its serial number is {self.__serial_num} and was issued '
              f'on {self.__issued}')


passport = Passport('Maximus', 'RT908657', '26.08.2000')
passport.show_info()
passport = Passport('Natali', 'CO777888', '14.07.1995')
passport.show_info()
