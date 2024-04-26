import random

import time
time.sleep(1)

# The clear function is used to clear the screen when view in command line
# In IDLE this results in a flash of command line and doesn't benefit the program
import os
def clear():
    os.system("cls")
    time.sleep(1)

# This function is used to verify input is an integer and in the valid range
def number_choice(low,hi):
    while True:
        try:
            temp = int(input("Enter number: "))
            if temp > hi:
                print("Too high")
            elif temp < low:
                print("Too low")
            else:
                return(temp)
        except ValueError:
            print("Not a number")

# Scores of both teams set to zer for start of game
scoreA = 0
scoreB = 0

# List of scorers to be printed at the end of the game
scorers = []

# List of football team names and players for each team
teams = ["FC Patel  ", "Habib Town", "Hallidays ", "Honley Utd", "ICT AFC   ", "Tech Town "]
players0 = ["Tee", "Yusuf", "Khadiga", "Aminah", "Mariyah"]
players1 = ["Habinho", "Biscuiteeta", "E Bey-Buyer", "Pill-Swallow", "Hugh Japetight"]
players2 = ["Geoff", "Debs", "Dan", "Emily", "Lowd Carr"]
players3 = ["E Block", "A Block", "Field", "Hall", "Jim"]
players4 = ["Rehman", "Patel", "Halliday", "Uncle Joe", "Moore-Bebras"]
players5 = ["Ken", "Clarence", "Ayub", "Switchovanon", "Webb-Down"]
players = [players0, players1, players2, players3, players4, players5]

print("Choose first team")
for x in range(6):
    print(x, "-", teams[x])
A = number_choice(0,5)
Ateam = teams[A]
print("Enter Defence rating (1-9)")
AteamD = number_choice(1,9)
print("Enter Midfield rating (1-9)")
AteamM = number_choice(1,9)
print("Enter Forward rating (1-9)")
AteamF = number_choice(1,9)
playersA = players [A] 

clear ()

B=A 
while B==A:
    print("Choose second team")
    for x in range(6):
        print (x, "-", teams[x])
    B = number_choice(0,5)
    if B==A:
        print("Cannot select the same team")
Bteam = teams[B]
print("Enter Defence rating (1-9)")
BteamD = number_choice(1,9)
print("Enter Midfield rating (1-9)")
BteamM = number_choice(1,9)
print("Enter Forward rating (1-9)")
BteamF = number_choice(1,9)
playersB = players [B] 

clear ()

print("RATINGS   ", Ateam, "vs ", Bteam)
print("Defence     ", AteamD, "            ", BteamD)
print("Midfield    ", AteamM, "            ", BteamM)
print("Forward     ", AteamF, "            ", BteamF)

time.sleep(3)
print
print
input("Press Enter to continue")

########################
###                  ###
###   Start of Game  ###
###                  ###
########################

clear()

time.sleep(2)

temp = AteamM + BteamM
MidfieldA = AteamM/temp # Ratio of midfield ratings will be used to determine probability of each chance falling to a team
chances = random.randint(8,14) # Total number of chances in the game

print(Ateam, scoreA, "-", scoreB, Bteam)
print("Kick off")

for x in range (chances):
    time.sleep(2)
    print()
    # Sets which team is attacking/defending
    if MidfieldA*100 > random.randint(1,99):
        team = Ateam
        attack = AteamF
        defence = BteamD
        Attackers = playersA
        Defenders = playersB
    else:
        team = Bteam
        attack = BteamF
        defence = AteamD
        Attackers = playersB
        Defenders = playersA

    OnBall = Attackers[random.randint(0,4)] # Selects player in possession
        
    print("Chance for",team)
    time.sleep(1)
    print(OnBall, "with the ball")
    time.sleep(1)

    if random.randint(1,2) == 1: 
        print(OnBall, "passes")
        while True:
            new = Attackers[random.randint(0,4)]
            if new != OnBall:
                OnBall = new
                break
    else:
        print (OnBall, "runs")

    time.sleep(1)

    while True:
        move = random.randint(1,4)
        if move == 1:
            print(OnBall, "runs")
        elif move == 2:
            print(OnBall, "passes")
            new = Attackers [random.randint(0,4)]
            tmp = 0
            while tmp == 0:
                if new == OnBall:
                    new = Attackers [random.randint(0,4)]
                else:
                    OnBall = new
                    tmp = 1
            
        elif move == 3:
            if defence > random.randint(0,8):
                print("Tackled by", Defenders [random.randint(0,4)])
                break
            else:
                print(OnBall, "skips challenge")
        else:
            print(OnBall,"shoots")
            time.sleep(1)
            if attack > random.randint(0,8):
                print("It's on target")
                time.sleep(1)
                if defence > random.randint(0,9):
                    print("Saved")
                else:
                    print("GOAL!!!!!")
                    time.sleep(2)
                    print(OnBall,"scores!!!")
                    scorers.append(OnBall)
                    if team == Ateam:
                        scoreA = scoreA + 1
                    else:
                        scoreB = scoreB + 1
                    print()
                    print(Ateam, scoreA, "-", scoreB, Bteam)
            else:
                print("Misses")
            break
        time.sleep(1)
print()
print("Full time")
print()
time.sleep(1)
print(Ateam, scoreA, "-", scoreB, Bteam)
time.sleep(1)
print()
print("Scorers are:")
for x in scorers:
    print (x)
print()
print()
input("Press Enter to exit")
