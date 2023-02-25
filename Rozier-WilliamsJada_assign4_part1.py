import random
runner = True

while runner == True:
    player_choice = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
    if player_choice < 0:
        print("Invalid size, try again")

    die_side = random.randint(1, player_choice)

    roll1 = random.randint(1, player_choice)
    roll2 = random.randint(1, player_choice)
    roll3 = random.randint(1, player_choice)

    total_roll = roll1 + roll2 + roll3

    print(roll1, roll2, roll3)
    
    if roll1 % 2 == 1 and roll2 % 2 == 1 and roll3 % 2 == 1:
        print("Odd Roll")
    if roll1 % 2 == 0 and roll2 % 2 == 0 and roll3 % 2 == 0:
        print("Even Roll")
    if roll1 * roll2 == roll3:
        print("Multiple Roll")
    if roll1 + roll2 == roll3:
        print("Sum Roll")
    if total_roll == True:
        print("Total Roll")
