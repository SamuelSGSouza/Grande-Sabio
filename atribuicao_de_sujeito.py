import json
import os
import re


#lendo o arquivo sujeitos.json
with open(os.path.join(os.path.dirname(__file__),'content/sujeitos.json')) as f:
    sujeitos = dict(json.load(f))
lista_sujeitos = sujeitos.keys()


def atribuicao_de_sujeito(frase: str,sujeito_anterior = "N/A") -> list:
        """
        Função que recebe uma frase e retorna o sujeito da frase.

        Essa função separa a frase recebida em várias palavras e verifica se
        alguma dessas palavras é um sujeito da lista de sujeitos.

        Args:
    
            frase (str): Frase a ser analisada.
    
        Returns:

            str: Sujeito da frase.
    
        """
        #limpando a frase
        frase = frase.lower()
        n_frase = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', frase)

        #verificando se a frase possui algum sujeito
        sujeito = None
        for palavra in n_frase.split():
            if palavra in lista_sujeitos:
                sujeito = palavra

        if not sujeito:
            return [sujeito_anterior, n_frase.replace(sujeito_anterior, '').strip()]
    
        #retirando o sujeito da frase
        frase = n_frase.replace(sujeito, '').replace("  ", " ")

        return [sujeito, frase.strip()]
