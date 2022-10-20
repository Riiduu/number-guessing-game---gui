from PyQt5.QtWidgets import *
from PyQt5 import uic
import random


class MyGUI(QMainWindow):   
        
    def __init__(self): # initializes the object's attributes
        super(MyGUI, self).__init__() # super constructor
        uic.loadUi("GUI.ui", self) # loads the ui file
        self.show()
        
        # gui functionality
        
        self.button_2.clicked.connect(self.show_message)
    
    #functions
    
    def show_message(self):
        print("tavmamm")


def checkWinner():
    print("checkWinner")
    
def pickWinner():
    print("pickWinner")

def clearNumbers():
    print("clearNumbers")

def generateNumbers(nums):
    newNumber = random.randint(1, 100)
    i = 0
    while i < 3:
        nums.append(newNumber)

def main():
    numbers = []
    
    app = QApplication([])
    window = MyGUI()
    
    nums = generateNumbers(numbers) # adds 3 random numbers to the numbers array
    print(nums)
    
    
    
    app.exec_()

if __name__ == "__main__":
    main()