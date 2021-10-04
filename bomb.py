import fbchat
from fbchat import *
from fbchat.models  import *
from pyfiglet import Figlet
import sys
from colorama import init
import time
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
import time

text="fb bombbbbbbbbbbbbbbbbbb"
cprint(figlet_format(text, font="digital"), "blue") 

print("Press CTRL+C to quit")
username = str(input("enter your username : "))
password = str(input("enter your password : "))

client = fbchat.Client(username,password)
name = str(input("enter your victim username : "))
friends = client.searchForUsers(name)
friend = friends[0]
message = str(input("enter your message : "))
x=0
y= int(input("enter the lenghtttttt of message in number : "))
while x <= y:
    sent = client.send(fbchat.models.Message(str(x)+".) "+message), friend.uid)
    time.sleep(3)
    if sent:
        print("Blast is running")
        time.sleep(3)
    x += 1
print("Blast stopped now go to hell idot motherfuckers ")
