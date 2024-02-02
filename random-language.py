import time
import random

languages = []

print("SCANNING...")
with open('languages.txt', 'r') as file:
    for line in file:
        line = line.strip()
        languages.append(line)

waitingMessages = ["WAIT FOR IT", "ALMOST THERE", "OH MY GOD ITS HAPPENING", "HERE WE GO!!!", "WE'RE SO CLOSE", "WHAT WILL IT BE???", "SUCH MYSTERY"]

time.sleep(1)
for i in range(3,0,-1):
    print(random.choice(waitingMessages))
    time.sleep(1)

print("WOW!!! THE RANDOM LANGUAGE YOU GOT IS: " + random.choice(languages))
