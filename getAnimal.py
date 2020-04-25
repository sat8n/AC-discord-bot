from pprint import pprint
from bs4 import BeautifulSoup
import requests

def getSpecies(name):
    try:
        url = "https://nookipedia.com/wiki/" + name

        response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})

        soup = BeautifulSoup(response.content, "lxml")

        #for span in soup.select('td.roundybr'):
        for temp in soup.select('td#Infobox-villager-species'):
            try:
                animal_species = str(temp.text.split("\n",1)[0])
                return animal_species
            except AttributeError:
                break
    except IndexError:
        print('Invalid animal name.')

    return 0

def getType(name):
    try:
        url = "https://nookipedia.com/wiki/" + name

        response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})

        soup = BeautifulSoup(response.content, "lxml")

        #for span in soup.select('td.roundybr'):
        for temp in soup.select('td#Infobox-villager-personality'):
            try:
                animal_species = str(temp.text.split("\n",1)[0])
                return animal_species
            except AttributeError:
                break
    except IndexError:
        return '0'

    return 0

#print(getAnimal("Apollo"))
    
