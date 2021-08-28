from tkinter import *

class toDoList(Frame):

    toDoArr = []

    def __init__(self, master = None):
        super().__init__(master, width = 500, height = 200)
        self.master = master
        self.pack()
        self.createWidgets()
        

    def createWidgets(self):
        
        self.title = Label(self, text = 'To Do List')
        self.label1 = Label(self, text = 'Enter your to do')
        self.toDoTextBox = Entry(self)
        self.submitToDo = Button(self, text = 'Submit', command = self.addItem)

        self.title.place(relx = .4, y = 5, width = 100, height = 20)
        self.label1.place(relx = .2, y = 25, width = 100, height = 20)
        self.toDoTextBox.place(relx = .2, y = 45, width = 100, height = 20)
        self.submitToDo.place(relx = .2, y = 85, width = 100, height = 20)
    
    def addItem(self, toDoArr = toDoArr):

        text = self.toDoTextBox.get()
        toDoArr.append(f'- {text}')
        print(toDoArr)
        self.showToDo = Label(self, text = '\n'.join(self.toDoArr), anchor = 'nw', justify = 'left')
        self.showToDo.place(relx = .5, y = 25, width = 200, relheight = 1)
        self.toDoTextBox.delete(0, 'end')




    def eraseItem(self):
        pass

    

root = Tk()
root.wm_title('To Do List')

app = toDoList(root)
app.mainloop()