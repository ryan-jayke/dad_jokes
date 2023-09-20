from pyfiglet import figlet_format
import requests
from random import randint
from colorama import init
import termcolor

init()
url = "https://icanhazdadjoke.com/search"
flag = 1

title = 'Dad Joke 3000'
ascii_title = termcolor.colored(figlet_format(title), color='green')
print(ascii_title)
print("Let me tell you a joke!")

while flag == 1:
    term = input("\nGive me a topic: ")
    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": term}
    )

    data = response.json()
    count_jokes = len(data['results'])

    if count_jokes >= 1:
        select_joke = randint(0, count_jokes-1)
        joke = data['results'][select_joke]['joke']
        print(f"I've got {count_jokes} jokes about {term}. Here's one:\n")
        print(joke)
    elif count_jokes == 1:
        joke = data['results'][0]['joke']
        print(f"I've got 1 joke about {term}. Here it is:\n")
        print(joke)
    else:
        print(f"Sorry, I don't have any jokes about {term}. Please try again.")

    cont = ''
    while cont not in ('y','n'):
        cont = input("\nDo you want another joke? (y/n) ").lower()
        if cont == 'y':
            pass
        elif cont == 'n':
            flag = 0
            print("Goodbye!")
        else:
            print("Please enter 'y' or 'n'.")