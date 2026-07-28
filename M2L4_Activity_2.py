# M2L4_Activity_2.py
def check_prime():
    num = int(input())
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Not a prime number")
                break
        else:
            print("Prime number")
    else:
        print("Not a prime number")

if __name__ == "__main__":
    check_prime()