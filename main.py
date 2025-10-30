import random

Max_Number = 26

players = random.randint(2, 10)

print("there are", players, "people playing fizzbuzz today")
print()

# for h in range(players):
#     player_talk =+ h+1 
#     print()
for i in range (1, Max_Number+1):
    if i % 3 == 0:
        print("P", h+1 , ": fizz")
    elif i % 5 == 0:
        print("P", h+1 , ": buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("P", h+1 , ": fizzbuzz")
    else:
        print("P", h+1 , ":", i)
