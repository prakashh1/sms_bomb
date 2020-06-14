import fbchat
from fbchat import *
from fbchat.models  import *

username = str(input("enter your username : "))
password = str(input("enter your password : "))

client = fbchat.Client(username,password)
name = str(input("enter your victim username : "))
friends = client.searchForUsers(name)
friend = friends[0]
message = str(input("enter your message : "))
x=0
y= int(input("enter the lenght of message in number : "))
while x <= y:
    sent = client.send(fbchat.models.Message(message), friend.uid)
    if sent:
        print("Blast is running")
    x += 1
print("Blast stopped")
