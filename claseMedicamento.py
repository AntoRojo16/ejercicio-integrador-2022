class Medicamento:
    __idCama=0
    __idMedicamento=0
    __nombreComercial=""
    __monoDroga=""
    __presentacion=""
    __cantidadApli=0
    __precioTotal=0

    def __init__(self,id,idM,nomC,mono,pre,cantidad,precio):

        self.__idCama=id
        self.__idMedicamento=idM
        self.__nombreComercial=nomC
        self.__monoDroga=mono
        self.__presentacion=pre
        self.__cantidadApli=cantidad
        self.__precioTotal=precio

    def __str__(self):
        return ("ID de cama {}, ID de habitacion {}, Nombre comercial {}, Mono droga {}, Presentacion {}, cantidad aplicad {}, precio total {}".format(self.__idCama,self.__idMedicamento,self.__nombreComercial,self.__monoDroga,self.__presentacion,self.__cantidadApli,self.__precioTotal))

    def getIdCama(self):
        return self.__idCama

    def getNombre(self):
        return self.__nombreComercial

    def getPresentacion(self):
        return self.__presentacion

    def getPrecio(self):
        return self.__precioTotal


    def getMonodroga(self):
        return self.__monoDroga

    def getCantidad(self):
        return self.__cantidadApli



