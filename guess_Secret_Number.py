import random

def playGame():

    global tries
    global playerGuess
    global guesses

    tries = 0
    playerGuess = 0
    guesses = []

    print("Welcome to Guess Secret Number game!")
    
    secretNum = random.randint(1, 100)
    
    # Game Loop and Rules

    while playerGuess != secretNum:
        playerGuess = int(input("Enter your guess here...."))

        if playerGuess > secretNum:
         guesses.append(playerGuess)
         tries +=1
         print("too high")

        elif playerGuess < secretNum:
            guesses.append(playerGuess)
            tries +=1
            print("too low")
        else:
            guesses.append(playerGuess)
            tries +=1
            print("Correct, you found it in " + str(tries) + " tries")
            print("Your tries is " + str(guesses) )


while True:
    playGame()
    # Menu
    print("(1) To play again (2) To save (3) To exit")
    menuChoice = int(input("Enter your choise..."))
    # Match
    match menuChoice:
       case 1:
          continue
       

       case 2:
          filename = input("Give your file a name...")
          
          with open(filename, "w") as file:
             file.write(str(guesses))


       case 3:
          break