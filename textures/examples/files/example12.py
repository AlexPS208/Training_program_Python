# Створення багатомірного масиву та його індексація

sub_list = [1, 2]
sub_tuple = (5, 6)
sub_dict = {8: 'a', 9: 'b', 10: 'c'}
main_list = [sub_list, 3, 4, sub_tuple, 7, sub_dict]
print(main_list)


print(main_list[3])
print(main_list[3][1])

print(main_list[-1][8])


main_dict = {
    1: sub_list,
    2: sub_tuple,
    3: sub_dict
}
print(main_dict)


print(main_dict[3])
print(main_dict[3][9])
print(main_dict[2][0])


# Дії з багатомірними масивами

for i in main_list:
    if type(i) in (list, tuple, set):
        for k in i:
            print(k, end=" ")
    elif type(i) == dict:
        for k in i:
            print(i[k], end=" ")
    else:
        print(i, end=" ")

print()


# Рекурсія

def recurs(arr):
    for i in arr:
        if type(i) in (list, tuple, set):
            recurs(i)
        elif type(i) == dict:
            for k in i:
                recurs(i[k])
        else:
            print(i, end=" ")


recurs((1, 2, main_list, sub_list, sub_dict))
