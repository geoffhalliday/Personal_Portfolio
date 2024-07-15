# To be run in command line - cls will not work in Idle
# The game play is inspired by the 1980s game Football Manager

import random
import time  # To allow pauses in the game for effect
time.sleep(1)

import os
def clear():  # To clear the screen (works in command line)
    os.system("cls")
    time.sleep(1)

# Initial team and player names (teams must be 10 characters)
teams = ["Albion FC ","Town FC   ","City FC   ","United FC ","County FC ","Wanderers "]
players0 = ["Andy","Alice","Anne","Alan","Alex"]
players1 = ["Beth","Ben","Bob","Bill","Betty"]
players2 = ["Clive","Claire","Carl","Chris","Cheryl"]
players3 = ["Dave","Dom","Daisy","Dot","Dee"]
players4 = ["Ellen","Eve","Eddie","Egbert","Elizabeth"]
players5 = ["Freddie","Frank","Florence","Frances","Floyd"]
players = [players0, players1, players2, players3, players4, players5]
ratings = [] 
team_rating = [] # defence, midfield, attack
# Randomly generating initial ratings for each team
for x in range (6):
    team_rating = [random.randint(1,9),random.randint(1,9),random.randint(1,9)]
    ratings.append(team_rating)

def game():
    clear()  # Clear screen
    time.sleep(2)  # Pause for 2 seconds
    scoreA = 0  # Team A's goals
    scoreB = 0  # Team B's goals
    scorers = []  # List of goal scorers

    # Midfield A used to determine the probablility of a chance being for team A
    MidfieldA = AteamM/(AteamM + BteamM)
    temp = random.randint(8,14) # Calculates total number of chances

    print (Ateam, scoreA, "-", scoreB, Bteam)
    print ("Kick off")

    for x in range (temp):  # Iterate through number of chances
        time.sleep(2)
        print ()
        if MidfieldA*100 > random.randint(1,99):  # Determines if chance is for Team A
            team = Ateam  # Attacking team set to team A
            attack = AteamF  # Team A attacking rating
            defence = BteamD  # Team B defending rating
            Attackers = playersA  # Team A players are attacking
            Defenders = playersB  # Team B players are defending
        else:  # Else chance is for Team B
            team = Bteam  # Attacking team set to team B
            attack = BteamF  # Team B attacking rating
            defence = AteamD  # Team A defending rating
            Attackers = playersB  # Team B players are attacking
            Defenders = playersA  # Team A players are defending
            
        OnBall = Attackers [random.randint(0,4)] # Selects the player in possession (OnBall)          
        print ("Chance for",team)
        time.sleep(1)
        print (OnBall, "with the ball")
        time.sleep(1)
        # Player in possession initially either passes or runs
        if random.randint(1,2) == 1:
            print (OnBall, "passes")
            while True:
                new = Attackers [random.randint(0,4)] # New player is in possession
                if new != OnBall:  # Check that new player is not existing player in possession
                    OnBall = new  
                    break
        else:
            print (OnBall, "runs")
        time.sleep(1)
        
        # Subsequent commentary for the chance
        while True:
            move = random.randint(1,4) # Random selection of next instance
            if move == 1:
                print (OnBall, "runs") # Player continues to run
            elif move == 2:
                print (OnBall, "passes")  # Player passes
                new = Attackers [random.randint(0,4)]  # New player is in possession
                #######
                
                #tmp = 0
                #while tmp == 0:
                    #if new == OnBall:
                        #new = Attackers [random.randint(0,4)]
                    #else:
                        #OnBall = new
                        #tmp = 1
                while True:
                    new = Attackers [random.randint(0,4)] # New player is in possession
                    if new != OnBall:  # Check that new player is not existing player in possession
                        OnBall = new  
                        break
            elif move == 3: # Attempted tackle
                if defence > random.randint(0,8): # Determines if tackle is successful
                    print ("Tackled by", Defenders[random.randint(0,4)]) # Tackling player selected
                    break  # Player has been tackled = end of chance
                else:
                    print (OnBall, "skips challenge") # Tackle not successful
            else:
                print (OnBall,"shoots") # Player shoots
                time.sleep(1)
                if attack > random.randint(0,8): # Attack rating determines if shot is on target
                    print ("It's on target")
                    time.sleep(1)
                    if defence > random.randint(0,9):  # Defence rating determines if shot is saved
                        print ("Saved")
                    else:
                        print ("GOAL!!!!!")  # Goal scored if shot on target and not saved
                        time.sleep(2)
                        print (OnBall,"scores!!!")  # Displays scorer
                        scorers.append(OnBall)  # Adds player to list of goal scorers
                        # Increase goals scored for team in possession
                        if team == Ateam:
                            scoreA = scoreA + 1
                        else:
                            scoreB = scoreB + 1
                        print()
                        print (Ateam, scoreA, "-", scoreB, Bteam)
                else:
                    print ("Misses") # Shot not on target
                break # Shot saved or scored - end of chance
            time.sleep(1)
    print ()
    print ("Full time")  # End of game
    print ()
    time.sleep(1)
    print (Ateam, scoreA, "-", scoreB, Bteam)  # Final score
    time.sleep(1)
    print ()
    print ("Scorers are:")
    print (scorers)   #  List of scorers
        
    print ()
    print ()
    input ("Press Enter to exit")



