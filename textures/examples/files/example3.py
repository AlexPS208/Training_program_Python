# Множинне розгалуження

a, b = 0, 1
bool1, bool2 = True, False


if a <= b:
    print("a <= b")
else:
    print("a > b")


if a != b:
    print("a != b")
else:
    print("a == b")


if a == b:
    print("a == b")
elif a-1 == b:
    print("a-1 == b")
elif a+1 == b:
    print("a+1 == b")
else:
    print("a != b, a-1 != b, a+1 != b")


if bool1:
    print("bool1 == True")
else:
    print("bool1 == False")


if bool2:
    print("bool2 == True")
else:
    print("bool2 == False")


# Форми запису розгалуджень

# 1)	Нормальна (повна) форма:

if a < 50:
    print("a < 50")
else:
    print("a >= 50")

# 2)	Коротка форма запису (тернарний вираз):

print("a < 50" if a < 50 else "a >= 50")

# 3)	If-elif-else (еквівалент switch case):

if a > 50:
    print("a > 50")
elif a == 50:
    print("a == 50")
else:
    print("a < 50")
