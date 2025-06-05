from abc import ABC, abstractmethod

class ControleRemoto():
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod    
    def desligar (self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
     pass
        

class ControleTV(ControleRemoto):
    def ligar(self):
     print("Ligando a TV...")
     print("TV Ligada!")
     
    def desligar(self):
         print("Desligando a TV...")
         print("Desligado!")
    
    @property     
    def marca(self):
        return "LG"     


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
     print("Ligando o ar...")
     print("AR Ligado!")
     
    def desligar(self):
         print("Desligando o AR...")
         print("Desligado!")
    
    @property     
    def marca(self):
        return "Philco"     
     
          
        

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()

print(controle.marca)
