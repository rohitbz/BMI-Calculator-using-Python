import tkinter
import sqlite3
from tkinter import *
from tkinter import messagebox



def save_data(gender, height, weight, bmi):
    conn = sqlite3.connect('data1.db')
    c = conn.cursor()


    c.execute('''CREATE TABLE IF NOT EXISTS bmi_data
                 (gender varchar(10),
                  height REAL,
                  weight REAL,
                  bmi REAL)''')
    c.execute("INSERT INTO bmi_data (gender, height, weight, bmi) VALUES (?, ?, ?, ?, ?)",
              (gender, height, weight, bmi))
    conn.commit()
    conn.close()


def reset_entry():
    age.delete(0, 'end')
    height.delete(0, 'end')
    weight.delete(0, 'end')

def calculate_bmi():
    kg = float(weight.get())
    m = float(height.get()) / 100
    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('Results', f'BMI = {bmi} is Underweight')
    elif 18.5 <= bmi < 24.9:
        messagebox.showinfo('Results', f'BMI = {bmi} is Normal')
    elif 24.9 <= bmi < 29.9:
        messagebox.showinfo('Results', f'BMI = {bmi} is Overweight', icon='warning')
    elif bmi >= 29.9:
        messagebox.showinfo('Results', f'BMI = {bmi} is Obesity', icon='warning')
    else:
        messagebox.showerror('Results', 'something went wrong!')

ws = Tk()
ws.title('Results')
ws.geometry('300x350')
ws.config(bg='lightblue')

var = IntVar()

frame = Frame(
    ws,
    padx=25,
    pady=25
)
frame.pack(expand=True)

age_lb = Label(
    frame,
    text="Enter Age (2 - 120)", bg='yellow'
)
age_lb.grid(row=1, column=1)

age = Entry(
    frame,
)
age.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender', bg='yellow'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text='Male',
    variable=var,
    value=1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text='Female',
    variable=var,
    value=2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Enter Height (cm)  ", bg='yellow'
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ", bg='yellow'
)
weight_lb.grid(row=4, column=1)

height = Entry(
    frame,
)
height.grid(row=3, column=2, pady=5)

weight = Entry(
    frame,
)
weight.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate', bg='pink',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset', bg='pink',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit', bg='pink',
    command=lambda: ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()
