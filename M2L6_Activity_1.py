# M2L6_Activity_1.py
import turtle

def draw_polygon():
    sides = int(input())
    length = int(input())
    angle = 360 / sides
    
    t = turtle.Turtle()
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
    turtle.done()

if __name__ == "__main__":
    draw_polygon()