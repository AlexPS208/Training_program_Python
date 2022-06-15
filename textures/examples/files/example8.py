# Цикл while

i = 1
while i < 20:
    i += 2
print(i)


# Оператори break, continue

i = 1
while(True):
    if i > 10:
        break
    else:
        i += 1
print(i)


i = 1
arr = []
while i < 10:
    i += 1
    if i % 2 == 1:
        continue
    arr.append(i)
print(arr)


# Цикл while для масивів

i = 0
while i < len(arr):
    print(arr[i], end="  ")
    i += 1


print()

# Цикл for

for i in arr:
    print(i, end="  ")

print()

for i in range(10):
    print(i+1, end="  ")

print()

arr = []
for i in range(100):
    if i % 2 != 0:
        continue
    elif i > 10:
        break
    arr.append(i)
print(arr)
