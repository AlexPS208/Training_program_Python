# Атрибути класів

class Table():
    item = "table"
    amount = 0

    # Атрибути об'єктів
    def __init__(self, w=1.2, h=1.5, material="wood"):
        self.width = w
        self.height = h
        self.material = material
        Table.amount += 1

    # При видаленні об'єкту
    def __del__(self):
        print("table was broken")
        Table.amount -= 1


table1 = Table()
table2 = Table(2, 2.5, "iron")
table3 = Table(1, material="plastic")

print(Table.amount)
print("table 1:", table1.__dict__)
print("table 2:", table2.__dict__)
print("table 3:", table3.__dict__)

del table2

print(Table.amount)
