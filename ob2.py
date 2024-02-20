class Persona:
    def __init__(self, nombre="", edad=None, dni=""):
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_dni(dni)

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            print("Error: El nombre debe ser una cadena de texto.")

    def get_nombre(self):
        return self._nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            print("Error: La edad debe ser un número entero positivo.")

    def get_edad(self):
        return self._edad

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self._dni = dni
        else:
            print("Error: El DNI debe ser una cadena de 9 caracteres.")

    def get_dni(self):
        return self._dni

    def mostrar(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Edad: {self.get_edad()}")
        print(f"DNI: {self.get_dni()}")

    def esMayorDeEdad(self):
        return self.get_edad() >= 18

# Ejemplo de uso:
# Crear una persona
    
name= input("Ingrese el nombre:")
edad= int(input("Ingrese la edad:"))
dn= input("Ingrese identificacion:")

persona1 = Persona(nombre=name, edad=edad, dni=dn)
# Mostrar los datos
persona1.mostrar()
# Verificar si es mayor de edad
print(f"¿Es mayor de edad? {persona1.esMayorDeEdad()}")