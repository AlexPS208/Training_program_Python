# імпортуємо Tkinter
import tkinter as tk

# створюємо головне вікно
win = tk.Tk()

# Налаштовуємо зовнішній вигляд вікна
w = win.winfo_screenwidth()/4           # Визначаємо ширину екрана
h = win.winfo_screenheight()/5          # Визначаємо висоту екрана
win.geometry('%dx%d+100+100' % (w, h))  # Виставляємо розмір вікна та його
#                                           відступ від верхнього лівого краю
win.title('Моя програма')               # Задаємо назву у заголовку вікна
win.configure(background='violet')      # Задаємо колір фону вікна

# Створюємо елементи
lab1 = tk.Label(win, width='20', text='Приклад тексту\nзверху',
                justify=tk.CENTER)          # Створюємо напис
lab2 = tk.Label(win, text='Приклад тексту\nсправа',
                justify=tk.RIGHT)           # Створюємо напис
lab3 = tk.Label(win, text='Приклад тексту\nзліва',
                justify=tk.LEFT)            # Створюємо напис
lab4 = tk.Label(win, width='20', text='Приклад тексту\nзнизу',
                justify=tk.CENTER)          # Створюємо напис

# Розташовуємо елементи у головному вікні
lab1.pack(side=tk.TOP)          # зверху у вікні
lab2.pack(side=tk.RIGHT)        # з правого боку вікна
lab3.pack(side=tk.LEFT)         # з лівого боку вікна
lab4.pack(side=tk.BOTTOM)       # знизу у вікні

# Запускаємо цикл обробки вікна
win.mainloop()
