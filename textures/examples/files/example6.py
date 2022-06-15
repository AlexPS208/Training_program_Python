# Словники

main_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
empty_dict = {}

print(main_dict['c'])
print(main_dict['a'])

main_dict[6] = 'f'
print(main_dict)

buf = main_dict[6]
main_dict[6] = 6
main_dict[buf] = main_dict.pop(6)
print(main_dict)

del main_dict['c']
print(main_dict)


# Множини

main_set = set('Hello, World!')
empty_set = set()

second_set = main_set.copy()
print(main_set)
print(second_set)

main_set.add('Hello')
print(main_set)

main_set.remove('e')
print(main_set)

main_set.pop()
print(main_set)

print(main_set & second_set)
print(main_set | second_set)
print(main_set - second_set)
print(main_set ^ second_set)
