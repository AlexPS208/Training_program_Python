# Створення класу
class Table():
    w = 10
    h = 15

    # Створення функцій класу
    def square(self):
        return Table.w*Table.h


# Створення об’єкту

table = Table()

print(table.square())

# Атрибут __dict__

print(Table.__dict__)
