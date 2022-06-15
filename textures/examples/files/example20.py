# Імпорт tkinter
import tkinter as tk


# Створення функціоналу
def output(event):
    text = ent.get()                # Взяття тексту з поля вводу
    result['text'] = str(text)      # Внесення тексту до текстового поля
    ent.delete(0, tk.END)           # Очищення поля вводу


# Створення головного вікна
win = tk.Tk()

# Налаштування зовнішнього вигляда вікна
w = win.winfo_screenwidth()/5           # Визначаємо ширину екрана
h = win.winfo_screenheight()/6          # Визначаємо висоту екрана
win.geometry('%dx%d+100+100' % (w, h))  # Розмір вікна
win.title('Моя програма')               # Назва програми
win.configure(background='lightpink')   # Фон вікна

# Створення елементів
lab = tk.Label(width='50', text='Введіть текст')    # Створюємо напис
ent = tk.Entry(width=30)                            # Поле для вводу
but = tk.Button(text='Переробити')                  # Кнопку
result = tk.Label(width='30', text='')              # Та пусте поле для напису

# Прив'язка елементів
but.bind('<Button-1>', output)

# Розташування елементів у вікні
lab.pack(side=tk.TOP)
ent.pack(side=tk.TOP)
but.pack(side=tk.TOP)
result.pack(side=tk.BOTTOM)

# Зациклення вікна
win.mainloop()
