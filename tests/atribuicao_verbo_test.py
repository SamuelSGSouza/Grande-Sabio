from atribuicoes import atribuicao_de_verbo

def test_atribuicao_verbo_esta_ativa():
    assert atribuicao_de_verbo(frase="ligar o") == ["ligar", "o"]

def test_atribuicao_verbo_1():
    assert atribuicao_de_verbo(frase="grande sabio ligue o") == ["ligar", "grande sabio o"]

def test_atribuicao_verbo_2():
    assert atribuicao_de_verbo(frase="grande sabio desligue a") == ["desligar", "grande sabio a"]

def test_atribuicao_verbo_frase_vazia():
    assert atribuicao_de_verbo(frase="") == [None, ""]

def test_atribuicao_verbo_frase_sem_verbo():
    assert atribuicao_de_verbo(frase="acenda o") == [None, "acenda o"]
