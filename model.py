# Model of calculator for handling calculations

def evaluateExpression(expression):
    """Evaluates expression"""

    ERROR_MSG = 'ERROR'

    try:
        result = str(eval(expression,{},{}))
    except:
        result = ERROR_MSG

    return result