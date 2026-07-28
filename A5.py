def sum_of_whole_numbers():
    n = int(input())
    total_sum = 0
    i = 1
    while i <= n:
        total_sum += i
        i += 1
    print(total_sum)

if __name__ == "__main__":
    sum_of_whole_numbers()