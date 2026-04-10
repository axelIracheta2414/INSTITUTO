class Persona:
    #edad, nombre,vivo,peso,altura
    def __init__(self,nombre:str,edad:int,altura:float,vivo= True):
        self.nombre:str = nombre.title()
        self.edad:int = edad
        self.altura:float = altura
        self.vivo:bool = vivo
    def presentarse(self):
        if self.vivo:
            print(f"Hola, soy {self.nombre} tengo {self.edad} años mido {self.altura} y al memento me encuentro {self.vivo}")
        else:
            print(f"QEPD{self.nombre}")