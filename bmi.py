import tkinter
from  tkinter import ttk
from tkinter import messagebox
import csv
from matplotlib import pyplot as plt

def    calculate_BMI():
    height = float(userheighttext.get())
    weight = float(userweighttext.get())
    bmi=round(weight/(height**2),2)
    user_name=usernametext.get()
    if bmi < 18.5:
        useroutcomelabel["text"]= f"BMI:your bmi level is {bmi} is Underweight"
    elif (bmi > 18.5) and (bmi < 24.9):
        useroutcomelabel["text"]=f"BMI:your bmi is {bmi} is Normal"
    elif (bmi > 24.9) and (bmi < 29.9):
        useroutcomelabel["text"] =f"BMI:YOUR bmi level is {bmi} is Overweight"
    elif (bmi > 29.9):
        useroutcomelabel["text"] = f"BMI:your bmi level is {bmi},is obesity"

    else:
        useroutcomelabel["text"] =f" something is wrong"

    with open("Bmidata.csv", "a") as filewriter:
        filewritercsv = csv.writer(filewriter)
        filewritercsv.writerow([height, weight, bmi,user_name])
def clear():
    userheighttext.delete(0,"end")
    userweighttext.delete(0,"end")
    usernametext.delete(0,"end")




window=tkinter.Tk()
window.title("BMI CALCULATOR ")
frame=tkinter.Frame(window)
frame.pack()

bmicalcframe=tkinter.LabelFrame(frame,text="Calculate BMI ")
bmicalcframe.grid(row=0,column=0,padx=10,pady=10)

username=tkinter.Label(bmicalcframe,text="Name")
username.grid(row=0,column=0, padx=10,pady=10)
usernametext=tkinter.Entry(bmicalcframe)
usernametext.grid(row=0,column=1,padx=10,pady=10)

userweightlabel=tkinter.Label(bmicalcframe,text="weight(kg)")
userweightlabel.grid(row=1,column=0,padx=10,pady=10)

userweighttext=tkinter.Entry(bmicalcframe)
userweighttext.grid(row=1,column=1,padx=10,pady=10)

userheightlabel=tkinter.Label(bmicalcframe,text="height(m)")
userheightlabel.grid(row=1,column=2,padx=10,pady=10)

userheighttext=tkinter.Entry(bmicalcframe)
userheighttext.grid(row=1,column=3,padx=10,pady=10)

useroutcomelabel=tkinter.Label(bmicalcframe,text="BMI")
useroutcomelabel.grid(row=2,column=0, padx=10, pady=10,sticky="news")



clearbutton=tkinter.Button(frame,text="clear",command=clear)
clearbutton.grid(row=3,column=0,padx=10,pady=10,sticky="ws")
calculatebutton=tkinter.Button(frame,text="Calculate BMI",command=calculate_BMI)
calculatebutton.grid(row=3,column=1,padx=10,pady=10,sticky="ne")

btn = tkinter.Button(frame, text='Show plot', command="plot")
btn.grid(row=3, column=2, padx=20, pady=10,sticky="news")
window.mainloop()
