import tkinter as tk
from tkinter import messagebox
import math

def calculate_factorial():
    try:
        number = int(entry.get())
        result = math.factorial(number)
        messagebox.showinfo("Результат", f"Факториал {number} равен {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число!")

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Вычисление факториала")

label = tk.Label(root, text="Введите число:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Вычислить", command=calculate_factorial)
calculate_button.pack(pady=10)

exit_button = tk.Button(root, text="Выход (p)", command=exit_program)
exit_button.pack(pady=10)

root.bind('<p>', lambda event=None: exit_program())  # Связываем выход с клавишей 'p'

root.mainloop()

