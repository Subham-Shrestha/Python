import random
a = int(input("Enter level from (1 - 3)"))
d = 5
while (d >= 1) :
    if a == 1 :
        b = random.randint(0, 20)
    c = int(input("Enter the number generated : "))
    if c == b :
        print("That's a correct guess!!")
        break
    else :
        d = d -1
        print("That's incorrect!!")
print("The correct generated number was " + " " + b)