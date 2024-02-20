# Un hospital necesita un programa para gestionar la información de pacientes y visualizar las imágenes radiológicas de manera eficiente. El sistema debe permitir registrar nuevos pacientes, asociar imágenes a pacientes existentes y mostrar imágenes específicas de pacientes.

# **Condiciones**:
# 1. Construir un Menú de entrada que le pregunte al usuario si quiere ingresar un paciente, ingresar una imagen o si quiere Salir.

#   **Ejemplo**:
#     1. Ingresar paciente
#     2. Ingresar información de imagen
#     3. Salir
# 2. Posterior a la selección del menú preguntar los datos del paciente en caso tal de ser seleccionado "Ingresar pacience" *(Nombres, cédula y edad)*. En caso tal de seleccionar "Ingresar información de la imagen" , generar un buscador por cédula para asociar los datos del la imagen a un paciente *(Tipo de imagen, fecha del procedimiento)*. Validar que las entradas sean del tipo de dato que se le especifica (ver tabla).

#   Nota:

#     * Cuando se ingresa la información del paciente, NO se solicita información de la imagen.  
# 3. Importante: para el caso de la fecha únicamente se acepta fechas en el formato establecido.
# 4. Para el caso del tipo de imagen, debe contener el tipo de imagen seguido del número del paciente. Para el caso del tipo de imagen, puede tener las siguientes opciones:

#   * CT: Tomografía computarizada
#   * RX: Rayos X
#   * MRI: Resonancia Magnética

# 5. El algoritmo debe ser diseñado para ingresar DOS pacientes y luego de esto debe pedir al usuario si desea volver a ingresar otro paciente o salirse del algoritmo.
# 6. Cuando decida salir, el algoritmo deberá mostrar la información de los pacientes ingresado con las imágenes que tiene asociado.
# 7. Añada el paciente al sistema general, es decir cree una matriz que contenga registrado cada uno de los datos solicitados de todos los pacientes ingresados.

#   **Ejemplo**:

#   [[Nombres, Edad, Cedula,[Tipo de imagen, fecha del procedimiento]],[...]]


# | Datos | Tipo de dato | Ejemplo |
# |----------|----------|----------|
# | Nombres    | str   | Luisa María Zapata Saldarriaga   |
# | Edad    | int   | 20   |
# | Documento de identidad    | int   | 0123456789   |
# | Tipo de imagen| Alfanúmerico| CT-0001 |
# |Fecha del procedimiento|Alfanúmerico |DD/MM/AA|

import datetime
print("\nBienvendio Al Sistema de Visualización de Imágenes Radiológicas")
print("*"*60,"\n")

pacientes=[]
ct=0
rx=0
rm=0

def  ingresar_paciente():
    global save
    while True:
        try:
            nombre=input("Ingrese nombre del paciente:")
            cc=int(input("Ingrese cedula del paciente:"))
            edad= int(input("Ingrese edad del paciente"))
            print("¡Registro exitoso!")
            save=[nombre,cc,edad]
            pacientes.append(save)
            validar= input("¿Desea seguir ingresando pacientes? Y/N").lower()
            if validar=="y":
                continue
            elif validar=="n":
                break
            else:
                print("Ingrese una opcion valida.")
        except ValueError:
            print("¡Ingrese un un valor valido!")

def info_imagen():
    global ct,rx,rm
    while True:
    # for x in pacientes:
        
        print("\nMenu:\n1)Asociar usuario\n2)Salir")
        entrada= int(input("Ingrese una opcion:"))
        if entrada ==1:
            print(pacientes[0:])
            busqueda= int(input("Ingrese el numero de cedula del paciente:"))
            for i in pacientes:   
                if busqueda in i:
                    print("Tipo de imagen:\n1)Tomografia computarizada (CT)\n2)Rayos X (RX)\n3)Resonancia Magnetica (RM)")
                    tipo= int(input("Tipo de imagen:"))
                    if tipo == 1:
                        letra="CT"
                        ct+=1
                        arreglo=f"{letra}-{ct:04}"
                        while True:
                            try:
                                fecha_procedimiento= input("Ingrese fecha del procedimiento en formato DD/MM/AAAA:")
                                fecha_validada = datetime.datetime.strptime(fecha_procedimiento, '%d/%m/%Y')
                                break
                            except ValueError:
                                print("Formato de fecha incorrecto.")

                        arreglo2=f"{arreglo},{fecha_procedimiento}"
                        arreglo3=[arreglo2]
                        img_ct=[save.append(arreglo3)]
                        #pacientes.append(img_ct)
                        
                validar= input("¿Desea seguir ingresando datos? Y/N")
                        
                if validar=="y":
                    continue
                if validar=="n":
                    break
                else:
                    print("Ingrese una opcion valida.")
                
                    

                    if tipo == 2:
                        letra="RX"
                        
                        rx+=1
                        arreglo=f"{letra}-{rx:04}"
                        while True:
                            try:
                                fecha_procedimiento= input("Ingrese fecha del procedimiento en formato DD/MM/AAAA:")
                                fecha_validada = datetime.datetime.strptime(fecha_procedimiento, '%d/%m/%Y')
                                break
                            except ValueError:
                                print("Formato de fecha incorrecto.")
                        arreglo2=f"{arreglo},{fecha_procedimiento}"
                        arreglo3=[arreglo2]
                        img_ct=[save.append(arreglo3)]
                                #pacientes.append(img_ct)
                        validar= input("¿Desea seguir ingresando datos? Y/N")
                        if validar=="y":
                            continue
                        elif validar=="n":
                            break
                        else:
                            print("Ingrese una opcion valida.")

                    
                    if tipo == 3:
                        letra="RM"
                        
                        rm+=1
                        arreglo=f"{letra}-{rm:04}"
                        while True:
                            try:
                                fecha_procedimiento= input("Ingrese fecha del procedimiento en formato DD/MM/AAAA:")
                                fecha_validada = datetime.datetime.strptime(fecha_procedimiento, '%d/%m/%Y')
                                break
                            except ValueError:
                                print("Formato de fecha incorrecto.")
                        arreglo2=f"{arreglo},{fecha_procedimiento}"
                        arreglo3=[arreglo2]
                        img_ct=[save.append(arreglo3)]
                                    #pacientes.append(img_ct)
                        validar= input("¿Desea seguir ingresando datos? Y/N").lower()
                        if validar=="y":
                            continue
                        if validar=="n":
                            break
                        else:
                            print("Ingrese una opcion valida.")
        if entrada==2:
            break
        else:
            print("Opcion no valida")
        
                        


while True:
    try:        
        print("\nMenu:\n")
        print("¿Que desea hacer?:\n")
        print("(1)Ingresar paciente\n(2)Ingresar informacion de imagen\n(3)Salir")
        entrada= int(input("Ingrese una opcion:"))

        if entrada==1:
            ingresar_paciente()
        elif entrada==2:
            info_imagen()
        elif entrada==3:
            print("Saliendo. . . ")
            print(pacientes)
            break
    except ValueError:
        print("Ingrese una opcion valida. . .")