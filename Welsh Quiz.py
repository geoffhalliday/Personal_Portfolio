# This program allows the user to choose whether to do an English to Welsh or Welsh to English quiz
# Each question selects (and removes) 5 words from the English/Welsh word lists
# All of these 5 words are used as multiple choice answers, and one of the 5 is selected for the question
# The user selects the number of questions (max = length of word list/5)

import random

# sample list of English words and corresponding list of Welsh words
english = ["Hello", "Cheese", "Sausages", "Water", "Night", "Day", "Leek", "Bread", "Morning", "Supermarket","Peas"]
welsh = ["Helo", "Caws", "Selsig", "Dwr", "Nos", "Dydd", "Cennin", "Bara", "Bore", "Archfarchnad","Pys"]

def quiz():
    score = 0
    if option =="1":  # Option 1 is an English to Welsh quiz (Language 1 is Welsh, 2 is English)
        list_1 = english
        list_2 = welsh
    else:             # Option 2 is a Welsh to English quiz (Language 1 is English, 2 is Welsh)
        list_1 = welsh
        list_2 = english
    for question in range(1,questions+1): # 'Questions' is the number of questions
        selected_1=[]  # Empty list to store 5 terms for language 1, selected for the question
        selected_2=[]  # Empty list to store 5 corresponding terms for language 2, selected for this question
        for x in range(5):
            y = random.randint(0,len(list_1)-1) # Random index number selected from 'list_1'
            selected_1.append(list_1.pop(y))  # Term added to language 1 selected terms list, and removed from source list
            selected_2.append(list_2.pop(y))  # Term added to language 2 selected terms list, and removed from source list
        word = random.randint(0,4)  # Index number selected to identify language 1 term used in question
        print("Question",question)
        print(f"Which of the following means '{selected_1[word]}'?") # Question with language 1 selected term
        for x in range(5):
            print(x+1,"-",selected_2[x])  # The 5 selected language 2 terms are listed as multiple choice answers
        answer = input("Enter answer (1-5): ")
        while True:  # Repeats until valid input
            if answer in ["1","2","3","4","5"]: # Checks for valid input
                break  # Iteration ends when valid answer selected
            else:
                answer = input("Invalid selection. Choose 1-5: ") # Error message and re-input if input invalid
        if answer == str(word+1): # Checks if answer is correct
            print("Correct")
            score +=1 # Score increases by 1
        else:
            print("Wrong")
    print(f"Your score is {score} out of {questions}") # Prints final score

print ("Welcome to the English/Welsh quiz")
print ()
print ("Please choose an option")
print ("1 - English to Welsh quiz")
print ("2 - Welsh to English quiz")
option = input("Enter your option: ")
while True:  # Repeats until valid input
    if option in ["1", "2"]:  # Checks for valid input
        break  # Iteration ends when valid answer selected
    else:
        option = input("Invalid selection. Choose 1 or 2: ") # Error message and re-input if input invalid
while True:  # Repeats until valid input
    questions = input("How many questions? ")
    try:
        questions = int(questions)  # Checks if input is an integer
        if questions < 1:
            print ("Positive numbers only")  # Error message if number of questions negative or zero
        elif questions*5 <= len(welsh):  #  Cndition met if there are not too many questions
            break  # End iteration as input is valid
        else:
            print ("Too many questions")  # Error message if there are too many questions
    except ValueError:
        print("Error - not a number")  # Exception if data other than integer is input
quiz()
        

    
    



