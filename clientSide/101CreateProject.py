import requests

x = requests.get("http://127.0.0.1:8080/guestList.txt")
print(f"Here is my current guest:\n{x.text}")


name = input("Input your name into the guest list: ")
r = requests.post("http://127.0.0.1:8080/addGuestList", data={"name": name})