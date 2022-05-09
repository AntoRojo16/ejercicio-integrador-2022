import csv
from claseCama import Cama
class ListaCama:

    def __init__(self):
        self.__lista=[]

    def agregarCama(self,unaCama):
        self.__lista.append(unaCama)

    def inicializar(self):
        archivo=open("camas.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera= True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                idCama=fila[0]
                habitacion=fila[1]
                estado=fila[2]
                nomyap=fila[3]
                diagnostico=fila[4]
                fi=fila[5]
                print(fi)
                unaCama=Cama(idCama,habitacion,estado,nomyap,diagnostico,fi)
                self.agregarCama(unaCama)

        archivo.close()


    def __str__(self):
        s=""
        for cama in self.__lista:
            s+= str(cama)+"\n"
        return s


    def buscarPaciente(self,nomap):

        i=0
        nom=self.__lista[i].getNombre()
        while(i<len(self.__lista))and(nom!=nomap):
            i+=1
            nom=self.__lista[i].getNombre()
        if i<len(self.__lista):
            print("Se encontro el paciente")
            #fecha=input("Ingrese la fecha en la que se le va a dar el alta")
            self.__lista[i].agregarFechaAlta("24/04/2022")
            print("\nPaciente {} Cama {} Habitacion {}".format(self.__lista[i].getNombre(),self.__lista[i].getId(),self.__lista[i].getHabitacion()))
            print("\nDiagnostico {} Fecha de Alta {} \nFecha de internacion {}".format(self.__lista[i].getDiagnostico(),self.__lista[i].getFechaAlta(),self.__lista[i].getFechaInternacion()))
            return self.__lista[i].getId()

    def mostrar(self,id):
        print(self.__lista[int(id)-1])


