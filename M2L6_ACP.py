# M2L6_ACP.py
import turtle

def draw_square():
    t = turtle.Turtle()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    turtle.done()

if __name__ == "__main__":
    draw_square()