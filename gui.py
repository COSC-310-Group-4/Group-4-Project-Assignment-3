from tkinter import *
import tkinter
import film as f
import person as p
import company as c
import user as u
import webbrowser

class IMDBotGUI():

    def __init__(self,master):
        self.master = master
        # Initialization
        master.title("IMDBot")
        master.geometry("500x500")
        master.minsize(300, 250) # minimum size so that the button and text boxes don't disappear or look odd

        # Menu Bar
        mainMenu = Menu(master)


        # Open Git's IMDBot Readme
        new = 1
        url = "https://github.com/COSC-310-Group-4/Group-4-Project-Assignment-3/blob/main/README.md"

        def openReadme():
            webbrowser.open(url,new=new)

        # Sub Menu for "File"
        self.fileMenu = Menu(mainMenu, tearoff=0, background="#555555", foreground="white", activebackground="black", activeforeground="white")
        self.fileMenu.add_command(label="New Conversation")
        self.fileMenu.add_command(label="Exit", command=self.exitProgram)

        # Sub Menu For "Help"
        self.helpMenu = Menu(mainMenu, tearoff=0, background="#555555", foreground="white", activebackground="black", activeforeground="white")
        self.helpMenu.add_command(label="About IMDBot", command=openReadme)

        # Main Menu
        mainMenu.add_cascade(label="File", menu=self.fileMenu)
        mainMenu.add_cascade(label="Help", menu=self.helpMenu)

        # Add the menus to the program  
        master.config(menu=mainMenu)

        # Create the text area of conversation
        self.outputBox = Text(master, state = "disabled", bg = "#555555",height = 10, fg = "white", font = ("Trebuchet 12"))
        self.outputBox.pack(side = TOP, fill="both", expand = True, padx = 5, pady = 5)   

        # Create the text widget for user input
        #self.inputBox = Text(master, state = "normal", bg = "#999999", height = 2, width = 10, fg = "black", font = ("Trebuchet 12"))
        self.input_var=StringVar()
        self.inputBox = Entry(master,textvariable = self.input_var, font=('calibre',10,'normal'))
        self.inputBox.pack(side = LEFT, fill = 'both', expand = True, padx = 5, pady = 5)

        # Create the send button
        self.send_button = Button(master,text = "Send",width = 10, height = 2,bg = "#555555", activebackground = "#3B3B3B",fg = "white", command=lambda: self.buttonClick())
        self.send_button.pack(side = RIGHT, padx = 5, pady = 5, expand=0)
        

        # Create the scroll bar
        self.scrollbar = Scrollbar(self.outputBox, orient = VERTICAL) # create the scrollbar
        self.scrollbar.pack(side = RIGHT, fill = Y) # put it on the right side filling vertically 
        self.outputBox['yscrollcommand'] = self.scrollbar.set # pack it inside the outputBox

        # will change after user click the button
        self.userInput=""


    # Command for Menu File > Exit
    def exitProgram(self):
        exit()

    # ButtonClick listener
    def buttonClick(self):
        self.userInput = self.inputBox.get() # Take the inputBox text from 1st word, 0th character, to the end without the new line
        # self.userInput = self.input_var.get()

        # Write to the outputBox, don't forget to disable it after
        self.outputBox["state"] = "normal"
        self.outputBox.insert("end-1c", self.userInput + "\n") # insert to the very last and create \n. so that next message will pop at the very end and automatically adds a new line
        self.outputBox["state"] = "disabled" 
        # Clear the input box
        self.inputBox.delete(0, tkinter.END)
        return self.userInput

    # helper function to add IMDBot's text to the GUI
    def addToOutputBox(self,text):
        # Write to the outputBox, don't forget to disable it after
        self.outputBox["state"] = "normal"
        self.outputBox.insert("end-1c", text + "\n") # insert to the very last and create \n. so that next message will pop at the very end and automatically adds a new line
        self.outputBox["state"] = "disabled" 

    def getUserInput(self):
        return self.userInput
    
root = Tk() 
imdbotgui = IMDBotGUI(root)
root.mainloop()