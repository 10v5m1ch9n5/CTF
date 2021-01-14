import requests
from bs4 import BeautifulSoup

url = "http://lamp4.ctf"

wordlist = open("/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt")
# wordlist = open("fake.txt")

lignes = wordlist.readlines()

for chemin in lignes:
    if chemin[0] == '#':
        continue
    chemin = chemin.strip()
    urltest = url+"/"+chemin
    rep = requests.get(url+"/"+chemin)
    if(rep.status_code != 404 and chemin != ""):
        print("/"+chemin+" (statut : "+str(rep.status_code)+")")
wordlist.close()
