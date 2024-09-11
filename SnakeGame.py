from tkinter import *
import random

GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 50
SPACE_SIZE = 45
BODY_PARTS = 3
SNAKE_COLOR = "#4eba6b"
FOOD_COLOR = "#ff0000"
BACKROUND_COLOR = "#000000"



class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass


window = Tk()
window.title("SnakeGame")
window.resizable(False, False)


score = 0
direction = "right"

label = Label(window, text="Score:{}".format(score), font=("Arial", 20))
label.pack()

canvas = Canvas(window, bg=BACKROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH )
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()

window.mainloop()
