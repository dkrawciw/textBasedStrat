import requests

while True:
    currGuestList = requests.get("http://127.0.0.1:8080/guestList.txt").text
    print("Here is my current guest:")

    currGuestList = currGuestList.split('\n')
    enumNames = 0
    for i in range(0, len(currGuestList) - 1, 2):
        enumNames += 1
        name = currGuestList[i]
        date = currGuestList[i + 1]
        print(str(enumNames) + ") " + name + " " + date)
    print("")


    ans = input("Input your name into the guest list (Enter 'Q' to quit): ")
    if ans.upper() == "Q":
        break

    r = requests.post("http://127.0.0.1:8080/addGuestList", data={"name": ans})