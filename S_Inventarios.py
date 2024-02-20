import datetime





Bio=[]
Sis=[]
Infra=[]

numero_activosB = 0
numero_activosS = 0
numero_activosI = 0
fecha_general= "NaN"

while True:
    try:
        print("\nBievenido al sistema de inventarios ")
        print("*"*30,"\n")
        print("¿A que area pertecene el activo:\n")
        print("(1)Biomedica\n(2)Sistemas\n(3)Infraestructura\n(4)Salir")
        entrada= int(input("Ingrese una opcion:"))

        while True:
            if entrada ==1:

                letra= "B"
                fechaactual= datetime.datetime.now()
                fecha= datetime.datetime.strftime(fechaactual,'%d/%m/%Y')
                numero_activosB=+1
                arreglo= f"{letra}-{fecha}-{numero_activosB:04}"


                modelo= input("Ingrese el numero de modelo:")
                
                while True:
                    try:
                        serie = int(input("Ingrese número de serie: "))
                        break  
                    except ValueError:
                        print("Por favor, ingrese un valor numérico para el número de serie.")

                while True:
                    try:
                        ubicacion= input("Ingrese la ubicacion del activo:")
                        if ubicacion.isalpha() == True:
                            break
                        else:
                            print("Por favor, ingrese solo letras.") 
                    except ValueError:
                        print("Por favor, ingrese solo letras.")

                
                while True:

                    try:
                        fecha_vencimiento= input("Ingrese fecha de vencimiento en formato DD/MM/AAAA:")
                        fecha_validada = datetime.datetime.strptime(fecha_vencimiento, '%d/%m/%Y')
                        print("¡Registro exitoso!")
                        break
                    except ValueError:
                        print("Formato de fecha incorrecto.")
                        
                
                bio=[arreglo,modelo,serie,ubicacion,fecha_vencimiento]
                Bio.append(bio)

                salida= input("¿Desea continuar ingresando mas datos al inventario Y/N ?").lower()
                if salida == "y":
                    continue
                elif salida == "n":
                    break
                else:
                    print("Ingrese una opcion valida")
    # except ValueError:
    #     print("Porfavor ingrese una opcion valida")
            

    
            if entrada == 2:

                letra= "S"
                fechaactual= datetime.datetime.now()
                fecha= datetime.datetime.strftime(fechaactual,'%d/%m/%Y')
                numero_activosS=+1
                arreglo= f"{letra}-{fecha}-{numero_activosS:04}"

                modelo= input("Ingrese el numero de modelo:")
                
                while True:
                    try:
                        serie = int(input("Ingrese número de serie: "))
                        break  
                    except ValueError:
                        print("Por favor, ingrese un valor numérico para el número de serie.")

                while True:
                    try:
                        ubicacion= input("Ingrese la ubicacion del activo:")
                        if ubicacion.isalpha() == True:
                            print("¡Registro exitoso!")
                            break
                        else:
                            print("Por favor, ingrese solo letras.") 
                    except ValueError:
                        print("Por favor, ingrese solo letras.")


                sis=[arreglo,modelo,serie,ubicacion,fecha_general]
                Sis.append(sis)

                salida= input("¿Desea continuar ingresando mas datos al inventario Y/N ?").lower()
                if salida == "y":
                    continue
                elif salida == "n":
                        break
                else:
                    print("Ingrese una opcion valida")

        
            if entrada == 3:
                letra= "I"
                fechaactual= datetime.datetime.now()
                fecha= datetime.datetime.strftime(fechaactual,'%d/%m/%Y')
                numero_activosI=+1
                arreglo= f"{letra}-{fecha}-{numero_activosI:04}"

                modelo= input("Ingrese el numero de modelo:")
                
                while True:
                    try:
                        serie = int(input("Ingrese número de serie: "))
                        break  
                    except ValueError:
                        print("Por favor, ingrese un valor numérico para el número de serie.")

                while True:
                    try:
                        ubicacion= input("Ingrese la ubicacion del activo:")
                        if ubicacion.isalpha() == True:
                            print("¡Registro exitoso!")
                            break
                        else:
                            print("Por favor, ingrese solo letras.") 
                    except ValueError:
                        print("Por favor, ingrese solo letras.")


                infra=[arreglo,modelo,serie,ubicacion,fecha_general]
                Infra.append(infra)

                salida= input("¿Desea continuar ingresando mas datos al inventario Y/N ?").lower()
                if salida == "y":
                    continue
                elif salida == "n":
                    break
                else:
                    print("Ingrese una opcion valida")

            if entrada == 4:
                print("Saliendo. . .")
                print(Bio,Sis,Infra)
                break
            
    except ValueError:
        print("Ingrese un opcion correcta")

