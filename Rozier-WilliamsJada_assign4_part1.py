import random
runner = True
player1_score = 0

while runner == True:
    player_choice = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
    die_side = random.randint(1, player_choice)

    roll1 = random.randint(1, player_choice)
    roll2 = random.randint(1, player_choice)
    roll3 = random.randint(1, player_choice)

    print(roll1, roll2, roll3)

    if roll1 % 2 == 1 and roll2 % 2 == 1 and roll3 % 2 == 1:
        print("Odd Roll")
    if roll1 % 2 == 0 and roll2 % 2 == 0 and roll3 % 2 == 0:
        print("Even Roll")
