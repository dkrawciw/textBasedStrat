from tkinter import Frame, Tk, Button, Entry, StringVar
from PreviousEntriesFrame import PreviousEntriesFrame

class CreateProjectGui(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x800')
        self.title('Guest List - CSCI 101')

        # Print all of the previous users to the screen
        entryFrame = PreviousEntriesFrame(self, SERVER_ADDRESS)
        entryFrame['relief'] = 'sunken'
        entryFrame.loadEntries()

        # Display the input to write your own name in
        nameInp = StringVar()

        nameEntryFrame = Frame(self)
        nameEntry = Entry(nameEntryFrame, textvariable=nameInp)
        nameEntry.pack(fill='x', expand=True)
        nameEntry.focus()

        # Handling the button and the button press
        def userPushedButton():
            entryFrame.pushEntry(nameInp.get())

        btn = Button(nameEntryFrame, text="Sign the List!", command=userPushedButton)
        btn.pack()

        nameEntryFrame.pack()



# Initial setup
SERVER_ADDRESS = "http://18.234.50.107"

if __name__ == "__main__":
    root = CreateProjectGui()
    root.mainloop()