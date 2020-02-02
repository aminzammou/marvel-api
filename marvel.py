import time
import hashlib
import requests
import json
import random


def rasuper():
    """Returned een random naam van een superheld"""
    # print('in loop')
    return randomhero['name']


def rasid():
    """Returned een random id van een superheld"""
    # print('in loop 2')
    return randomhero['id']


def rasdes():
    """Returned een random description van een superheld"""
    naam = rasuper()
    url = "http://gateway.marvel.com:80/v1/public/characters"
    connection_url = url + "?ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest + "&name=" + naam
    print(connection_url)

    response = requests.get(connection_url)
    jsontext = json.loads(response.text)

    payloadObject = jsontext['data']
    supperlist = payloadObject['results']

    for supper in supperlist:
        hint = supper['description'].replace(supper['name'], '***').split(',')
        return hint


def racomic():
    """Returned een random comic title van een superheld"""
    url = "http://gateway.marvel.com:80/v1/public/characters/" + extra + "/comics"
    connection_url = url + "?ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest + "&characterId=" + extra

    response = requests.get(connection_url)
    jsontext = json.loads(response.text)
    payloadObject = jsontext['data']
    supperlist = payloadObject['results']
    for supper in supperlist:
        hint = supper['title']
        return hint


def raevent():
    """Returned een random event title van een superheld"""
    url = "http://gateway.marvel.com:80/v1/public/characters/" + extra + "/events"
    connection_url = url + "?ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest + "&characterId=" + extra

    response = requests.get(connection_url)
    jsontext = json.loads(response.text)
    payloadObject = jsontext['data']
    supperlist = payloadObject['results']
    for supper in supperlist:
        hint = supper['title']
        return hint


def raserie():
    """Returned een random series title van een superheld"""
    url = "http://gateway.marvel.com:80/v1/public/characters/" + extra + "/series"
    connection_url = url + "?ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest + "&characterId=" + extra

    response = requests.get(connection_url)
    jsontext = json.loads(response.text)
    payloadObject = jsontext['data']
    supperlist = payloadObject['results']
    for supper in supperlist:
        hint = supper['title']
        return hint


def fetchCharacters():
    """Returned een lijste van superhelden"""
    url = "http://gateway.marvel.com:80/v1/public/characters"
    connection_url = url + "?ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest

    response = requests.get(connection_url)
    jsontext = json.loads(response.text)
    payloadObject = jsontext['data']
    supperlist = payloadObject['results']
    return supperlist


def newHero():
    """Functie die word opgehaald wanneer er nieuwe gegevens nodig zijn"""
    global randomhero, extra
    randomhero = random.choice(supperlist)
    extra = str(rasid())


# nodige gegevens om te gebruiken zo als de key's en de tijd, ook het hashen van de key's
timestamp = str(time.time())
private_key = "41761bda4b150292c98ea417f555a61b9e1c0eb7"
public_key = "7ebffc98e9ccc7da9e11e78b725f4365"
hash = hashlib.md5((timestamp + private_key + public_key).encode('utf-8'))
md5digest = str(hash.hexdigest())

supperlist = fetchCharacters()
randomhero = random.choice(supperlist)
extra = str(rasid())
