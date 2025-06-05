class Pessoa:
    def __init__(self,nome,ano):
        self._nome = nome
        self._ano = ano
        
    @property
    def nome(self):
     return self._nome
 
    @property
    def idade(self):
     _ano_atual = 2025
     return _ano_atual - self._ano
 
 
 
pessoa = Pessoa("Mauro", 2000)
print(f"Nome:{pessoa.nome} \t Idade:{pessoa.idade}")
        
        
        