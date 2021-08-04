import requests as r 
from bs4 import BeautifulSoup

def pedir_nome():
    while True:
        nome = input("Digite o nome da pessoa: ")
        nome = nome.title()
        nome = nome.split()
        if len(nome) == 2:
            nome = nome[0] + "_" + nome[1]
            return nome
        else:
            print("Digite o nome com apenas um espaço separando-os.")
            continue

    
def fazer_requisicao():
        url = "https://pt.wikipedia.org/wiki/" + pedir_nome()
        resposta = r.get(url).text
        soup = BeautifulSoup(resposta, 'html.parser')
        print(soup.find("p").text)


fazer_requisicao()


