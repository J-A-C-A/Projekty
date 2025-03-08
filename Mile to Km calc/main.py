import tkinter as tk

def mile_to_kilometer():
    miles = float(miles_input.get())
    km = round(miles * 1.60934 ,2)
    label_4.config(text=f"{km}")

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20 , pady=20)

label_1 = tk.Label(text="Miles", font=("Arial", 18, "normal"))
label_1.grid(column=2, row= 0)

label_2 = tk.Label(text="Km" , font=("Arial", 18, "normal") )
label_2.grid(column=2, row= 1)

label_3 = tk.Label(text="is equal to:" , font=("Arial", 18, "normal"))
label_3.grid(column=0, row= 1)

label_4 = tk.Label(text= "0" , font=("Arial", 18, "normal"))
label_4.grid(column=1, row= 1)

button_1 = tk.Button(text="Calculate", command= mile_to_kilometer)
button_1.grid(column= 1, row= 2)


miles_input = tk.Entry(window, width=10)
miles_input.grid(column=1, row=0)



window.mainloop()