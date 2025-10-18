import turtle
import time
import random

# --- Game Setup ---
delay = 0.1
score = 0
high_score = 0

# Screen setup
win = turtle.Screen()
win.title("🐍 Snake Game (Python)")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)  # Turn off auto screen updates

# --- Snake Head ---
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# --- Food ---
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

# --- Body Segments ---
segments = []

# --- Score Display ---
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 18, "normal"))

# --- Game Over Display ---
game_over_text = turtle.Turtle()
game_over_text.speed(0)
game_over_text.color("red")
game_over_text.penup()
game_over_text.hideturtle()
game_over_text.goto(0, 0)

# --- Movement Functions ---
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# WASD movement bindings
def w_up(): go_up()
def s_down(): go_down()
def a_left(): go_left()
def d_right(): go_right()

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# --- Reset Function ---
def reset_game():
    global score
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))
    game_over_text.clear()

# --- Keyboard Bindings ---
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Also bind WASD keys
win.onkeypress(w_up, "w")
win.onkeypress(s_down, "s")
win.onkeypress(a_left, "a")
win.onkeypress(d_right, "d")

# --- Main Game Loop ---
while True:
    win.update()

    # Check for collision with wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over_text.write("💀 GAME OVER 💀", align="center", font=("Courier", 30, "bold"))
        reset_game()

    # Check for collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        # Update score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 18, "normal"))

    # Move the snake body
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move first segment to where the head was
    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for collision with itself
    for segment in segments:
        if segment.distance(head) < 20:
            game_over_text.write("💀 GAME OVER 💀", align="center", font=("Courier", 30, "bold"))
            reset_game()

    time.sleep(delay)
