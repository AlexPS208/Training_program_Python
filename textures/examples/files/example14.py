# Створення бінарного файлу, модуль pickle

import pickle

with open('new_binar_file', 'wb') as temp:
    data = "Some string\n1 2 3 4 5"
    pickle.dump(data, temp)
    temp.close()

with open('new_binar_file', 'rb') as temp:
    print(pickle.load(temp))
    temp.close()


# Модуль os

import os

print(os.path.isfile("new_binar_file"))
print(os.path.isdir("new_binar_file"))
print(os.path.exists("new_binar_file"))

os.mkdir("new_folder")
os.rename("new_folder", "just_folder")
os.remove("new_binar_file")
os.rmdir("just_folder")
print(os.listdir())
print(os.stat("example14.py"))
