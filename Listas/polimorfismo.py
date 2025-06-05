class Passaro:
    def voar(self):
        print("Voando...")
        

class Pardal(Passaro):
    def voar (self):
        print("Pardal voando...")
    
      
class Avestruz(Passaro):
    def voar(self):
       print("Avestruz não voa")



#FIXME: não usa esse trem não que é feio 
class Aviao(Passaro):
    def voar(self):
        print("Zumbido do Avião")


            
def plano_voo(obj):
    obj.voar()
    

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())  

            
                    