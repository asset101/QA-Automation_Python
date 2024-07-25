import sys
import tkinter as tk
from tkinter import messagebox

def check_number():
    try:
        number = int(entry_number.get())
        if number > 7:
            messagebox.showinfo("Результат", "Привет")
            
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, введите число")

    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целочисленное число")

def check_name():
    name = entry_name.get()
    if name == "Вячеслав":
        messagebox.showinfo("Результат", "Привет, Вячеслав")
    else:
        messagebox.showinfo("Результат", "Нет такого имени")

def filter_multiples_of_three():
    try:
        array = list(map(int, entry_array.get().split()))
        result = [x for x in array if x % 3 == 0]
        messagebox.showinfo("Результат", f"Элементы массива, кратные 3: {result}")
               
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовой массив через пробел")

# Создание главного окна
root = tk.Tk()
root.title("Проверка числа, имени и массива")

# Метка и поле ввода для числа
label_number = tk.Label(root, text="Введите число:")
label_number.pack()
entry_number = tk.Entry(root)
entry_number.pack()

# Кнопка для проверки числа
button_check_number = tk.Button(root, text="Проверить число", command=check_number)
button_check_number.pack()

# Метка и поле ввода для имени
label_name = tk.Label(root, text="Введите имя:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Кнопка для проверки имени
button_check_name = tk.Button(root, text="Проверить имя", command=check_name)
button_check_name.pack()

# Метка и поле ввода для массива
label_array = tk.Label(root, text="Введите числовой массив через пробел:")
label_array.pack()
entry_array = tk.Entry(root)
entry_array.pack()

# Кнопка для проверки массива
button_check_array = tk.Button(root, text="Проверить массив", command=filter_multiples_of_three)
button_check_array.pack()

# Запуск главного цикла
root.mainloop()

try:
    sys.exit(0)
except SystemExit:
    print("Программа завершена")