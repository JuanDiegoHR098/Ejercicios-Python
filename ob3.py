class Persona:
    def __init__(self,nombre,cedula,genero) -> None:
        self.nombre= nombre
        self.cedula= cedula
        self.genero= genero

class Paciente(Persona):
    def __init__(self,nombre,cedula,genero) -> None:
        super().__init__(nombre,cedula,genero)
        self.servicio=""

class Enfermera(Persona):
    def __init__(self,nombre,cedula,genero,turno,rango) -> None:
        super().__init__(nombre,cedula,genero)
        self.turno = turno
        self.rango = rango




class Medico(Enfermera):
    def __init__(self, nombre, cedula, genero,turno,especialidad) -> None:
        Enfermera.__init__(self,nombre, cedula, genero,turno,None)
        self.especialidad = especialidad

    def hablar(self):
        return f"Mi nombre es {self.nombre} y mi especialidad es {self.especialidad}"


carlos= Medico(nombre="Carlos",cedula=1036,genero="F",turno="12-14",especialidad="Neurocirujano")

print(carlos.hablar())


