class Bicicleta:
   def __init__(self,cor, modelo, ano, valor,aro):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
    self.aro = aro
    
   def buzinar(self):
       print("Plim plim plim")
       
   def parar (self):
     print ("Parando bicicleta...")
     print ("Bicicleta parada")          
   
   def correr(self):
      print("Vrummmmmmm")
      
   def __str__(self):
    return f"{self.__class__.__name__}: {", ".join ([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"
      
      
      
    
b1 = Bicicleta("vermelha", "caloi", 2002, 600, 16)
b1.buzinar()
b1.correr()
b1.parar()



b2 = Bicicleta("verde", "monark", 2000, 189,18)
print (b2)

   

