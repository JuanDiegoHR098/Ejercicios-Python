# class Persona:
#     def __init__(self) -> None:
#         self.__nombre= ""
#         self.__cedula= ""
#         self.__genero= ""
#         self.__servicio= ""

#     #Getters
#     def get_nombre(self):
#         return self.__nombre 
#     def get_cedula(self):
#         return self.__cedula
#     def get_genero(self):
#         return self.__genero
#     def get_servicio(self):
#         return self.__servicio
    
#     #Setters
#     def set_nombre(self,nombre):
#         self.__nombre= nombre
#     def set_cedula(self,cedula):
#         self.__cedula= cedula
#     def set_genero(self,genero):
#         self.__genero= genero
#     def set_servicio(self,servicio):
#         self.__servicio= servicio
    

# class Sistema():
    
#     def __init__(self) -> None:
#         self.__lista_paciente=[]
        

#     def get_listaPacientes(self):
#         return self.__lista_paciente
    

    
#     def get_numeroPacientes(self):
#         return len(self.__lista_paciente)
    
    


#     def ingresar_paciente(self,paciente):
#         #Ingresar ds del paciente
#         self.__lista_paciente.append(paciente)

            
#     def verDatosPaciente(self,c):
#         pacientes_coinciden=[]
#         # if self.verificarPac(c) == False:
#         #     return None
#         for p in self.__lista_paciente:
#             if c == p.get_cedula():
#                 return p
#             if c in p.get_nombre().lower():
#                 pacientes_coinciden.append(p)
#             return None
    
            
# sis= Sistema()

# while True:
    
    
#     print("Menu:")
#     print("¿Que desea hacer?\n1. Ingresar Paciente\n2. Ver datos del paciente\n 3. Ver numero de pacientes\n4. Salir")

#     entrada= int(input("Ingrese una opcion:"))

#     if entrada == 1:
        
#         nombre= input("Ingresar nombre del paciente:")
#         cedula= (input("Ingrese cedula del paciente:"))
#         genero= input("Genero:")
#         servicio= input("Ingrese servicio donde se encuentra:")

#         paciente= Persona() 
#         paciente.set_nombre(nombre)
#         paciente.set_cedula(cedula)
#         paciente.set_genero(genero)   
#         paciente.set_servicio(servicio)
#         sis.ingresar_paciente(paciente)
#         print(f"¡El paciente {nombre} se a ingresado satiscatoriamente!")
        
#     elif entrada== 2:
#         validacion= (input("Ingrese el numero de cedula del paciente"))
#         paciente_encontrado= sis.verDatosPaciente(validacion)

#         if paciente_encontrado == None:
#             print("Paciente no encontrado")
#         else:
            
#             print("Nombre: ", paciente_encontrado.get_nombre())
#             print("Genero: ", paciente_encontrado.get_genero())
#             print("Servicio: ", paciente_encontrado.get_servicio())
    
#     elif entrada == 3:
#         print(f"El numero de pacienes registrado es : {sis.get_numeroPacientes()}")
            
        

#     if entrada==4:
#         break


class Persona:
    def __init__(self) -> None:
        self.__nombre = ""
        self.__cedula = ""
        self.__genero = ""
        self.__servicio = ""

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_cedula(self):
        return self.__cedula

    def get_genero(self):
        return self.__genero

    def get_servicio(self):
        return self.__servicio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def set_genero(self, genero):
        self.__genero = genero

    def set_servicio(self, servicio):
        self.__servicio = servicio


class Sistema:

    def __init__(self) -> None:
        self.__lista_paciente = []

    def get_listaPacientes(self):
        return self.__lista_paciente

    def get_numeroPacientes(self):
        return len(self.__lista_paciente)

    def ingresar_paciente(self, paciente):
        self.__lista_paciente.append(paciente)

    def buscar_paciente(self, clave):
        pacientes_coinciden = []

        for p in self.__lista_paciente:
            if clave == p.get_cedula() or clave.lower() in p.get_nombre().lower():
                paciente_info = (
                    p.get_nombre(), p.get_cedula(), p.get_genero(), p.get_servicio())
                pacientes_coinciden.append(paciente_info)

        return pacientes_coinciden

sis = Sistema()

while True:
    print("Menu:")
    print("¿Que desea hacer?\n1. Ingresar Paciente\n2. Ver datos del paciente\n3. Ver numero de pacientes\n4. Salir")

    entrada = int(input("Ingrese una opcion:"))

    if entrada == 1:
        nombre = input("Ingresar nombre del paciente:")
        cedula = input("Ingrese cedula del paciente:")
        genero = input("Genero:")
        servicio = input("Ingrese servicio donde se encuentra:")

        paciente = Persona()
        paciente.set_nombre(nombre)
        paciente.set_cedula(cedula)
        paciente.set_genero(genero)
        paciente.set_servicio(servicio)

        sis.ingresar_paciente(paciente)
        print(f"¡El paciente {nombre} se ha ingresado satisfactoriamente!")

    elif entrada == 2:
        clave_busqueda = input("Ingrese el numero de cedula o nombre del paciente:")
        pacientes_encontrados = sis.buscar_paciente(clave_busqueda)

        if not pacientes_encontrados:
            print("Paciente no encontrado")
        else:
            for paciente_encontrado in pacientes_encontrados:
                print(( "Nombre: {}, Cedula: {}, Genero: {}, Servicio: {}").format(
                    *paciente_encontrado))

    elif entrada == 3:
        print(f"El numero de pacientes registrados es: {sis.get_numeroPacientes()}")

    elif entrada == 4:
        break

