#This is the GUI for the chatbot

#importing libraries
import tkinter
from tkinter import *

#TODO: Import chatbot

# The window class is not standard, so create a Window
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.initialize()

    def initialize(self):
        #Set window default settings
        self.master.title('IMDBot') #Window title
        self.master.geometry('500x500') #default size when the application opens
        self.master.minsize(300, 250) #set minimum size of parent window
        self.master.configure(background = '#1B1B1B') #dark mode
        #TODO: Better dark mode

        #Create the Main Menu (horizontal top menu)
        mainMenu = Menu(self.master)
        self.master.config(menu=mainMenu)

        #Create the sub menu "File" and sub-options
        fileMenu = Menu(mainMenu)
        fileMenu.add_command(label='New Conversation')
        fileMenu.add_command(label="Exit", command=self.exitProgram)

        #Create the sub menu "Help Menu" and its sub-options
        helpMenu = Menu(mainMenu)
        helpMenu.add_command(label='View Help')
        helpMenu.add_command(label='About IMDBot')

        #Add sub menus to main menu
        mainMenu.add_cascade(label='File', menu=fileMenu)
        mainMenu.add_cascade(label='Help', menu=helpMenu)

        # Create the Text widget for the conversation history
        outputBox = Text(self.master,
                            state = 'disabled', # Must change the state to normal before adding text and back to disabled after adding text
                            bg = '#555555',
                            height = 10,
                            wrap = NONE,
                            relief = FLAT,
                            fg = 'white',
                            font = ("Trebuchet 12"))
        outputBox.pack(side = TOP, fill='both', expand = True, padx = 5, pady = 5)        

        # Create the scrollbar for the outputBox
        scrollbar = Scrollbar(outputBox, orient = VERTICAL) # create the scrollbar
        scrollbar.pack(side = RIGHT, fill = Y) # put it on the right side filling vertically 
        outputBox['yscrollcommand'] = scrollbar.set # pack it inside the outputBox

        # TODO: TESTING ONLY. DELETE LATER
        outputBox['state'] = 'normal'
        for i in range(40):
            outputBox.insert('1.0', "text for testing the scrollbar\n")
        outputBox['state'] = 'disabled'

        # Create the text widget for user input
        inputBox = Text(self.master,
                            state = 'normal', # normal state means user can write in it
                            bg = '#999999',
                            height = 2,
                            width = 10,
                            yscrollcommand = 'TRUE',
                            fg = 'black',
                            font = ("Trebuchet 12"))
        inputBox.pack(side = LEFT, fill = 'both', expand = True, padx = 5, pady = 5)

        # Create the send button
        send_button = Button(self.master,
                                text = 'Send',
                                command=self.get_response,
                                #TODO: need event listener
                                width = 10,
                                height = 2,
                                bg = '#555555',
                                activebackground = '#3B3B3B',
                                fg = 'white')
        send_button.pack(side = RIGHT, padx = 5, pady = 5, expand=0)

    def create_event_listener(self):
        user = 0;    
    # Command for the send button - send info to the chatbot, receive info from chatbot, print all.
    def get_response(self):
        user_input = self.master.inputBox.get() # Get the input String and save as variable
        self.inputBox.delete(0, END) # Delete the input String in the inputBox

        response = "some reply here" # TODO: FOR TESTING ONLY DELETE LATER. Should be something like self.chatbot.get_response(user_input)

        self.outputBox['state'] = 'normal' #Change state of outputbox to normal so it can be edited
        self.outputBox.insert(END, "Human: " + user_input + "\n" + "IMDBot: " + str(response.text) + "\n") #TODO: need username, user_input, and response text
        self.outputBox['state'] = 'disabled' #Change state of outputbox to disabled so user can't edit text

    # Command for Menu File > Exit
    def exitProgram(self):
        exit()


def run_app():
    # initialize tkinter and create a window with a menu
    root = Tk()
    app = Window(root)

    # Show the window
    app.mainloop()


# Run the program
run_app()