import sys 
sys.path.append("..")
from src.model import pessoa

def test_concatenacao_nome_sobrenome():
    p1 = pessoa.Pessoa('Fernanda','Maia', 58, '88845990168')
    assert p1.nome_completo() == 'Fernanda Maia'