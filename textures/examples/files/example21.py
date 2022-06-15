# Імпорт Tkinter
from tkinter import *


# Створення функціонального класу
class Noted():
    def __init__(self, master):
        # Створення текстового поля
        self.area = Text(master, height=1000, width=1,
                         bg='#93f5af', fg='#a30075', wrap=WORD)
        # Розташування текстового поля
        self.area.pack(side=LEFT, expand=1, fill=X)
        # Створення скроллера
        self.scroll = Scrollbar(master, command=self.area.yview)
        # Налаштування скроллера
        self.area.config(yscrollcommand=self.scroll.set)
        # Розташування скроллера
        self.scroll.pack(side=LEFT, fill=Y)

    def delet(self):
        """Функція очищення текстового поля (для закриття файлу)"""
        self.area.delete(1.0, END)

    def ins(self, s):
        """Функція вставлення тексту (для відкриття файлів)"""
        self.area.insert(1.0, s)

    def g(self):
        """Отримання тексту (для зберігання данних до файлу)"""
        return self.area.get(1.0, END)


def openfile(event):
    """Функція відкриття файлу"""
    file = open(ent.get())
    textarea.delet()
    textarea.ins(file.read())
    file.close()


def savefile(event):
    """Функція зберігання файлу"""
    file = open(ent.get(), 'w')
    file.write(textarea.g())
    file.close()


# Створення вікна, його налаштування
main = Tk()
main.geometry('510x500+200+200')
main.title('Блокнот')

# Створення розділу вікна (для нотатків)
frame2 = LabelFrame(main)
textarea = Noted(frame2)

# Створення розділу вікна (функціанальний)
frame1 = LabelFrame(main, bg='#789af0', padx=5)
ent = Entry(frame1, width=30, font='Arial, 14', justify=CENTER)
butsave = Button(frame1, width=11, text='Зберегти')
butopen = Button(frame1, width=11, text='Відкрити')

# Прив'язка кнопок
butsave.bind('<Button-1>', savefile)
butopen.bind('<Button-1>', openfile)

# Розташування елементів на екрані
frame1.pack(fill=X, side=TOP, padx=0, pady=0, ipadx=0, ipady=0)
ent.pack(side=LEFT)
butsave.pack(side=RIGHT, padx=0, pady=5)
butopen.pack(side=RIGHT, padx=5, pady=5)
frame2.pack(fill=BOTH, side=BOTTOM, padx=0, pady=0, ipadx=0, ipady=0)

# Цикл обробки
main.mainloop()
