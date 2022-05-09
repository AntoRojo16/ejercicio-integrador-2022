class Cama:
    __idCama=0
    __habitacion=0
    __estado=None
    __nombreYapellido=None
    __diagnostico=""
    __fechaInternacion=""
    __fechaAlta=""


    def __init__(self,id,hab,estado,nya,diagnostico,fechai,fechaa=0):
        self.__idCama=id
        self.__habitacion=hab
        self.__estado=estado
        self.__nombreYapellido=nya
        self.__diagnostico=diagnostico
        self.__fechaInternacion=fechai
        self.__fechaAlta=fechaa

    def __str__(self):
        return ("Id cama {}, habitacion {}, estado {}, nombre y apellido {}, diagnostico {}, fecha de internacion {}, fecha de alta {}".format(self.__idCama,self.__habitacion,self.__estado,self.__nombreYapellido,self.__diagnostico,self.__fechaInternacion,self.__fechaAlta))

    def getNombre(self):
        return self.__nombreYapellido

    def getId(self):
        return self.__idCama

    def getHabitacion(self):
        return self.__habitacion

    def getDiagnostico(self):
        return self.__diagnostico

    def getFechaAlta(self):
        return self.__fechaAlta

    def getFechaInternacion(self):
        print(self.__fechaInternacion)
        return self.__fechaInternacion

    def agregarFechaAlta(self,fecha):
        print("hola")
        print(fecha)
        self.__fechaAlta=fecha


    def __str__(self):
        return ("ID de cama {} Habitacion {} Estado {} Nombre y Apellido del paciente {} Diagnostico {} Fecha de internacion {} Fecha de alta {}".format(self.__idCama,self.__habitacion,self.__estado,self.__nombreYapellido,self.__diagnostico,self.__fechaInternacion,self.__fechaAlta))


