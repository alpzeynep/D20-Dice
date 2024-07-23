import random

while True:
    input("Press enter to roll a D20")
    d20= random.randint(1,20)
    print(d20)

    if d20 == 1:
        print("CRITICAL FAIL")
    if d20 == 20:
        print("CRITIL HIT")