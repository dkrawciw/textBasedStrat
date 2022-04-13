from tkinter import Frame, Label
from create101Internet import Create101InternetAccess

class PreviousEntriesFrame(Frame):
    def __init__(self, container, hostname):
        Frame.__init__(self, container)
        self.hostname = hostname
        self.loadEntries()
    
    def loadEntries(self):
        for childWidget in self.winfo_children():
            childWidget.destroy()

        entryList = Create101InternetAccess.getListOfEntries(self.hostname)
        for entry in entryList:
            label = Label(self, text=entry[0] + " : " + entry[1])
            label.pack(ipadx=10, ipady=10)
        
        self.pack()
    
    def pushEntry(self, name):
        if len(name) == 0:
            return
        Create101InternetAccess.addToListOfEntries(self.hostname, name)
        self.loadEntries()