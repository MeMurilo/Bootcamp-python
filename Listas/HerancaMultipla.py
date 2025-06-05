class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
     
    def __str__(self):
     return f"{self.__class__.__name__}: {", ".join ([f"{chave}= {valor}" for chave, valor in self.__dict__.items()])}"            
    

 


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo 
        super().__init__(**kw)
        
    
        
     



class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
        
    


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass






class Onitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, **kw):
                      
        super().__init__(cor_pelo = cor_pelo,cor_bico=cor_bico, **kw)
        
        
    


gato = Gato(nro_patas=2, cor_pelo="Preto")
print(gato)

Perry = Onitorrinco(nro_patas=2, cor_pelo="Vermelho", cor_bico="Laranja")
print(Perry)
