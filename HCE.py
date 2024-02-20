# Crear una Historia Clínica Electrónica donde se puedan almacenar los datos de
# Nombre, identificación, edad y EPS de los pacientes.
# 1. Realice este algoritmo utilizando un ciclo for y las sentencias que este utiliza.
# 2. Crear un rango de tamaño 1000, los cuales serán los ciclos del for.
# 3. Almacene la información del paciente utilizando listas anidadas.
# 4. Las listas anidadas deben empezar vacías.
# 5. El algoritmo deberá preguntar al usuario si desea ingresar más pacientes o
# salir, en caso de salir, deberá imprimir la información almacenada de los
# pacientes.

print("Bienvenido al sitema de inventario")
print("-"*50)

hc=[]


for i in range(100):
    nombre=[]
    cc=[]
    edad=[]
    eps=[]
    name= input("Ingrese el nombre del paciente:")
    ide= int(input("Ingrese cedula del paciente:"))
    age= input("Ingrese edad del paciente:")
    salud= input("Ingrese EPS del paceinte:")
    nombre.append(name)
    cc.append(ide)
    edad.append(age)
    eps.append(salud)
    historia=[nombre,cc,edad,eps]
    hc.append(historia)
    validacion= input("¿Desea continuar ingresando pacientes? Y/N").lower()
    if validacion == "y":
        continue
    elif validacion=="n":
        print(hc)
        print(len(hc))
        break