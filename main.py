from manejadorCama import ListaCama
from manejadorMedicamentos import listaMedicamentos
from claseMenu import Menu


if __name__ == '__main__':
    unManejadorCama=ListaCama()
    unManejadorMedicamentos=listaMedicamentos()
    unManejadorCama.inicializar()
    unManejadorMedicamentos.inicializarMedicamentos()
    bandera = False
    while not bandera:
        print("\nMENU DE OPCIONES")
        print("0 Salir")
        print("1 ITEM 1: ) Dado un el nombre y apellido de un paciente internado al que se le da el alta, listar los datos \ndel paciente y los medicamentos que deberá devolver, indicando el precio de cada medicamento y \nel total que deberá abonar en caso de no devolverlos")
        print("2 ITEM 2: Listar los datos de pacientes internados (cama ocupada), que tienen un diagnóstico leído desde teclado")

        opcion = int(input('Ingrese una opcion:'))
        unmenu=Menu()
        unmenu.opcion(opcion,unManejadorMedicamentos,unManejadorCama)
        bandera = int(opcion)== 0

