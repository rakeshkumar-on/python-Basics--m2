# M2L5_Activity_1.py
def right_angle_triangle():
    rows = int(input())
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    right_angle_triangle()