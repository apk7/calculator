import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

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

        # Setting central widget
        self._centralWidget = QWidget(self)         # Creating a QWidget object
        self.setCentralWidget(self._centralWidget)
        

# Client code
def main():
    """Main function"""

    # Creating instance of QApplications
    mycalc = QApplication(sys.argv)

    # Showing GUI
    view = CalcUI()
    view.show()

    # Execute the main loop
    sys.exit(mycalc.exec_())

if __name__ == "__main__":
    main()