while True:
    clear()
    # Display main screen - list of teams and options
    print ("TEAM LIST:")
    for x in range (6):
        print(f"{x} - {teams[x]}")
    print ()
    print ("OPTIONS:")
    print ("1 - View teams")
    print ("2 - Edit names")
    print ("3 - Edit ratings")
    print ("4 - Play friendly match")
    #print (" - Play league")  ## Not yet done
    print ("5 - Exit game")
    print ()
    option = input("Choose an options (1-5): ")
    if option == "1":
        print ("VIEW TEAMS")
        choice = input("Choose team to view: ")
        choice = int(choice)
        print(teams[choice]) # Displays chosen team
        print()
        # Display player names
        print("Players:")
        for x in range(5):
            print (players[choice][x])
        print()
        # Display defence, midfield and attack ratings
        print("DEFENCE:", ratings[choice][0])
        print("MIDFIELD:", ratings[choice][1])
        print("ATTACK:", ratings[choice][2])
        print()
        input("Press ENTER to return to main menu")
    if option == "2":
        print ("EDIT NAMES")
        choice = input("Choose team to edit: ")
        choice = int(choice)
        new_name = input("Enter team name:") # Input new team name
        new_name = new_name + "         "  # Adding to ensure string is at least 10 characters
        teams[choice] = new_name[:10]  # String must be exactly 10 characters for neat printing
        # Input 5 player names for the team
        print (f"Enter names for {teams[choice]}")
        for x in range (5):
            players[choice][x] = input(f"Enter name for player {x}: ")
    if option == "3":
        print ("EDIT RATINGS")
        choice = input("Choose team to edit: ")
        choice = int(choice)
        # Input defence, midfield and attack ratings for chosen team
        print (f"Enter ratings for {teams[choice]}")
        ratings[choice][0] = int(input("Enter defence rating (1-9): "))
        ratings[choice][1] = int(input("Enter midfield rating (1-9): "))
        ratings[choice][2] = int(input("Enter attack rating (1-9): "))
    if option == "4":  # Friendly match selected
        temp = int(input("Enter first team number: ")) # Choose first team
        # Set variables for first team
        Ateam = teams[temp]
        AteamD = ratings[temp][0]
        AteamM = ratings[temp][1]
        AteamF = ratings[temp][2]
        playersA = players [temp] 
        temp = int(input("Enter second team number: ")) # Choose second team
        # Set variable for second team
        Bteam = teams[temp]
        BteamD = ratings[temp][0]
        BteamM = ratings[temp][1]
        BteamF = ratings[temp][2]
        playersB = players [temp] 
        clear ()
        # Display team names and ratings
        print ("RATINGS   ", Ateam, "vs ", Bteam)
        print ("Defence     ", AteamD, "            ", BteamD)
        print ("Midfield    ", AteamM, "            ", BteamM)
        print ("Forward     ", AteamF, "            ", BteamF)
        time.sleep(3)
        print
        print
        input ("Press Enter to continue")
        game() # Run the game
    if option == "5":
        print ("End of game")
        time.sleep(2)
        break

for x in scorers:
    print (x)
print()
print()
input("Press Enter to exit")
