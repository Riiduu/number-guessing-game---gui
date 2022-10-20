import random

numbers = []
totalPoints = 0

def clearNumbers():
    numbers.clear()

def generateNumbers():
    i = 0
    while i < 3:
        number = random.randrange(0, 100)
        numbers.append(number)
        i += 1

def selectWinner():
    winner = random.choice(numbers)
    
    return winner

def tryAgain():
    tryAgain = input("Try again...?(yes/no): ")
    if tryAgain == "yes":
        main()
        
def updateScore():
    totalPoints += 1
    
    return totalPoints
        
def main():
    points = updateScore()
    
    print("Welcome to number guesssing game!")
    print(f"Current points: {points}")
    print("Guess the number!")
    #print 3 random numbers
    generateNumbers()
    for num in numbers:
        print(num)
        
    #input for the number
    guess = int(input("guess: "))
    winner = selectWinner()
    print(f"Winning number: {winner}")
    clearNumbers()
    
    if guess == winner:
        print("You won!")
        print("+1 points")
        print(f"total: {points}")
        tryAgain()
    else:
        print("You lost!")
        tryAgain()


main()

