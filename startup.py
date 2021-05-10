import requests
from datetime import datetime
from bs4 import BeautifulSoup
from random import randint


# Colors
RESET = '\033[0m'
CITALIC = '\33[3m'
CYELLOW = '\33[33m'
CBLUE = '\33[34m'
CBEIGE = '\33[36m'
CGREEN2 = '\33[92m'


def print_color(text, color):
    print(color, text, RESET)


def print_time_date():
    now = datetime.now()
    date_string = "<< " + now.strftime("%A, %d %B %Y %H:%M:%S") + " >>"
    print_color(date_string, CYELLOW)


def print_quote_author():
    QUOTE = '"Ще се оправят работите. Злото не е трайно, доброто е господар на човешкото сърце."'
    AUTHOR = 'Елин Пелин'
    author_str = (len(QUOTE)-len(AUTHOR)-1) * ' ' + '-' + AUTHOR
    print_color(CITALIC+QUOTE, CBEIGE)
    print_color(author_str, CBLUE)


def print_random_fact():
    try:
        URL = 'https://bestlifeonline.com/random-fun-facts/'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
    except requests.exceptions.RequestException:
        print_color('Could not load website', CYELLOW)
        exit()
    fact_index = randint(0, 174)
    fact = soup.findAll('div', class_='title')[fact_index].text.strip()
    fact_string = "Random Fact: " + fact
    print_color(fact_string, CGREEN2)


if __name__ == "__main__":
    # Date and time
    print_time_date()
    print()
    # Random fact
    print_random_fact()
    # Quote
    print_quote_author()
