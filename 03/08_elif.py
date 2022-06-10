score = int(input())

# corner case
# 0-20
"""
if 0 <= score <= 20:
    if 17 <= score <= 20:
        print("A")
    else:
        if 14 <= score < 17:
            print("B")
        else:
            if 11 <= score < 14:
                print("C")
            else:
                if 8 <= score < 11:
                    print("D")
                else:
                    print("E")
else:
    print("Invalid score! you must enter a number between 0 and 20.")

if 0 <= score <= 20:
    if 17 <= score <= 20:
        print("A")
    if 14 <= score < 17:
        print("B")
    if 11 <= score < 14:
        print("C")
    if 8 <= score < 11:
        print("D")
    else:
        print("E")
else:
    print("Invalid score! you must enter a number between 0 and 20.")
"""

if 0 <= score <= 20:
    if 17 <= score <= 20:
        print("A")
    elif 14 <= score < 17:
        print("B")
    elif 11 <= score < 14:
        print("C")
    elif 8 <= score < 11:
        print("D")
    else:
        print("E")
else:
    print("Invalid score! you must enter a number between 0 and 20.")
