from atribuicao_de_sujeito import atribuicao_de_sujeito


def test_atribuicao_sujeito():
    assert atribuicao_de_sujeito(frase="ligar o drone") == ["drone", "ligar o"]

def test_atribuicao_sujeito_2():
    assert atribuicao_de_sujeito(frase="Grande sábio, ligue o drone.") == ["drone", "grande sábio ligue o"]

def test_atribuicao_sujeito_3():
    assert atribuicao_de_sujeito(frase="Grande sábio, desligue a Geladeira.") == ["geladeira", "grande sábio desligue a"]

def test_atribuicao_sujeito_4():
    assert atribuicao_de_sujeito(frase="") == ["N/A", ""]

def test_atribuicao_sujeito_5():
    assert atribuicao_de_sujeito(frase="Acesse o site da contabilidade e me diga as novidades") == ["contabilidade", "acesse o site da e me diga as novidades"]