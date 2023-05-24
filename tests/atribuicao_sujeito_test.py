from atribuicoes import atribuicao_de_sujeito

def test_atribuicao_sujeito():
    assert atribuicao_de_sujeito(frase="ligar o drone") == ["drone", "ligar o"]

def test_atribuicao_sujeito_2():
    assert atribuicao_de_sujeito(frase="Grande sábio, ligue o drone.") == ["drone", "grande sabio ligue o"]

def test_atribuicao_sujeito_3():
    assert atribuicao_de_sujeito(frase="Grande sábio, desligue a Geladeira.") == ["geladeira", "grande sabio desligue a"]

def test_atribuicao_sujeito_4():
    assert atribuicao_de_sujeito(frase="") == [None, ""]

def test_atribuicao_sujeito_5():
    assert atribuicao_de_sujeito(frase="Acesse o site da contabilidade e me diga as novidades") == ["contabilidade", "acesse o site da e me diga as novidades"]

def test_frase_sem_sujeito():
    assert atribuicao_de_sujeito(frase="Gostaria de um pastel") == [None, "gostaria de um pastel"]

def test_frase_vazia():
    assert atribuicao_de_sujeito(frase="") == [None, ""]
    