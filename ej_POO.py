class Persona:
    def __init__(self) -> None:
        self.__nombre= ""
        self.__cedula= int
        self.__genero= ""
        self.__servicio= ""

    #Getters
    def get_nombre(self):
        return self.__nombre 
    def get_cedula(self):
        return self.__cedula
    def get_genero(self):
        return self.__genero
    def get_servicio(self):
        return self.__servicio
    
    #Setters
    def set_nombre(self,nombre):
        self.__nombre= nombre
    def set_cedula(self,cedula):
        self.__cedula= cedula
    def set_genero(self,genero):
        self.__genero= genero
    def set_servicio(self,servicio):
        self.__servicio= servicio
    

class Sistema():
    
    def __init__(self) -> None:
        self.__lista_paciente=[]
        self.__numero_pacientes= len(self.__lista_paciente)

    def get_listaPacientes(self):
        return self.__lista_paciente
    
    def get_numeroPacientes(self):
        return self.__numero_pacientes
    
    


    def ingresar_paciente(self,paciente):
        #Ingresar ds del paciente
        self.__lista_paciente.append(paciente)

    # def ver_datos_paciente(self,c):
    #     # for i in self.__lista_paciente:
    #     #     if i.ge in 
    #         pass
    
    # def ver_datos_paciente(self, c):
    #     for paciente in self.__lista_paciente:
    #         if paciente == c:
    #             print(f"Nombre: {paciente.get_nombre()}")
    #             print(f"Cedula: {paciente.get_cedula()}")
    #             print(f"Genero: {paciente.get_genero()}")
    #             print(f"Servicio: {paciente.get_servicio()}")
    #             return
    #     print("Paciente no encontrado.")
    # def verificarPac(self,ced):
    #     encontrado =  False
    #     for p in self.__lista_paciente:
    #         if ced == p.get_cedula():
    #             encontrado = True
    #             break
    #     return encontrado
            
    def verDatosPaciente(self,c):
        # if self.verificarPac(c) == False:
        #     return None
        for p in self.__lista_paciente:
            if c == Persona.get_cedula():
                return p

while True:
    
    sis= Sistema()
    print("Menu:")
    print("¿Que desea hacer?\n1. Ingresar Paciente\n2. Ver datos del paciente\n 3. Ver numero de pacientes\n4. Salir")

    entrada= int(input("Ingrese una opcion:"))

    if entrada == 1:
        
        nombre= input("Ingresar nombre del paciente:")
        cedula= int(input("Ingrese cedula del paciente:"))
        genero= input("Genero:")
        servicio= input("Ingrese servicio donde se encuentra:")

        paciente= Persona() 
        paciente.set_nombre(nombre)
        paciente.set_cedula(cedula)
        paciente.set_genero(genero)   
        paciente.set_servicio(servicio)
        r=sis.ingresar_paciente(paciente)
        print(f"¡El paciente {nombre} se a ingresado satiscatoriamente!")
        
    elif entrada== 2:
        validacion= int(input("Ingrese el numero de cedula del paciente"))
        f=sis.verDatosPaciente(validacion)
        if f == None:
            print("Paciente no encontrado")
        else:
            
            print("Nombre: " + f.get_nombre())
            
        

    if entrada==4:
        break


