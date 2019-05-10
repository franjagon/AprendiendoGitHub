import click

textColors = {'black': '30', 'red': '31', 'green': '32', 'yellow': '33', 'blue': '34', 'magenta': '35', 'cyan': '36', 'white': '37', 'reset': '39'}
backGround = {'black': '40', 'red': '41', 'green': '42', 'yellow': '43', 'blue': '44', 'magenta': '45', 'cyan': '46', 'white': '47', 'reset': '49'}
styles = {'bold': 1, 'underline': 4, 'blink': 5, 'reversed': 7}

def clear():
    print("\033[2J")

def locate(line, column):
    print("\033[{};{}H".format(line, column))

def clearLine(line = None, column = None):
    if line != None and column != None:
        locate(line, column)
    elif line != None:
        locate(line, 1)
        
    print("\033[K", end = "")

def processParams(params):
    if 'line' in params:
        line = params['line']
        column = 1
        
        if 'column' in params:
            column = params['column']
        
        locate(line, column)
        
    if 'color' in params and params['color'] in textColors:
        print("\033[{}m",format(colors[params['color']]), end = "")
        
    if 'back' in params and params['back'] in backGround:
        print("\033[{}m",format(backGround[params['back']]), end = "")
        
    if 'style' in params and params['style'] in styles:
        print("\033[{}m",format(styles[params['style']]), end = "")
    
def Print(cadena, **params):
    processParams(params)
    
    if 'newline' in params and params['newline']:
        print(cadena)
    else:
        print(cadena, end = "")
    
    if 'noreset' not in params:
        Reset()
    
def Input(msg, **params):
    processParams(params)
    
    if 'dirty' not in params:
        clearLine()
    
    return input(msg)
        
def Format(style, colorText, colorBack):
    print("\033[{};{};{}m".format(style, colorText, colorBack), end = "")

def Reset():
    print("\033[=3l", end = "")
#    Format(0, 37, 40)
    
