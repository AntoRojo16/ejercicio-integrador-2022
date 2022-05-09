import csv
from claseMedicamento import Medicamento
from manejadorCama import ListaCama
class listaMedicamentos:

    def __init__(self):
        self.__lista=[]

    def agregarMedicamento(self,unMedicamento):
        self.__lista.append(unMedicamento)

    def inicializarMedicamentos(self):
        archivo=open("medicamentos.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                idcama=fila[0]
                idmedicamento=fila[1]
                nombre=fila[2]
                monodroga=fila[3]
                presentacion=fila[4]
                cantidad=fila[5]
                precio=fila[6]
                unMedicamento=Medicamento(idcama,idmedicamento,nombre,monodroga,presentacion,cantidad,precio)
                self.agregarMedicamento(unMedicamento)
        archivo.close()

    def __str__(self):
        s=""
        for medicamento in self.__lista:
            s+= str(medicamento)+"\n"
        return s


    def buscarMedicamento(self,id):
        m="Menicamento"
        M="Monodroga"
        P="Presentacion"
        c="Cantidad"
        p="Precio"
        print("{:>0}/{}{:>50}{:>50}{:>50},".format (m,M,P,c,p))
        for medicamento in self.__lista:

            if medicamento.getIdCama()==id:

                print("{:>0}/{}{:>50}{:>50}{:>50}".format(medicamento.getNombre(),medicamento.getMonodroga(),medicamento.getPresentacion(),medicamento.getCantidad(),medicamento.getPrecio()))

    def MostrarDatos(self,camas):
        med=input("Ingrese medicameto")
        i=0
        for medicamento in self.__lista:
            if (medicamento.getNombre()==med):
                camas.mostrar(medicamento.getIdCama())











