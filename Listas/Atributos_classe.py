class Estudante:
    escola = "Puc" #classe
    
    def __init__(self,nome,matricula): 
        self.nome = nome #instancia
        self.matricula = matricula
        
    def __str__(self):
        return f"{self.escola} {self.__class__.__name__}: {", ".join ([f"{chave}= {valor}" for chave, valor in self.__dict__.items()])}"  
    
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)    

aluno_1 = Estudante("Pedro", 231)
aluno_2 = Estudante("jessica", 900)

print(aluno_1)
print(aluno_2) 
   
print()

Estudante.escola = "UFMG"

aluno_1.matricula = 3
aluno_3 = Estudante("Carlos", 390)
mostrar_valores(aluno_1, aluno_2,aluno_3)
  