from tkinter import *

# Command for Menu File > Exit
def exitProgram():
    exit()

# ButtonClick listener
def buttonClick():
    text = inputBox.get("1.0", "end-1c") # Take the inputBox text from 1st word, 0th character, to the end without the new line
    print(text)
    
    # Write to the outputBox, don't forget to disabled it after
    outputBox["state"] = "normal"
    outputBox.insert("end-1c", text + "\n") # insert to the very last and create \n. so that next message will pop at the very end and automatically adds a new line
    outputBox["state"] = "disabled" 

    # Clear the input box
    inputBox.delete("1.0", "end-1c")

# Initialization
root = Tk()
root.title("IMDBot")
root.geometry("500x500")

# Menu Bar
mainMenu = Menu(root)

# Sub Menu for "File"
fileMenu = Menu(mainMenu, tearoff=0, background="#555555", foreground="white", activebackground="black", activeforeground="white")
fileMenu.add_command(label="New Conversation")
fileMenu.add_command(label="Save")
fileMenu.add_command(label="Save As...")
fileMenu.add_command(label="Exit", command=exitProgram)

# Sub Menu For "Help"
helpMenu = Menu(mainMenu, tearoff=0, background="#555555", foreground="white", activebackground="black", activeforeground="white")
helpMenu.add_command(label="View Help")
helpMenu.add_command(label="About IMDBot")

# Main Menu
mainMenu.add_cascade(label="File", menu=fileMenu)
mainMenu.add_cascade(label="Help", menu=helpMenu)

# Add the menus to the program  
root.config(menu=mainMenu)

# Create the text area of conversation
outputBox = Text(root, state = "disabled", bg = "#555555",height = 10, fg = "white", font = ("Trebuchet 12"))
outputBox.pack(side = TOP, fill="both", expand = True, padx = 5, pady = 5)   

# Create the text widget for user input
inputBox = Text(root, state = "normal", bg = "#999999", height = 2, width = 10, fg = "black", font = ("Trebuchet 12"))
inputBox.pack(side = LEFT, fill = 'both', expand = True, padx = 5, pady = 5)

# Create the send button
send_button = Button(root,text = "Send",width = 10, height = 2,bg = "#555555", activebackground = "#3B3B3B",fg = "white", command=lambda: buttonClick())
send_button.pack(side = RIGHT, padx = 5, pady = 5, expand=0)

# Create the scroll bar
scrollbar = Scrollbar(outputBox, orient = VERTICAL) # create the scrollbar
scrollbar.pack(side = RIGHT, fill = Y) # put it on the right side filling vertically 
outputBox['yscrollcommand'] = scrollbar.set # pack it inside the outputBox

# Run
root.mainloop()