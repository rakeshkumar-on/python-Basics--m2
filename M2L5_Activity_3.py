# M2L5_Activity_3.py
def diamond_pattern():
    n = int(input())
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
    for i in range(n - 1):
        print(" " * (i + 1) + "* " * (n - i - 1))

if __name__ == "__main__":
    diamond_pattern()