import tkinter as tk
from tkinter import Canvas, PhotoImage
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✔"
reps = 0
timer = None
#1 praca 25
#2 przerwa 5
#3 praca  25
#4 przerwa 5
#5 praca 25
#6 przerwa 5
#7 praca 25
#8 długa przerwa 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(canvas_text, text=f"00:00")
    checkmark_label.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN

    reps += 1

    if reps % 8 == 0:
        # przerwa 25
        count_down(1*60)
        timer_label.config(text= "Break" ,fg=RED)
    elif reps % 2 == 0:
        # przerwa 5
        count_down(1*30)
        timer_label.config(text= "Break" ,fg=PINK)
    else:
        timer_label.config(text= "Work" ,fg=GREEN)
        count_down(1*45)

    if reps == 2:
        checkmark_label.config(text=CHECK_MARK)
    elif reps == 4:
        checkmark_label.config(text=f"{CHECK_MARK}{CHECK_MARK}")
    elif reps == 6:
        checkmark_label.config(text=f"{CHECK_MARK}{CHECK_MARK}{CHECK_MARK}")


    print(reps)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvas_text , text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down , count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()

window.title("Pomodoro")
window.config(padx = 100 , pady = 50 , bg=YELLOW)
canvas = Canvas(width=200 , height=224 , bg=YELLOW , highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image= tomato_img)
canvas_text = canvas.create_text(100,130 , text= "00:00" , fill= "white" , font=(FONT_NAME,35,"bold"))
canvas.grid(column= 1, row= 1)


timer_label = tk.Label(text="Timer",font=(FONT_NAME,35,"bold"))
timer_label.config(fg=GREEN , bg=YELLOW , highlightthickness=0)
timer_label.grid(column= 1, row= 0)

start_button = tk.Button(text="Start", command= start_timer,font=(FONT_NAME,12,"bold"))
start_button.config(fg="black" , bg=YELLOW , highlightthickness=0 )
start_button.grid(column=0 , row=2)

reset_button = tk.Button(text="Reset", command= reset_timer,font=(FONT_NAME,12,"bold"))
reset_button.config(fg="black" , bg=YELLOW , highlightthickness=0 )
reset_button.grid(column=2 , row=2)

checkmark_label = tk.Label(text="" , font=(FONT_NAME,8,"bold"))
checkmark_label.config(fg= GREEN , bg=YELLOW , highlightthickness=0)
checkmark_label.grid(column= 1, row=3)


window.mainloop()