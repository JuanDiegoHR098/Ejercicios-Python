# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# mostrar(): Muestra los datos de la persona.
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():
    def __init__(self,nombre,edad,dni) :
        self.nombre= nombre
        self.edad= edad
        self.dni= dni

    def nombre(self):
        return self.nombre
    
    def edad(self):
        if self.edad < 0:
            print("Edad Incorrecta")
        else:
            return self.edad
    
    def dni(self):
        if len(self.dni) < 5:
            print("DNI Invalido")
        else:
            return self.dni
    
    def mostrar(self):
        return f"Nombre:{self.nombre}, Edad:{self.edad}, DNI:{self.dni}"
    
    def esMayorDeEdad(self):
        if self.edad> 18:
            return f"{self.nombre} es mayor de edad"
        else:
            return f"{self.nombre} es menor de edad"

name= input("Ingrese el nombre:")
edad= int(input("Ingrese la edad:"))
dn= input("Ingrese identificacion:")
x= Persona(name,edad,dn)

print(x.mostrar())
print(x.esMayorDeEdad())