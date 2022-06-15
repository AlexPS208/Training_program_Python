# Створення функції

def test(a):
    return a**2


print(test(5))


# Локальні та глобальні змінні

a = 5


def function(a):
    a += 5
    return a


print(function(2.5))
print(a)


# Значення параметра за замовченням

def func(a=3):
    return a**2


print(func())
print(func(5))
