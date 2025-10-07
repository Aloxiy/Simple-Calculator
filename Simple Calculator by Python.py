"""
@Author: Pranta Sarker (модифицировано для тестов и работы интерфейса)
"""

from tkinter import *
from tkinter import messagebox

# ========== ЛОГИЧЕСКИЕ ФУНКЦИИ (тестируемые) ==========

def is_number(s):
    """Проверяет, является ли строка числом"""
    if s == '':
        return False
    s = s.strip().replace(',', '.')
    try:
        float(s)
        return True
    except ValueError:
        return False


def casting(num):
    """Преобразует строку в число (int или float)"""
    num = num.replace(',', '.')
    if '.' in num:
        return float(num)
    return int(num)


def add(a, b):
    """Сложение"""
    if not (is_number(a) and is_number(b)):
        raise ValueError("Invalid numbers")
    return casting(a) + casting(b)


def sub(a, b):
    """Вычитание"""
    if not (is_number(a) and is_number(b)):
        raise ValueError("Invalid numbers")
    return casting(a) - casting(b)


def mul(a, b):
    """Умножение"""
    if not (is_number(a) and is_number(b)):
        raise ValueError("Invalid numbers")
    return casting(a) * casting(b)


def div(a, b):
    """Деление"""
    if not (is_number(a) and is_number(b)):
        raise ValueError("Invalid numbers")
    b_val = casting(b)
    if b_val == 0:
        raise ZeroDivisionError("Division by zero")
    return casting(a) / b_val


# ========== GUI-ФУНКЦИИ (интерфейс) ==========

def actionauthor():
    messagebox.showinfo("Author", "Pranta Sarker\nBatch: 6th\nDepartment: CSE\nNorth East University Bangladesh")


def actionPlus():
    try:
        num1 = Numberentry1.get()
        num2 = Numberentry2.get()
        ans = add(num1, num2)
        Showlabel.delete(0, END)
        Showlabel.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def actionMinus():
    try:
        num1 = Numberentry1.get()
        num2 = Numberentry2.get()
        ans = sub(num1, num2)
        Showlabel.delete(0, END)
        Showlabel.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def actionMul():
    try:
        num1 = Numberentry1.get()
        num2 = Numberentry2.get()
        ans = mul(num1, num2)
        Showlabel.delete(0, END)
        Showlabel.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def actionDiv():
    try:
        num1 = Numberentry1.get()
        num2 = Numberentry2.get()
        ans = div(num1, num2)
        Showlabel.delete(0, END)
        Showlabel.insert(0, str(ans))
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ========== ЗАПУСК GUI ТОЛЬКО ПРИ ПРЯМОМ ЗАПУСКЕ ==========

if __name__ == "__main__":
    global root, Numberentry1, Numberentry2, Showlabel

    root = Tk()
    root.title('My First Python Calculator')
    root.geometry('380x300+200+250')

    Titlelabel = Label(root, fg='green', font='none 10 bold underline',
                       text='Python Calculator', compound=CENTER)
    Titlelabel.place(relx=0.5, rely=0.1, anchor='center')

    Numberentry1 = Entry(root)
    Numberentry2 = Entry(root)
    Showlabel = Entry(root)

    Numberentry1.place(relx=0.5, rely=0.3, anchor='center')
    Numberentry2.place(relx=0.5, rely=0.4, anchor='center')
    Showlabel.place(relx=0.5, rely=0.5, anchor='center')

    Button(root, text="+", width=5, command=actionPlus).place(relx=0.1, rely=0.7)
    Button(root, text="-", width=5, command=actionMinus).place(relx=0.3, rely=0.7)
    Button(root, text="*", width=5, command=actionMul).place(relx=0.5, rely=0.7)
    Button(root, text="/", width=5, command=actionDiv).place(relx=0.7, rely=0.7)
    Button(root, text='Author', width=6, command=actionauthor).place(relx=0.5, rely=0.95, anchor='center')

    root.resizable(False, False)
    root.mainloop()
