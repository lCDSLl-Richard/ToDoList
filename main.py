from tkinter import *

class toDoList(Frame):

    toDoDict = {0: None}

    def __init__(self, master = None):
        super().__init__(master, width = 500, height = 200)
        self.master = master
        self.pack(fill = BOTH)
        self.createWidgets()
        

    def createWidgets(self):
        
        self.title = Label(self, text = 'To Do List')
        self.label1 = Label(self, text = 'Enter your to do')
        self.toDoTextBox = Entry(self)
        self.submitToDo = Button(self, text = 'Submit', command = self.addItem)
        self.eraseToDo = Button()

        self.title.place(relx = .4, y = 5, width = 100, height = 20)
        self.label1.place(relx = .2, y = 25, width = 100, height = 20)
        self.toDoTextBox.place(relx = .2, y = 45, width = 100, height = 20)
        self.submitToDo.place(relx = .2, y = 85, width = 100, height = 20)
    
    def addItem(self, toDoDict = toDoDict):
        
        text = self.toDoTextBox.get()
        errorMessage = Label(self, text = '', fg = 'red')
        errorMessage.place(relx = .2, y = 110, width = 100, height = 20)

        if len(text) > 0:
            errorMessage.config(text = '')
            toDoKeys = list(toDoDict.keys())
            toDoDict[toDoKeys[-1]+1] = text
            toDoKeys = list(toDoDict.keys())
            print(toDoDict)
            toDoArr = []
            for i in toDoKeys:
                toDoArr.append(f'{i}.- {toDoDict[i]}')
            toDoArr.pop(0)
            self.showToDo = Label(self, text = '\n'.join(toDoArr), anchor = 'nw', justify = 'left')
            self.showToDo.place(relx = .5, y = 25, width = 200, relheight = 1)
            self.toDoTextBox.delete(0, 'end')

        else:
            errorMessage.config(text = 'Input something')

    def eraseItem(self):
        pass

    

root = Tk()
root.wm_title('To Do List')

app = toDoList(root)
app.mainloop()