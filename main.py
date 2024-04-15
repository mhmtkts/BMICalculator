from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(300, 200)


def cal_bmi():
    try:
        weight = float(Weight.get())
        height_cm = float(Height.get())
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 1)

        if bmi < 18.5:
            label.config(text=f"BMI: {bmi:.1f} (Underweight)")
        elif 18.5 <= bmi < 25:
            label.config(text=f"BMI: {bmi:.1f} (Normal Weight)")
        elif 25 <= bmi < 30:
            label.config(text=f"BMI: {bmi:.1f} (Overweight)")
        else:
            label.config(text=f"BMI: {bmi:.1f} (Obese)")
    except ValueError:
        label.config(text="Enter valid weight and height!")


vcmd = (window.register(cal_bmi), "%p")

my_label = Label(text="Enter Your Weight(kg)")
my_label.config(fg="black")
my_label.config(padx=0, pady=10)
my_label.pack()

Weight = Entry(width=15, validatecommand=vcmd)
Weight.pack()

my_label_2 = Label(window, text="Enter Your Height(cm)", )
my_label_2.config(fg="black")
my_label_2.config(padx=0, pady=10)
my_label_2.pack()

Height = Entry(width=15, validatecommand=vcmd)
Height.pack()

label = Label(window, text=" ", )
label.pack(pady=20)
label.place(x=90, y=160)

my_button = Button(text="Calculate", command=cal_bmi, width=10, )
my_button.pack()
my_button.place(x=110, y=125)

window.mainloop()
