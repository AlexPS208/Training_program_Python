# Корисні вбудовані функції

def test():
    print(ord('r'))
    print(chr(114))
    print(len('qwerty'))
    print(abs(-17.25))
    print(round(1141.12345, -2))
    print(divmod(27, 5))
    print(max('abc', '10', '01', '1k'))
    print(min('abc', '10', '01', '1k'))
    print(sum((1, 2, 3, 4, 5)))

# test()


# Створення власної бібліотеки

def plus(a, b):
    return a+b


def minus(a, b):
    return a-b


def multiply(a, b):
    return a*b


def diverse(a, b):
    return a/b
