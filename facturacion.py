print("-"*30)
print("Bienvenido al sistema de facturacion\n")
print("-"*30)

contador=0

comprador=[]
compra=0
articulos = {
    'resonador': {
        1: ['MAGNETOM', 'Sola', 1.5, 1000],
        2: ['MAGNETOM', 'Altea', 1.5, 1200],
        3: ['MAGNETOM', 'Amira', 1.5, 1300],
        4: ['MAGNETOM', 'Sempra', 1.5, 2000]
    },
    'angiografia': {
        1: ['Artis', 'zee', 1000],
        2: ['Artis', 'one', 1100],
        3: ['Artis', 'Q',1300],
        4: ['Artis', 'icono', 1500]
    },
    'radiografia': {
        1: ['YSIO', 'FAST', 1300],
        2: ['MULTIX', 'myExam', 1220],
        3: ['Multix', 'Select', 2050]
    }
}

while True:
    try:
        # name= input("Nombre del usuario:")
        # cc= int(input("Numero de cedula:"))
        # address= input("Direccion:")
        # tel= int(input("Telefono"))
        # datos=[name,cc,address,tel]
        # comprador.append(datos)
        # print("-"*20,"\n")

        print("¿Que articulos desea comprar?\nMenu:")
        print("\n1)Resonador\n2)Angiografia\n3)Radiografia\n4)Totalizar")
        entrada= int(input("Ingrese una opcion:"))

        if entrada==1:
            print("\nArtículos disponibles en Resonador:")
            for key, value in articulos['resonador'].items():
                print(f"Clave: {key}, Valor: {value}")                
            validacion= int(input("Ingrese el numero de la clave del articulo:"))
            if validacion ==1:
                for key, value in articulos['resonador'].items():
                    if key == 1:
                        print(f"Precio {value[3]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[3]
                        
            if validacion ==2:
                for key, value in articulos['resonador'].items():
                    if key == 2:
                        print(f"Precio {value[3]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[3]
            if validacion ==3:
                for key, value in articulos['resonador'].items():
                    if key == 3:
                        print(f"Precio {value[3]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[3]
            if validacion ==4:
                for key, value in articulos['resonador'].items():
                    if key == 4:
                        print(f"Precio {value[3]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[3]
                    
                        
        if entrada==2:
            print("\nArtículos disponibles en Resonador:")
            for key, value in articulos['angiografia'].items():
                print(f"Clave: {key}, Valor: {value}")                
            validacion= int(input("Ingrese el numero de la clave del articulo:"))
            if validacion ==1:
                for key, value in articulos['angiografia'].items():
                    if key == 1:
                        print(f"Precio {value[2]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[2]
                        
            if validacion ==2:
                for key, value in articulos['angiografia'].items():
                    if key == 2:
                        print(f"Precio {value[2]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[2]


            if validacion ==3:
                for key, value in articulos['angiografia'].items():
                    if key == 3:
                        print(f"Precio {value[2]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[2]
            if validacion ==4:
                for key, value in articulos['angiografia'].items():
                    if key == 4:
                        print(f"Precio {value[2]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[2]
                        


        if entrada==3:
            print("\nArtículos disponibles en Resonador:")
            for key, value in articulos['radiografia'].items():
                print(f"Clave: {key}, Valor: {value}")                
            validacion= int(input("Ingrese el numero de la clave del articulo:"))
            if validacion ==1:
                for key, value in articulos['radiografia'].items():
                    if key == 1:
                        print(f"Precio {value[2]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[2]
                        
            if validacion ==2:
                for key, value in articulos['radiografia'].items():
                    if key == 2:
                        print(f"Precio {value[2]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[2]
            if validacion ==3:
                for key, value in articulos['radiografia'].items():
                    if key == 3:
                        print(f"Precio {value[2]}$")
                        cuantos= int(input(f"Cuantos {value[0]} {value[1]} desea comprar:"))
                        compra+= cuantos*value[2]
                        print(compra)
        
        if entrada==4:
            print(f"El total de la compra es:{compra} \n")

        


    except ValueError:
        print("Inregese un valor valido")
