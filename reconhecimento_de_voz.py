import speech_recognition as sr
import time
from atribuicao_de_sujeito import atribuicao_de_sujeito

# Função para reconhecer a voz
def reconhecer_voz():
    # Criando um objeto do tipo Recognizer
    r = sr.Recognizer()

    # Abrindo o microfone para captura
    with sr.Microphone() as source:
        print("Diga alguma coisa: ")
        # Captura o áudio
        audio = r.listen(source)

    # Usando o Google Speech Recognition
    try:
        # Passa o áudio para o reconhecedor de padrões do speech_recognition
        frase = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + frase)
        # Após alguns segundos, retorna a frase falada
        
        return frase
    # Caso não tenha reconhecido o padrão de fala, exibe esta mensagem
    except sr.UnknownValueError:
        pass
    return None

def verifica_comando_inicial(frase: str):
    if not frase:
        return False
    palavras = frase.lower().split()

    if "iniciar" in palavras[0]:
        return True
    else:
        return False

if __name__ == '__main__':
    sujeito_anterior = "N/A"
    while True:
        frase = reconhecer_voz()
        if not verifica_comando_inicial(sujeito_anterior, frase):  
            time.sleep(1)
            continue
        
        sujeito, frase = atribuicao_de_sujeito(frase)


        if sujeito == "N/A":
            print("Não entendi o que você disse")
            continue
        
        print(f"Sujeito: {sujeito}")