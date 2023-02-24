import random

player1_score = 0


four_side = random.randint(1,4)
six_side = random.randint(1,6)
eight_side = random.randint(1,8)
ten_side = random.randint(1,10)
twelve_side = random.randint(1,12)
twenty_side = random.randint(1,20)


player_choice = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))

for i in range(3):

    if(player_choice == "4"):
        print(four_side)
