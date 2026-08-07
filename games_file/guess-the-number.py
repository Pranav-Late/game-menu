import random

high_scores = {'easy': None, 'medium': None, 'hard': None}

def difficulty(diff):
    if diff == 1:
        num = random.randint(1, 50)
        print("Guess the number between 1 to 50")
        return num, 'easy'
    elif diff == 2:
        num = random.randint(1, 100)
        print("Guess the number between 1 to 100")
        return num, 'medium'
    elif diff == 3:
        num = random.randint(1, 1000)
        print("Guess the number between 1 to 1000")
        return num, 'hard'
    else:
        print("Invalid Difficulty")
        return None

def play(num, level):
    global high_scores
    counter = 0
    while True:
        try:
            user_input = int(input("Enter a number: "))
        except ValueError:
            print("Invalid Input")
            continue
        counter += 1
        if user_input == num:
            print("Hurray! You guessed it correctly")
            print(f'Attempts = {counter}')
            if (high_scores[level] == None) or (counter < high_scores[level]):
                high_scores[level] = counter
                print(f"New high score for {level.title()}!")
            break
        elif user_input > num:
            print("The answer is smaller")
        elif user_input < num:
            print("The answer is greater")

def show_highscore(level=None):
    if level:
        hs = high_scores.get(level)
        if hs:
            print(f'Highscore ({level.title()}) = {hs} attempts')
        else:
            print(f"No highscore yet for {level.title()}. Play a game first!")
    else:
        for lvl in high_scores:
            hs = high_scores[lvl]
            if hs:
                print(f'Highscore ({lvl.title()}) = {hs} attempts')
            else:
                print(f"No highscore yet for {lvl.title()}")

def menu():
    while True:
        print("Welcome!")
        print("Select:")
        print("1 to Play")
        print("2 to Check Highscore")
        print("3 to Quit")
        try:
            user_input = int(input())
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
            continue
        
        if user_input == 1:
            print("Select difficulty")
            print("1 for Easy")
            print("2 for Medium")
            print("3 for Difficult")
            try:
                user_input2 = int(input())
            except ValueError:
                print("Invalid difficulty. Try again.")
                continue
            num, level = difficulty(user_input2)
            if num:
                play(num, level)
        elif user_input == 2:
            show_highscore()
        elif user_input == 3:
            print("Thanks for Playing")
            break
        else:
            print("Invalid selection")

menu()