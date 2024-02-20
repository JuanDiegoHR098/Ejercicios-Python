# class Usuario:
#     def __init__(self,nombre,apellido) :
#         self.nombre = nombre
#         self.apellido = apellido
    
#     def saludo(self):
#         print("Hola, mi nombre es", self.nombre,self.apellido)

# x= input("Ingrese su nombre:")
# y=input("Ingrese su apellido")
# usuario= Usuario(x,y)
# usuario.saludo()


#Realizar un progrma que conste de una clase llamada alumno que tenga como atributos el nombre y la nota del alumno
#Definir los metodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si aprobo o no

# class Alumno:
#     def __init__(self,nombre,nota):
#         self.nombre= nombre
#         self.nota= nota

#     def imprimir(self):
#         print(f"Nombre:",self.nombre)
#         print(f"Nota:",self.nota)
#         print("")
    
#     def validar(self):
#         if self.nota < 3:
#             print("Reprobo")
#         elif self.nota >=3 and self.nota<=5:
#             print("Aprobo")
#         else:
#             print("Ingrese un valor valido")

# x= Alumno("Juan",6)
# y=Alumno("Diego",2)

# x.imprimir()
# x.validar()


#Haga una calculadora utilizando clases

# class Calculadora:
#     def __init__(self,a,b):
#         self.suma = a+b
#         self.resta= a-b
#         self.multiplicacion= a*b
#         self.cuadrado= a**b
#         self.division= a/b

# f= Calculadora(2,3)

# print(f.suma)