import requests as r 
from bs4 import BeautifulSoup

def pedirNome():
    global nome
    nome = input("Digite o nome da pessoa: ")
    nome = nome.title()
    nome = nome.split()
    if len(nome) == 2:
        nome = nome[0] + "_" + nome[1]
        return True
    elif len(nome) < 2:
        print("Nome não suportado.Por favor digite o nome e sobrenome da pessoa.")
        return False
    else:
        print("Nome não suportado.Por favor digite apenas o nome e sobrenome da pessoa.")
        return False

    
def fazerRequisicao():
    url = "https://pt.wikipedia.org/wiki/" + nome
    resposta = r.get(url).text
    soup = BeautifulSoup(resposta, 'html.parser')
    print(soup.find("p").text)


if pedirNome():
    fazerRequisicao()
else:
    print("ERRO EM ALGUM LUGAR AI BIXO")

