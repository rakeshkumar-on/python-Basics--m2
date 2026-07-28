def check_age():
    age = int(input())
    
    if age < 0:
        print("Invalid age")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 59:
        print("Adult")
    else:
        print("Senior")

if __name__ == "__main__":
    check_age()