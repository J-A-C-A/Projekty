import random
from tkinter import PhotoImage
import pandas as pd
import tkinter as tk
BACKGROUND_COLOR = "#B1DDC6"
word = {}

def random_word():
    global word , flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(to_learn)
    canvas.itemconfig(language_label , text="French" , fill= "black")
    canvas.itemconfig(word_label , text=f"{word["French"]}" , fill= "black")
    canvas.itemconfig(canvas_image , image=front_card_image)
    flip_timer = window.after(3000, change_card)

def change_card():
    global word
    canvas.itemconfig(language_label , text= "English" , fill= "white")
    canvas.itemconfig(word_label , text= f"{word["English"]}" , fill= "white")
    canvas.itemconfig(canvas_image , image= back_card_image)


def check_if_know():
    global word , to_learn
    to_learn.remove(word)
    delete_word_from_list()
    random_word()

def delete_word_from_list():
    data_to_learn = pd.DataFrame(to_learn)
    data_to_learn.to_csv("words_to_learn.csv", index=False)

try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("french_words.csv")
    to_learn = data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")

window = tk.Tk()
window.title("Flash Cards Program")
window.config(padx=50 , pady=50 , bg= BACKGROUND_COLOR)
canvas = tk.Canvas(width=800, height=526 , highlightthickness= 0)
canvas.config(bg= BACKGROUND_COLOR)
front_card_image = PhotoImage(file="card_front.png")
back_card_image = PhotoImage(file="card_back.png")

canvas_image = canvas.create_image(400, 263, image= front_card_image)

flip_timer = window.after(3000 , change_card)

canvas.grid(column= 0 , row= 0 , columnspan = 2)

language_label = canvas.create_text(400 , 150 , font=("Arial",30,"italic") , text="French")
word_label = canvas.create_text(400 , 263 , font=("Arial",40,"bold") , text="Word")


cross_image = PhotoImage(file="wrong.png")
cross_button = tk.Button(image=cross_image, command= random_word , highlightthickness= 0)
cross_button.grid(column= 0 , row= 1)

check_image = PhotoImage(file= "right.png")
check_button = tk.Button(image= check_image, command= check_if_know , highlightthickness= 0)
check_button.grid(column= 1 , row=1)


random_word()
window.mainloop()