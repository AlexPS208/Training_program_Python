# Генератори списків

gen_list = [i+1 for i in range(10)]
print(gen_list)

new_gen_list = [i for i in range(1, 11) if i % 2 == 0]
print(new_gen_list)

gen_tuple = tuple([i for i in range(1, 11)])
print(gen_tuple)

# Генератори словників та множин

gen_dict = {i+1: str(gen_tuple[i]) for i in range(10)}
print(gen_dict)

gen_set = {i for i in range(1, 11)}
print(gen_set)

# Функції map() та lambda

modify_list = list(map(lambda x: x*2, gen_list))
print(modify_list)
