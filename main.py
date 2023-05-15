from tkinter import *

window=Tk()
window.minsize(width=300,height=300)
window.config(bg="lightblue")

#height
height_label=Label(text="Boyunuzu Giriniz: ",font=("calibri", 30, "bold"), bg="lightblue")
height_label.pack()

height_entry=Entry(width=20)
height_entry.pack()

#weight
weight_label=Label(text="Kilonuzu Giriniz: ",font=("calibri", 30, "bold"), bg="lightblue")
weight_label.pack()

weight_entry=Entry(width=20)
weight_entry.pack()

result=0
def calculate_bmi():
    global result
    a = int(weight_entry.get())
    b = int(height_entry.get())/100
    c=b**2
    result = a /c
    result_label.config(text=result)
    if (result<18.4):
        bmi_result_label.config(text="BMI is underweight")
    elif(result>18.4 and result<24.9):
        bmi_result_label.config(text="BMI is normal" )
    elif (result > 24.9 and result < 39.9):
        bmi_result_label.config(text="BMI is Overweight")
    else:
        bmi_result_label.config(text="BMI is  OBESE" )

#buton
calculate_btn=Button(text="hesapla", width=20,pady=10, command=calculate_bmi)
calculate_btn.pack()

#result
result_label=Label(text="BM index is here")
result_label.pack()
#result
bmi_result_label=Label(text="BMI result is here")
bmi_result_label.pack()
window.mainloop()