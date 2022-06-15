# Списки

main_list = ['a', 4, -3.8, True, '8']
empty_list = []

print(main_list[0])
print(main_list[-1])
print(main_list[:2])
print(main_list[2:])
print(main_list[::-1])

main_list[-1] = 8
print(main_list)

main_list.append('9')
print(main_list)

main_list.insert(1, -2)
print(main_list)

main_list.pop(-2)
print(main_list)

del main_list[1]
print(main_list)


# Кортежи

main_tuple = ('a', 4, -3.8, True, '8')
empty_tuple = ()

print(main_tuple[0])
print(main_tuple[-1])
print(main_tuple[:2])
print(main_tuple[2:])
print(main_tuple[::-1])
