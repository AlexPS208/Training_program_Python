# Запис у текстовий файл

file = open("new_text_file.txt", "w")
file.write("Some string\nSome numbers\n1 2 3 4 5")
file.close()

# Відкриття текстового файлу
# Читання текстового файлу

with open("new_text_file.txt", 'r') as temp:
    data = temp.read()
    print(data)
    temp.close()

# Модифікація текстового файлу

data = data.split("\n")[-1]
data = data[::-1]

with open("new_text_file.txt", 'a') as temp:
    temp.write("\n")
    temp.write(data)
    temp.close()


# Перевірка модифікації

with open("new_text_file.txt", 'r') as temp:
    print(temp.read())
    temp.close()
