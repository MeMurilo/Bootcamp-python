class Cachorro:
    def __init__(self,nome,cor, acordado = True):
     print ("Iniciando a classe...")
     self.nome = nome 
     self.cor = cor
     self.acordado = acordado
     
    def __del__(self):
        print("Removendo a a instancia da classe")
    
    def latir(self):
         print ("auau")
         
    def __str__(self):
     return f"{self.__class__.__name__}: {", ".join ([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"  
     
     

      
c = Cachorro("Zeus", "Branco e preto",False)
print(c) 
      
           
      
      




          
       
