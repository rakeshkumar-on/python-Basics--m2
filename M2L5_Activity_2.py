# M2L5_Activity_2.py
def floyds_triangle():
    rows = int(input())
    num = 1
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(num, end=" ")
            num += 1
        print()

if __name__ == "__main__":
    floyds_triangle()