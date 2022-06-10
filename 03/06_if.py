"""
selection statement
if keyword, reserved keyword
if = 12 INVALID

if condition:
    code block
"""

# "The weather is great!"
weather_is_good = True 

# "My car is clean!"
is_clean = True

# "The road is crowded!"
is_crowded = False 

if weather_is_good and is_clean:
    # code block
    # 4 spaces
    # indentation
    print("I'm going to travel!")

    if is_crowded:
        print("I'm coming back home!")
        
        if is_crowded:
            print("I'm coming back home!")
            

is_crowded = True
if is_crowded:
    print("I'm coming back home!")
    