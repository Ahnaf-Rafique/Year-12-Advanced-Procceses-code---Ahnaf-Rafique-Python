def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# score board
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# loop-
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------
#quiz question and options

questions = {
    "what do you do if you do not have housing?: ": "A",
    "what are the reasons for why people are in poverty?: ": "B",
    "what is the reasoning for why today people are in poverty and lack in finance?: ": "C",
    "what is the average age for a individual who is in poverty?: ": "A"
}

options = [["A. Google for homeless housing or use the location app", "B. Live outside or a public space",
           "C. Go find and live in an abandoned building" ],
            ["A. Lack in education", "B. Lack of funds, support in state and to measure poverty", "C. Low end job"],
            ["A. Certain changes in the law", "B. Tax's", "C. Pandemic's like COVID 19"],
            ["A. ages 30 to 50", "B. under 18", "C. ages 21 to 30"]]
new_game()

while play_again():
    new_game()

print("Byeeeeee!")

# -------------------------
