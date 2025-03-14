## turtle only work with gif
import turtle 
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=800, height=600)
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)



df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
x = df['x'].to_list()
y = df['y'].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 states", prompt="What's the state name?").title()

    if answer_state == "Exit": 
        missing_states = [ state for state in all_states if state not in guessed_states ]
        #for state in all_states:
        #    if state not in guessed_states:
        #        missing_states.append(state)
        #print(missing_states)
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        index = df[df['state'] == answer_state].index[0]
        xcor = x[index]
        ycor = y[index]
        t.goto(xcor,ycor)
        t.write(f"{answer_state}")
        guessed_states.append(answer_state)


turtle.mainloop()

# def get_mouse_click_coor(x,y): 
#    print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)

#screen.exitonclick()