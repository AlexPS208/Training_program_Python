# 1.	Оператор присвоювання =.
variable1 = 2
variable2 = 3+3
string1 = "Hello, "
string2 = "World!"


print(variable1, variable2, '\n', string1, string2, '\n')

# 2.	Оператор складання або конкантенації +.

sum = variable1+variable2
concatenation = string1+string2

print(sum, '\n', concatenation, '\n')

# 3.	Оператор множення *.

multiplication = variable1*variable2
multiplication_for_string = string1*3

print(multiplication, '\n', multiplication_for_string, '\n')

# 4.	Арифметичні оператори -, /, **.

minus = variable2-variable1
divisor = variable1/variable2
exponentiation = variable2**variable1

print(minus, divisor, exponentiation, '\n')

# 5.	Логічні оператори ~, >>, <<, &, |, ^.

inversion = ~variable1
lshift = variable1 << variable2
rshift = variable1 >> variable2
i = variable1 & variable2
abo = variable1 | variable2
xor = variable1 ^ variable2

print(inversion, lshift, rshift, i, abo, xor, '\n')

# Типи данних

print(type(4))
print(type(4.2))
print(type("string"))
print(type(True), '\n')

# Функції

a = int(input('Введіть ціле число '))
print(a)
a += 0.2749675
print(a, round(a, 2))
