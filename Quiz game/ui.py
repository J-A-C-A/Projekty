import tkinter as tk
from tkinter import PhotoImage
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UserInterface:

    def __init__(self , quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("QuizGame")
        self.window.config(padx= 20 , pady= 20 , bg= THEME_COLOR)
        self.canvas = tk.Canvas(width= 300, height= 250 , highlightthickness= 0)
        self.canvas.config(bg= "white")
        self.canvas.grid(column= 0 , row= 1 , columnspan = 2 , pady=50)

        check_image = PhotoImage(file="true.png")
        self.check_button = tk.Button(image= check_image, command= self.true_answer , highlightthickness= 0)
        self.check_button.grid(column= 0 , row= 2)

        cross_image = PhotoImage(file="false.png")
        self.cross_button = tk.Button(image= cross_image, command= self.false_answer , highlightthickness= 0)
        self.cross_button.grid(column= 1 , row= 2)

        self.question_text =  self.canvas.create_text(150 , 125 ,width=280 ,font=("Arial",20,"italic") , text="placeholder")
        self.score_label = tk.Label(text="Score" , font=("Arial",10,"normal") , fg="white", bg=THEME_COLOR , highlightthickness= 0)
        self.score_label.grid(column= 1 , row= 0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
          if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            new_question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text , text= new_question_text)
          else:
              self.canvas.itemconfig(self.question_text , text="You have reached the end of the quiz")
              self.canvas.config(bg="white")
              self.check_button.config(state= "disabled")
              self.cross_button.config(state= "disabled")

    def true_answer(self):
       is_right = self.quiz.check_answer("True")
       self.give_feedback(is_right)



    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)



    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000 , self.get_next_question)

