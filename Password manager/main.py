
import tkinter as tk
from tkinter import Canvas, PhotoImage
from tkinter.constants import END
from tkinter import messagebox
import random
import pyperclip
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    letters_list = [random.choice(letters)  for char in range(nr_letters)]
    numbers_list = [random.choice(numbers) for char in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for char in range(nr_symbols)]

    password_list = letters_list + numbers_list + symbols_list



    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0 , password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_input.get()
    user_name = username_input.get()
    password = password_input.get()

    new_data = {
        website_name: {
            "email": user_name,
            "password": password
        }
    }

    string_to_write = f"{website_name} | {user_name} | {password}\n"


    if len(website_name) == 0 or len(password) == 0:
        messagebox.showinfo("Ooops", "Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json" , "w") as file:
                json.dump(new_data , file , indent= 4)
        else:
            data.update(new_data)

            with open("data.json" , "w") as file:
                json.dump(data , file , indent= 4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

def find_password():
    website_name = website_input.get()
    try:
        with open("data.json" , "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=f"{website_name}" , message= f"email: {email}\n"
                                    f"password: {password}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website")






window = tk.Tk()
window.title("Password Generator")
window.config(padx=50 , pady=50)
canvas = Canvas(width=200 , height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100 , image=lock_image)
canvas.grid(column= 1 , row= 0)

website_label = tk.Label(text="Website:" , font=("Arial",18,"normal"))
website_label.grid(column=0 , row= 1)

username_label = tk.Label(text="Email/Username:", font=("Arial",18,"normal"))
username_label.grid(column= 0 , row= 2)

password_label = tk.Label(text="Password:", font=("Arial",18,"normal"))
password_label.grid(column= 0 , row= 3)

generate_button = tk.Button(text= "Generate Password", command= generate_password ,font=("Arial",12,"normal"))
generate_button.grid(column= 2, row= 3)

add_button = tk.Button(text= "Add" ,command= save , font=("Arial",12,"normal") , width= 36)
add_button.grid(column= 1, row= 4 , columnspan= 2)

search_button = tk.Button(text= "Search", command= find_password,font=("Arial",12,"normal") , width= 17)
search_button.grid(column= 2 , row= 1)

website_input = tk.Entry(window , width= 23)
website_input.focus()
website_input.grid(column= 1 , row= 1 , columnspan= 1)

username_input = tk.Entry(window , width= 48)
username_input.insert(0 , "przykładowy@gmail.com")
username_input.grid(column= 1 , row= 2 , columnspan= 2)

password_input = tk.Entry(window , width= 23)
password_input.grid(column= 1 , row= 3 , columnspan= 1)


window.mainloop()
