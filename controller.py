# This file contains controller class

from functools import partial

class CalcController:
    """Calculator controller class"""

    def __init__(self,view, model):
        """Initializer"""
        self._view = view
        self._evaluate = model
        self._connectSignals()  # For connecting signals and slots

    def _buildExpression(self,sub_exp):
        """To handle creation of math expressions"""
        expression = self._view.getDisplayText() + sub_exp
        self._view.setDisplayText(expression)

    def _calculateResult(self):
        """Evaluating results"""
        result = self._evaluate(expression = self._view.getDisplayText())
        self._view.setDisplayText(result)
    
    def _connectSignals(self):
        """For connecting signals and slots"""
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=','C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))
                # or 
                # expr = lambda : self._buildExperession(btnText)
                # btn.clicked.connect(expr)
    
        self._view.buttons['='].clicked.connect(self._calculateResult) # '='
        self._view.display.returnPressed.connect(self._calculateResult) # Enter
        
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay) # 'C'

    