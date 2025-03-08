import pandas as pd
import turtle



screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("States Game")
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
answers = []
score = 0
all_states = data.state.to_list()
while len(answers) < 50:
    user_answer = screen.textinput(title=f"Guess the State {score}/50",prompt="What's another state's name?")
    user_answer = user_answer.title()
    if user_answer == "Exit":
        print(answers)
        states_to_learn = [state for state in all_states if state not in answers]
        states_to_learn_df = pd.DataFrame(states_to_learn)
        states_to_learn_df.to_csv("states_to_learn.csv")
        break

    if user_answer in data["state"].values:
        state_data = data[data["state"] == user_answer]
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto( state_data.iloc[0]["x"] , state_data.iloc[0]["y"])
        new_turtle.write(user_answer)
        score += 1

        if user_answer not in answers:
            answers.append(user_answer)
    print(score)

screen.exitonclick()
