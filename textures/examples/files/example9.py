# Функції range(), enumerate()

main_range = range(5, 21)
print(main_range)
print(type(main_range))

for i in main_range:
    print(i, end=" ")

print()


arr = list(range(0, 15, 2))
print(arr)

for i in range(len(arr)):
    print(str(i)+":"+str(arr[i]), end=" ")

print()


for key, elem in enumerate(arr):
    print(str(key)+":"+str(elem), end=" ")

print()


# Кострукція try-except

a = " some string "
try:
    print(a*2)
except:
    print("Error")


try:
    print(a**2)
except:
    print("Error")
