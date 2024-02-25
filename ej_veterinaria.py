class Mascota:
    def __init__(self) -> None:
        self.__nombre= ""
        self.__num_historia= int
        self.__tipo= ""
        self.__peso=""
        self.__fecha_ingreso= ""
        self.__medicamento= ""


    # Getters
    def ver_nombre(self):
        return self.__nombre
    
    def ver_tipo(self):
        return self.__tipo
    
    def ver_peso(self):
        return self.__peso
    
    def ver_num_historia(self):
        return self.__num_historia
    
    def ver_fecha_ingreso(self):
        return self.__fecha_ingreso
    
    def ver_medicamento(self):
        return self.__medicamento
    
    #Setters    
    def asignar_nombre(self,nombre):
        self.__nombre= nombre

    def asignar_tipo(self,tipo):
        self.__tipo= tipo

    def asignar_peso(self,peso):
        self.__peso= peso
    
    def asignar_num_historia(self,num):
        self.__num_historia= num

    def asignar_fecha_ingreso(self,ingreso):
        self.__fecha_ingreso= ingreso

    def asignar_medicamento(self,medicamento):
        self.__medicamento= medicamento

class Sistema:
    def __init__(self) -> None:
        self.lista_mascotas= []
        self.lista_medicamentos=[]

    def conseguir_nombre(self,num):
        for i in self.lista_mascotas:
            if num == i.ver_num_historia():
                return i.ver_nombre()
            
    def conseguir_cedula(self,num):
        for i in self.lista_mascotas:
            if num == i.ver_num_historia():
                return i.ver_num_historia()
            
    def Verificar_existente(self,num):
        for mascota in self.lista_mascotas:
            if num ==  mascota.ver_num_historia():
                return True



    def ingresar_mascota(self,mascota):
        self.lista_mascotas.append(mascota)

    def ver_fecha_ingreso(self,nombre):
        for mascota in self.lista_mascotas:
            if nombre == mascota.ver_nombre() :
                return mascota.ver_fecha_ingreso()
        return None
    
    def ver_num_mascotas(self):
        return len(self.lista_mascotas)

    def ver_medicamento(self,codigo):
        for mascota in self.lista_mascotas:
            if codigo == mascota.ver_num_historia():
                return mascota.ver_medicamento()
            
            
        

    def eliminar_mascota(self,mascota_eliminar):
        for mascota in self.lista_mascotas:
            if mascota_eliminar == mascota.ver_num_historia():
                self.lista_mascotas.remove(mascota)
        

sis= Sistema()
while True:
    print("Menu:")
    print("-"*30)
    print("¿Que desea hacer?\n1. Ingresar Mascota\n2. Ver fecha de ingreso\n3.Ver numero de mascotas registradas\n4.Ver medicamento suministrado(Filtrado por # de historia clinica)\n5.Eliminar mascota\n6.Salir")
    print("-"*30)

    entrada = int(input("Ingrese una opcion:"))

    if entrada==1:

        num_historia= int(input("Ingrese el numero de historia:"))
        f= sis.Verificar_existente(num_historia)
        if f == True:
            print("¡Ya existe una mascota registrada con ese numero de historia!")
        else:
            
        
            nombre= input("Ingrese el nombre de la mascota:") 
            tipo=input("Que tipo de mascota es (Canino/Felino):")
            peso= int(input("Ingrese el peso de la mascota:"))
            fecha_ingreso= input("Ingrese la fecha de ingreso:")
            medicamento= input("Medicamento suministrado:")

            mascota= Mascota()
            mascota.asignar_nombre(nombre)
            mascota.asignar_num_historia(num_historia)
            mascota.asignar_tipo(tipo)
            mascota.asignar_peso(peso)
            mascota.asignar_fecha_ingreso(fecha_ingreso)
            mascota.asignar_medicamento(medicamento)
            sis.ingresar_mascota(mascota)

    if entrada==2:
        fecha= input("Ingrese el nombre de la mascota:")
        busqueda= sis.ver_fecha_ingreso(fecha)
        print(f"La fecha de ingreso de la mascota {fecha} es : {busqueda}")

    if entrada ==3:
        print(f"el numero de mascotas ingresadas es :{sis.ver_num_mascotas()}")

    if entrada==4:
        codigo= int(input("Ingrese el # de historia clinica de la mascota:"))
        verificar= sis.ver_medicamento(codigo)
        nom= sis.conseguir_nombre(codigo)
        print(f"El medicamento suminstrado a {nom} es {verificar}")

    if entrada== 5:
        entrada1=int(input("Ingresa el # de historia del paciente:"))
        masc_eliminar= sis.eliminar_mascota(entrada1)

    if entrada== 6:
        break