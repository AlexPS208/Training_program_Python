# Спадкування

class Table():
    item = "table"
    amount = 0

    def __init__(self, w=1.5, h=1.5, material="wood"):
        self.width = w
        self.height = h
        self.material = material
        Table.amount += 1

    def __del__(self):
        Table.amount -= 1


class Desktable(Table):
    def square(self):
        return self.width*self.height


table1 = Desktable()
table2 = Table(2, 2.5, "iron")
table3 = Desktable(1, material="plastic")

print(Table.amount)
print("table 1:", table1.__dict__)
print("table 2:", table2.__dict__)
print("table 3:", table3.__dict__)

print(table1.square())

try:
    print(table2.square())
except:
    print("Клас Table не має функції square")


print()

# Поліморфізм


class Vehicle:
    def print_details(self):
        print("Це батьківський метод класа класса Vehicle")


class Car(Vehicle):
    def print_details(self):
        print("Це дочірній метод класа Car")


class Cycle(Vehicle):
    def print_details(self):
        print("Це дочірній метод класа Cycle")


machine1 = Vehicle()
machine2 = Car()
machine3 = Cycle()

machine1.print_details()
machine2.print_details()
machine3.print_details()


print()

# Інкапсуляція


class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.__surname = surname
        self._age = age

    def get_surname(self):
        return self.__surname


human = Person("Іван", "Крузенштерн", 42)
print(human.name)
print(human._age)  # Ця функція буде недоступна при імпорті класу до іншого файлу
try:
    print(human.__surname)
except:
    print("Атрибут surname має приватний модифікатор доступу\n\
Для його виведення потрібно використовувати метод get_surname")
print(human.get_surname())
