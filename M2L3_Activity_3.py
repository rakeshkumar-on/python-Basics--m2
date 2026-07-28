# M2L3_Activity_3.py
def check_armstrong():
    num = int(input())
    temp = num
    sum_val = 0
    digits = len(str(num))
    
    while temp > 0:
        digit = temp % 10
        sum_val += digit ** digits
        temp //= 10
        
    if num == sum_val:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

if __name__ == "__main__":
    check_armstrong()