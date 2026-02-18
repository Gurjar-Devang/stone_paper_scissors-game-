import random

def game_win(user, computer):
    if user == computer:
        return None
    # stone vs pepar
    if user == "s" and computer == "p":
        return False
    if user == "p" and computer == "s":
        return True
    # pepar vs cheger
    if user == "p" and computer == "c":
        return False
    if user == "c" and computer == "p":
        return True
    # cheger vs stone
    if user == "c" and computer == "s":
        return False
    if user == "s" and computer == "c":
        return True


rand_no = random.randint(1, 3)
print("computer turn : stone(s) , pepar(p) , cheger(c)")

if rand_no == 1:
    computer = "s"
elif rand_no == 2:
    computer = "p"
else:
    computer = "c"

user = input("your turn : stone(s) , pepar(p) , cheger(c): ").lower()

result = game_win (user, computer)
print(f"\nyou choose : {user}")
print(f"\ncoputer choose : {computer}")

if result is None :
    print ("it's draw!")
elif (result):
    print("yoy win")
else :
    print("you lose")