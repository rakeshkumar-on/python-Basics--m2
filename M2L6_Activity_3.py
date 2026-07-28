# M2L6_Activity_3.py
import turtle

def draw_spiral():
    t = turtle.Turtle()
    size = 0
    while size < 100:
        t.forward(size)
        t.right(90)
        size += 5
    turtle.done()

if __name__ == "__main__":
    draw_spiral()