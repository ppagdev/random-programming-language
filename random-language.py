import random

languages = []

with open('languages.txt', 'r') as file:
    for line in file:
        line = line.strip()
        languages.append(line)

print("WOW!!! THE RANDOM LANGUAGE YOU GOT IS: " + random.choice(languages))
