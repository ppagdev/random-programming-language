import requests
from bs4 import BeautifulSoup
import sys

try:
    # make a GET request to wikipedia page
    response = requests.get("https://en.wikipedia.org/wiki/List_of_programming_languages")
except:
    sys.exit("wikipedia is dead?")

# parse the html
soup = BeautifulSoup(response.content, 'html.parser')

# find all links in the page
links = soup.find(id="bodyContent").find_all("a")

# get relevant info
with open('languages.txt', 'w') as f:
    write = False
    for link in links:
        # find wikipedia links
        if 'href' in link.attrs and "/wiki/" in link['href']:
            # found first language, start writing to file
            if 'A.NET' in link.text:
                write = True
            if write:
                f.write(link.text + "\n")
            # found last language, stop writing to file
            if 'Zig' in link.text:
                break
print("Done!")
