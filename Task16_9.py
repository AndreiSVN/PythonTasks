#    Задание 16.9.1                           применение метода __str__ (вывод в строку)
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle: {self.x}, {self.y}, {self.width}, {self.height}'

rect = Rectangle(5, 10, 50, 100)
print(rect.__str__())
=================================================================================================================


# Задание 16.9.2                            создание класса фигуры и расчет ее площади

class Rectangle:
    def __init__(self, width, height):
        self.width = a
        self.height = b

    def getArea(self):
        return self.width * self.height

a = 135
b = 49
result = Rectangle(a, b)
print(result.getArea())

==================================================================================================================


# Задание 16.9.3                          вывод информации о клиенте в строку методом __str__
class Clients:
    def __init__(self, firstname, lastname, city, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.firstname} {self.lastname}. {self.city}. Balance: {self.balance} руб.'

client1 = Clients('Иван', 'Петров', 'Москва', '50')
print(client1.__str__())

==================================================================================================================

# Задание 16.9.4                      формирование списка приглашенных на корпоратив: через словарь

Customers = [{'firstname': 'Иван', 'lastname': 'Иванов', 'city': 'Москва', 'balance': 100},
             {'firstname': 'Петр', 'lastname': 'Петров', 'city': 'Москва', 'balance': 150},
             {'firstname': 'Федор', 'lastname': 'Федотов', 'city': 'Москва', 'balance': 170},
             {'firstname': 'Александр', 'lastname': 'Александров', 'city': 'Москва', 'balance': 130},
             {'firstname': 'Владимир', 'lastname': 'Владимиров', 'city': 'Москва', 'balance': 130}]

class Clients:
    def __init__(self, firstname = '', lastname = '', city = '', balance = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def get_guest(self, customer_from_dict):
        self.firstname = customer_from_dict.get('firstname')
        self.lastname = customer_from_dict.get('lastname')
        self.city = customer_from_dict.get('city')
        return f'{self.firstname} {self.lastname}, г.{self.city}'


print('Список приглашенных на корпоратив:')
for customer in Customers:
    customer_obj = Clients()
    customer_obj.get_guest(customer)
    print(customer_obj.get_guest(customer))
