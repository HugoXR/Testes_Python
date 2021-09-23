from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import csv

try:
    html = urlopen("https://en.wikipedia.org/wiki/1980s_in_film")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(), "html5lib")

    tabela = res.find("table",{"class": "wikitable sortable"})
    linhas = tabela.tbody.findAll("tr")

    ano = [coluna.getText().strip() for linha in linhas if linha == linha 
    for coluna in linha.findAll("td") if coluna.getText().startswith("1") and len(coluna.getText()) == 5]
    
    filmes = [link.getText() for linha in linhas if linha == linha 
    for coluna in linha.findAll("td") if coluna == coluna 
    for elemento in coluna.findAll("i") if elemento == elemento 
    for link in elemento.findAll("a")]


path = "filmes.csv"
file = open(path, 'w')
writer = csv.writer(file)
for filme in filmes:
    writer.writerow([filme])

path = "filmesComAno.csv"
file = open(path, 'w')
writer = csv.writer(file)
for i in range(len(filmes)):
    writer.writerow([filmes[i], ano[i]])


