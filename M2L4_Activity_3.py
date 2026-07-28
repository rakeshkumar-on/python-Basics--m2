# M2L4_Activity_3.py
def mid_product():
    num = int(input())
    num_str = str(num)
    length = len(num_str)
    
    if length % 2 == 0:
        mid1 = int(num_str[(length // 2) - 1])
        mid2 = int(num_str[length // 2])
        print(mid1 * mid2)
    else:
        mid = int(num_str[length // 2])
        print(mid * mid)

if __name__ == "__main__":
    mid_product()