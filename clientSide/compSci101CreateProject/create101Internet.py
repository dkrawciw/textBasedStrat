import requests

class Create101InternetAccess:
    @staticmethod
    def getListOfEntries(serverAddress):
        splitListOfEntries = requests.get(serverAddress + "/getGuestList").text.split('\n')
        entryList = []

        for line in range(0, len(splitListOfEntries) - 1, 2):
            entryList.append( [splitListOfEntries[line], splitListOfEntries[line + 1]] )

        return entryList
    
    @staticmethod
    def addToListOfEntries(serverAddress, name):
        requests.post(serverAddress + "/addGuestList", data={"name": name})