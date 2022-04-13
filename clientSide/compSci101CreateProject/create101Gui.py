from tkinter import Frame, Tk, Button, Entry, StringVar
import PreviousEntriesFrame

# Initial setup
SERVER_ADDRESS = "http://18.234.50.107"

root = Tk()
root.geometry('800x800')
root.title('Guest List - CSCI 101')

# Print all of the previous users to the screen
entryFrame = PreviousEntriesFrame(root, SERVER_ADDRESS)
entryFrame.loadEntries()

# Display the input to write your own name in
nameInp = StringVar()

nameEntryFrame = Frame(root)
nameEntry = Entry(nameEntryFrame, textvariable=nameInp)
nameEntry.pack(fill='x', expand=True)
nameEntry.focus()

# Handling the button and the button press
def userPushedButton():
    entryFrame.pushEntry(nameInp.get())

btn = Button(nameEntryFrame, text="Sign the List!", command=userPushedButton)
btn.pack()

nameEntryFrame.pack()

root.mainloop()