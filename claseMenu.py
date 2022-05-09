from manejadorCama import ListaCama
from manejadorMedicamentos import listaMedicamentos

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            0:self.salir
                          }
    def opcion(self,op,medicamentos,camas):
        print(op)
        func=self.__switcher.get(op,lambda: print("Opción no válida"))
        func(medicamentos,camas)

    def salir(self,medicamentos,camas):
        print('Usted salio del programa')
    def opcion1(self,medicamentos,camas):
        j=camas.buscarPaciente("Perez, Luis")
        medicamentos.buscarMedicamento(j)


    def opcion2(self,medicamentos,camas):
        medicamentos.MostrarDatos(camas)


        
