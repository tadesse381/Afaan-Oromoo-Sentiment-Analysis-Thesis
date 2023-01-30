import tkinter
from tkinter import*
def main():
    window= tkinter.Tk()
    # to rename the title of the window
    window.title("MSSAAP")
    # pack is used to show the object in the window

    def function():
        pass

    # creating a root menu to insert all the sub menus
    root_menu = tkinter.Menu(window)
    window.config(menu = root_menu)

    # creating sub menus in the root menu
    file_menu = tkinter.Menu(root_menu) # it intializes a new su menu in the root menu
    root_menu.add_cascade(label = "File", menu = file_menu) # it creates the name of the sub menu
    file_menu.add_command(label = "New file.....", command = function) # it adds a option to the sub menu 'command' parameter is used to do some action
    file_menu.add_command(label = "Open files", command = function)
    file_menu.add_separator() # it adds a line after the 'Open files' option
    file_menu.add_command(label = "Exit", command = window.quit)

    # creting another sub menu
    edit_menu = tkinter.Menu(root_menu)
    root_menu.add_cascade(label = "Edit", menu = edit_menu)
    edit_menu.add_command(label = "Undo", command = function)
    edit_menu.add_command(label = "Redo", command = function)
    black= Label(window, text = "Machine Learning Based", foreground="white", bg="black", height=2,justify=LEFT,font=('Verdana', 12, 'bold', 'italic'))
    black.pack(fill='x')
    red = Label(window,text = "Multi Scale Sentiment Analysis for",foreground="black", bg="red", height=2,font=('Verdana', 12, 'bold', 'italic'))
    red.pack(fill='x')
    white = Label(window,text = "Afaan Oromoo Posts",foreground="red",  bg="white", height=2,font=('Verdana', 12, 'bold', 'italic'))
    white.pack(fill='x')
    lbl = Label(text="Yaada Keessan Galchaa:",font=('Verdana', 12, 'bold', 'italic'))
    lbl.pack()
    lbl.place(x=0,y=200)
    def ClassificationAlgorithm():
        return (text.get("1.0",END))
    def clearText():
        text.delete('1.0', END)
        window = tkinter.Tk()
    text = Text(window, height=15, width=60)
    s = tkinter.Scrollbar(window)
    s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    s.config(command=text.yview)
    text.config(yscrollcommand=s.set)
    text.focus_set()
    text.pack()
    text.place(x=220,y=150)
    lbl1 = Label(text="Algoorizimii Filadhaa:",font=('Verdana', 12, 'bold', 'italic'))
    lbl1.pack()
    lbl1.place(x=0, y=425)
    txtresult = Text(window, height=5, width=30)
    txtresult.pack()
    txtresult.place(x=730,y=250)
    v0=IntVar()
    v0.set(0)
    r1=Radiobutton(window, text="Naive Bayes", variable=v0,value=2,font=('Verdana', 10))
    r2=Radiobutton(window, text="Support Vector Machine", variable=v0,value=3,font=('Verdana', 10))
    r3=Radiobutton(window, text="Maximum Entropy", variable=v0,value=4,font=('Verdana', 10))
    r1.pack()
    r1.place(x=220, y=425)
    r2.pack()
    r2.place(x=350, y=425)
    r3.pack()
    r3.place(x=560, y=425)
    lbg = Label(text="N-Grams:",font=('Verdana', 12, 'bold', 'italic'))
    lbg.pack()
    lbg.place(x=0, y=500)
    ch1 = IntVar()
    ch1.set(0)
    c1 = Checkbutton(window, text = "Unigram", variable = ch1,onvalue = 2,font=('Verdana', 10))
    c2 = Checkbutton(window, text = "Bigram", variable = ch1,onvalue = 3,font=('Verdana', 10))
    c3 = Checkbutton(window, text = "Trigram", variable = ch1,onvalue = 4,font=('Verdana', 10))
    c1.pack()
    c1.place(x=220, y=500)
    c2.pack()
    c2.place(x=350, y=500)
    c3.pack()
    c3.place(x=560, y=500)
    b1 = Button(window, text ="Qoqqodi",width=10, font=('Verdana', 10), command=ClassificationAlgorithm)
    b2 = Button(window, text ="Haqi",width=10,font=('Verdana', 10), command = clearText)
    b3 = Button(window, text ="Cufi",width=10,font=('Verdana', 10), command = window.destroy)
    b1.pack()
    b1.place(x=220, y=600)
    b2.pack()
    b2.place(x=400, y=600)
    b3.pack()
    b3.place(x=580, y=600)
    window.geometry('1000x1000')
    #window.mainloop()
    txti= ClassificationAlgorithm()
    return txti
main()
