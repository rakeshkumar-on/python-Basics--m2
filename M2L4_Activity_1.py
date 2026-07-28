# M2L4_Activity_1.py
def character_occurrence():
    string = input()
    char = input()
    count = 0
    for i in string:
        if i == char:
            count += 1
    print(count)

if __name__ == "__main__":
    character_occurrence()