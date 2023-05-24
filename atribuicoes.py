import json
import os
import re
from unicodedata import normalize


def atribuicao_de_sujeito(frase: str) -> list:
        """
        Função que recebe uma frase e retorna o sujeito da frase.

        Essa função separa a frase recebida em várias palavras e verifica se
        alguma dessas palavras é um sujeito da lista de sujeitos.

        Args:
            frase (str): Frase a ser analisada.
    
        Returns:
            str: Sujeito da frase.
            str: Frase sem o sujeito.  

        """
        #lendo o arquivo sujeitos.json
        with open(os.path.join(os.path.dirname(__file__),'content/sujeitos.json')) as f:
            sujeitos = dict(json.load(f))
        lista_sujeitos = sujeitos.keys()


        #limpando a frase
        frase = frase.lower()
        n_frase = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', frase)
        n_frase = normalize('NFKD', n_frase).encode('ASCII', 'ignore').decode('ASCII')

        #verificando se a frase possui algum sujeito
        sujeito = None
        for palavra in n_frase.split():
            if palavra in lista_sujeitos:
                sujeito = palavra

        if not sujeito:
            return [None, n_frase]
    
        #retirando o sujeito da frase
        frase = n_frase.replace(sujeito, '').replace("  ", " ").strip()

        return [sujeito, frase.strip()]

def atribuicao_de_verbo(frase: str) -> list:
    """
    Função que recebe uma frase e retorna o verbo da frase.

    Essa função separa a frase recebida em várias palavras e verifica se
    alguma dessas palavras é um verbo da lista de verbos.

    Args:
        frase (str): Frase a ser analisada.

    Returns:
        str: Verbo da frase.
        str: Frase sem o verbo.  

    """
    #lendo o arquivo verbos.json
    with open(os.path.join(os.path.dirname(__file__),'content/verbos.json')) as f:
        verbos = dict(json.load(f))
    lista_verbos = verbos


    #limpando a frase
    frase = frase.lower()
    n_frase = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', frase)
    n_frase = normalize('NFKD', n_frase).encode('ASCII', 'ignore').decode('ASCII')

    #verificando se a frase possui algum verbo
    verbo = None
    for palavra in n_frase.split():
        if palavra in lista_verbos.keys():
            verbo = lista_verbos[palavra]
            sub_verbo = palavra

    if not verbo:
        return [None, n_frase]

    #retirando o verbo da frase
    frase = n_frase.replace(sub_verbo, '').replace("  ", " ").strip()

    return [verbo, frase.strip()]

