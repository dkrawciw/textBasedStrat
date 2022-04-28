from tkinter import Frame, Label, E, W
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
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=8)

        cnt = 0
        for entry in range(len(entryList) - 1, -1, -1):
            if cnt == 5:
                break
            cnt += 1

            name = Label(self, text=entryList[entry][0])
            name.grid(column=0, row=entry, sticky=W, padx=5, pady=5)

            date = Label(self, text=entryList[entry][1])
            date.grid(column=1, row=entry, sticky=E, padx=5, pady=5)
        
        self.pack()
    
    def pushEntry(self, name):
        if len(name) == 0:
            return
        Create101InternetAccess.addToListOfEntries(self.hostname, name)
        self.loadEntries()