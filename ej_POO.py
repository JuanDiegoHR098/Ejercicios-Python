class Persona:
    def __init__(self,nombre,cedula,genero,servicio) -> None:
        self.nombre= nombre
        self.cedula= cedula
        self.genero=genero
        self.servicio= servicio

class Sistema(Persona):
    def __init__(self, nombre, cedula, genero, servicio) -> None:
        super().__init__(nombre, cedula, genero, servicio)

    def hola():
        pass
        
