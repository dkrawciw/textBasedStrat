from tkinter import Frame, Tk, Button, Entry, StringVar
from PreviousEntriesFrame import PreviousEntriesFrame

class CreateProjectGui(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('1600x900')
        self.title('Guest List - CSCI 101')

        # Print all of the previous users to the screen
        entryFrame = PreviousEntriesFrame(self, SERVER_ADDRESS)
        entryFrame.loadEntries()

        # Display the input to write your own name in
        nameInp = StringVar()

        nameEntryFrame = Frame(self)
        nameEntry = Entry(nameEntryFrame, textvariable=nameInp)
        nameEntry.pack(ipadx=20,ipady=20, fill='both', expand=True)

        # Handling the button and the button press
        def userPushedButton():
            entryFrame.pushEntry(nameInp.get())

        btn = Button(nameEntryFrame, text="Sign the List!", command=userPushedButton)
        btn.pack(ipadx=10,ipady=10, expand=True, fill='both')

        nameEntryFrame.pack(padx=10,pady=10,fill='both')



# Initial setup
SERVER_ADDRESS = "http://18.234.50.107"

if __name__ == "__main__":
    app = CreateProjectGui()
    app.mainloop()