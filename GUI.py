from curses import BUTTON1_CLICKED
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

numbers = []

def generateNumbers():
    i = 0
    while i < 3:
        newNumber = random.randint(1, 100)
        numbers.append(newNumber)
        i += 1
        
def checkWinner(guess, winner):
    if guess == winner:
        print("You Won!")
        #Add points
    else:
        print("You lost!")
        #remove points
        #if 0 then don't
    
def pickWinner():
    winner = random.choice(numbers)
    return winner
    

def clearNumbers():
    numbers.clear()
    
def tryAgain():
    main()
    
def game():
    generateNumbers()
    guess = MyGUI.button_1_click()
    winner = pickWinner()
    checkWinner(guess, winner)


class MyGUI(QMainWindow):   
    points = 0
    
    
    def __init__(self): # initializes the object's attributes
        super(MyGUI, self).__init__() # super constructor
        uic.loadUi("GUI.ui", self) # loads the ui file
        self.show()
        
        # gui functionality
        
        self.button_1.clicked.connect(self.button_1_click)
    
    #functions
    
    
    
    def button_1_click():
        guess = numbers[0]
        
        return guess
            
    




def main():    
    app = QApplication([])
    window = MyGUI()
    
    app.exec_()

if __name__ == "__main__":
    main()