import tkinter as tk

# contains calculator window and all its related functions
class Calculator:
    
    def __init__(self):
        self.window = tk.Tk()
        self.initializeWindow()
        self.expressionBox = None
        self.initializeButtons()
    
    # sets window to default settings
    def initializeWindow(self):
        self.window.title('Calculator')

        # changes icon if icon file is present
        try:
            icon = tk.PhotoImage(file='icon.png')
            self.window.wm_iconphoto(False, icon)
        except Exception as _:
            pass

    # creates all buttons
    def initializeButtons(self):
        # holds all buttons
        buttonsDict = {}

        # button dimensions
        buttonWidth = 6
        buttonHeight = 2
        buttonFont = 'Calibri 16'

        # creates display box at top of screen
        self.expressionBox = tk.Entry(self.window, insertontime=0, width=24, font='Calibri 20') # TODO does font change?
        self.expressionBox.grid(row=0, columnspan=5, ipady=15)

        # creates buttons 0 - 9
        for i in range(10):
            buttonsDict[i] = tk.Button(self.window, text=str(i), command=lambda i=i: self.updateExpression(str(i)), font=buttonFont, width=buttonWidth, height=buttonHeight)
            if i < 5:
                buttonsDict[i].grid(row=1, column=i)
            else:
                buttonsDict[i].grid(row=2, column=i-5)
        
        # create operator buttons * / + - =
        operators = ['*', '/', '+', '-', '=']
        for i, operator in enumerate(operators):
            buttonsDict[operator] = tk.Button(self.window, text=operator, command=lambda i=operators[i]: self.updateExpression(i), bg='#7986CB', font=buttonFont, width=buttonWidth, height=buttonHeight)
            buttonsDict[operator].grid(row=3, column=i)
        buttonsDict['='].config(bg='#81C784', command=lambda: self.evaluateExpression())

        # create clear button
        buttonsDict['clear'] = tk.Button(self.window, text='clear', command=lambda: self.clearExpression(), bg='#FF8A80', font=buttonFont, width=25, height=buttonHeight)
        buttonsDict['clear'].grid(row=4, columnspan=5)

    # updates displayed expression text
    def updateExpression(self, text):
        oldText = self.expressionBox.get()
        self.expressionBox.delete(0, tk.END)
        if oldText == 'Error':
            self.expressionBox.insert(0, text)
        else:
            self.expressionBox.insert(0, oldText + text)
    
    # clears displayed expression text
    def clearExpression(self):
        self.expressionBox.delete(0, tk.END)

    # evaluates the displayed expression text and displays result
    def evaluateExpression(self):
        try:
            result = eval(self.expressionBox.get())
            self.expressionBox.delete(0, tk.END)
            self.expressionBox.insert(0, str(result))
        except Exception as _:
            self.expressionBox.delete(0, tk.END)
            self.expressionBox.insert(0, "Error")