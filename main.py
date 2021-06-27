import sys

# for view
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

# completing the view
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QVBoxLayout

# importing controller
from controller import CalcController

__version__ = '0.1'
__author__ = 'Apurv Kulkarni'
__reference__ = __credits__ = 'Leodanis Pozo Ramos'

# -------------------
# Creating skeleton
# -------------------

class CalcUI(QMainWindow):
    """Calculator's main window"""

    def __init__(self):
        """Class Initializer"""
        super().__init__()                  # Initialization from super class
        
        # Setting window properties
        self.setWindowTitle("MyCalc")   # Setting window title
        self.setFixedSize(250,250)          # Set size 
        # Note to self: think abut shifting these settings to a settings class later

        # Set the general layout and central widget
        self.generalLayout = QVBoxLayout()     # 1st row- Display, 2nd row- buttons
        self._centralWidget = QWidget(self) # Creating a QWidget object
        
        self._centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(self._centralWidget)
             
        # Private functions for creating display and buttons
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        """Creates the display"""

        # Create the display widget
        self.display = QLineEdit()

        # Setting display properties
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        # Add the display to the general layout
        self.generalLayout.addWidget(self.display)
    
    def _createButtons(self):
        """Create buttons"""

        self.buttons = {}
        buttonsLayout = QGridLayout()

        # Creating button dictionary
        buttons = {
            # Numbers
            '7':(0,0),'8':(0,1),'9':(0,2),
            '4':(1,0),'5':(1,1),'6':(1,2),
            '1':(2,0),'2':(2,1),'3':(2,2),
            '0':(3,0),'00':(3,1),
            
            # Operations and other
            '+':(0,3),
            '-':(1,3),
            '*':(2,3),
            '/':(3,3),
            '.':(3,2),
            '=':(3,3),
            'C':(0,4) # Clear screen
        }

        # Adding buttons to the grid layout
        for btn,pos in buttons.items():
            # Creating dicionary of buttons
            self.buttons[btn] = QPushButton(btn)
            self.buttons[btn].setFixedSize(40,40) # setting size

            # Adding buttons to butotns layout
            buttonsLayout.addWidget(self.buttons[btn],pos[0],pos[1])

        # Add buttons layout to the genral (main) layout
        self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        """Printing the text to display"""
        self.display.setText(text)
        self.display.setFocus()
        print(help(self.display.setFocus()))

    def getDisplayText(self):
        """To get the display text"""
        return self.display.text()

    def clearDisplay(self):
        """To clear the screen"""
        self.setDisplayText('')

# Client code
def main():
    """Main function"""

    # Creating instance of QApplications
    mycalc = QApplication(sys.argv)

    # Showing GUI
    myView = CalcUI()
    myView.show()

    # Executing controller
    CalcController(view=myView)

    # Execute the main loop
    sys.exit(mycalc.exec_())

if __name__ == "__main__":
    main()



