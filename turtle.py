# character_turtle.py
import turtle

# --- Setup ---
screen = turtle.Screen()
screen.title("Karakter Turtle")
screen.setup(width=800, height=700)
screen.bgcolor("#eaf6ff")  # latar belakang

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)

# --- Helper functions ---
def go(x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()

def circle_fill(radius, color):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def semicircle(radius, extent=180):
    pen.begin_fill()
    pen.circle(radius, extent)
    pen.end_fill()

def draw_head(x=0, y=50, radius=120, color="#ffd49a"):
    go(x, y - radius)
    pen.color("black", color)
    pen.pensize(3)
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_eye(x, y, size=18):
    # white eyeball
    go(x, y)
    pen.color("black", "white")
    pen.pensize(2)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()
    # pupil
    go(x, y + 6)
    pen.color("black", "black")
    pen.begin_fill()
    pen.circle(size/2)
    pen.end_fill()
    # tiny sparkle
    go(x + size/3, y + size/2 + 3)
    pen.color("white")
    pen.begin_fill()
    pen.circle(size/6)
    pen.end_fill()

def draw_blush(x, y, radius=14, color="#ff9aa2"):
    go(x, y)
    pen.color("", color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_smile(x, y, radius=60):
    go(x - radius/1.5, y - 10)
    pen.setheading(-60)
    pen.pensize(4)
    pen.color("black")
    pen.down()
    pen.circle(radius, 120)
    pen.up()

def draw_body(x=0, y=-80, width=160, height=200, color="#8ecae6"):
    # simple oval body using stretched circles
    go(x, y)
    pen.color("black", color)
    pen.pensize(3)
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    # draw a rounded rectangle / oval-ish body
    pen.setheading(0)
    pen.forward(width/2)
    pen.circle(height/8, 90)
    pen.forward(width)
    pen.circle(height/8, 90)
    pen.forward(width/2)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
    pen.end_fill()
    pen.up()

def draw_arm(x, y, length=80, angle=200):
    go(x, y)
    pen.setheading(angle)
    pen.pensize(12)
    pen.color("#ffd49a")
    pen.down()
    pen.forward(length)
    # hand (circle)
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()
    pen.up()
    pen.pensize(2)

def draw_leg(x, y, length=90, angle=-90):
    go(x, y)
    pen.setheading(angle)
    pen.pensize(12)
    pen.color("#7b6eaa")
    pen.down()
    pen.forward(length)
    # foot
    pen.begin_fill()
    pen.right(90)
    pen.forward(20)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
    pen.forward(20)
    pen.end_fill()
    pen.up()
    pen.pensize(2)

def draw_hat(x, y):
    # simple beanie hat
    go(x - 70, y + 120)
    pen.color("black", "#ff6f91")
    pen.pensize(2)
    pen.down()
    pen.fillcolor("#ff6f91")
    pen.begin_fill()
    pen.setheading(0)
    pen.forward(140)
    pen.left(90)
    pen.circle(70, 180)
    pen.left(90)
    pen.forward(140)
    pen.end_fill()
    pen.up()
    # pompom
    go(x + 60, y + 180)
    pen.color("", "#ffe066")
    pen.begin_fill()
    pen.circle(14)
    pen.end_fill()

# --- Draw the character ---
# Head
draw_head(0, 70, 120, color="#ffd9b3")

# Eyes
draw_eye(-45, 110, size=22)
draw_eye(45, 110, size=22)

# Blush
draw_blush(-80, 90, 14)
draw_blush(80, 90, 14)

# Smile
draw_smile(0, 80, radius=60)

# Hat
draw_hat(0, 70)

# Body (simple rounded rectangle-ish)
# We'll draw a filled oval-like shape by drawing an ellipse with circles trick
go(-80, -40)
pen.pensize(3)
pen.color("black", "#9ad3bc")
pen.fillcolor("#9ad3bc")
pen.begin_fill()
pen.setheading(0)
pen.forward(160)
pen.circle(80, 90)
pen.forward(160)
pen.circle(80, 90)
pen.end_fill()
pen.up()

# Arms
draw_arm(-80, 20, length=90, angle=200)
draw_arm(80, 20, length=90, angle=-20)

# Legs
draw_leg(-40, -160, length=110, angle=-100)
draw_leg(40, -160, length=110, angle=-80)

# Optional: pocket on body
go(-30, -20)
pen.color("black", "#ffffff")
pen.pensize(2)
pen.down()
pen.fillcolor("#ffffff")
pen.begin_fill()
pen.setheading(-90)
pen.circle(30, 180)
pen.end_fill()
pen.up()

# Finish
go(0, -260)
pen.color("black")
pen.write("Turtle Character ✔", align="center", font=("Arial", 14, "normal"))

# keep window open until closed
turtle.done()