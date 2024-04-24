"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    return controller.new_controller(tipo)
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Escoger Tamaño")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    return controller.load_data(control, size_archivo)
    
    


def print_data(control):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
#    catalog = controller.get_data(control)
    #print(tabulate(catalog['elements']))
     

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    mem = int(input('Quiere observar el uso de memoria?\n 1: Si\n 2: No'))
    if mem == 1:
        memflag = True
    else:
        memflag = False
    pais = input('Inserte el codigo del pais: ')
    exp = input('Que nivel de experiencia busca?(junior,mid,senior): ')
    n = int(input('Ingrese la cantidad de ofertas que desea ver: '))
    tup = controller.req_1(control, n, pais, exp)
    
    return tup


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    mem = int(input('Quiere observar el uso de memoria?\n 1: Si\n 2: No'))
    if mem == 1:
        memflag = True
    else:
        memflag = False
    city = input('Inserte el nombre de la ciudad: ')
    empresa = input('Ingrese el nombre de la empresa: ')
    n = int(input('Ingrese la cantidad de ofertas que desea ver: '))    
    tup = controller.req_2(control, n , empresa, city, memflag)
    
    return tup


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    empresa = input('Escriba el nombre de la empresa que desea')
    fecha_in= input('Escriba la fecha inicial (mas antigua):')
    fecha_fin=input('Escriba la fecha final (mas reciente):')
    return  controller.req_3(control,empresa,fecha_in,fecha_fin)
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    mem = int(input('Quiere observar el uso de memoria?\n 1: Si\n 2: No'))
    if mem == 1:
        memflag = True
    else:
        memflag = False
    country = input("Escriba el codigo de país: ")
    f_inicio = input("La fecha inicial del periodo a consultar (con formato 'año-mes-dia'):")
    f_fin = input("La fecha final del periodo a consultar (con formato 'año-mes-dia'):")
    total_ofertas, total_empresas, total_ciudades, ciudad_mayor, ciudad_menor, catalogo = controller.req_4(control, country, f_inicio, f_fin, memflag)
    print(f"El total de ofertas es: {total_ofertas}")
    print(f"El total de empresas son: {total_empresas}")
    print(f"El total de ciudades son: {total_ciudades}")
    print(f"La ciudad con mayor numero de ofertas es {ciudad_mayor[0]} con un total de {ciudad_mayor[1]}")
    print(f"La ciudad con menor numero de ofertas es {ciudad_menor[0]} con un total de {ciudad_menor[1]}")
    
    
    print(tabulate(catalogo['elements'][:5]))

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    mem = int(input('Quiere observar el uso de memoria?\n 1: Si\n 2: No'))
    if mem == 1:
        memflag = True
    else:
        memflag = False
    ciudad= input("Escriba la ciudad que desea:  ")
    fecha_inicial= input("Escriba la fecha inicial (más antigua):  ")
    fecha_final= input("Escriba la fecha final (más reciente):  ")
    total_ofertas, total_empresas, mayor, menor, ultima_respuesta= controller.req_5(control, ciudad, fecha_inicial, fecha_final)
    print(f"El total de ofertas es: {total_ofertas}")
    print(f"El total de empresas son: {total_empresas}")
    print(f"La ciudad con mayor numero de ofertas es {mayor[0]} con un total de {mayor[1]}")
    print(f"La ciudad con menor numero de ofertas es {menor[0]} con un total de {menor[1]}")
    #print(ultima_respuesta)
    
    
    
    


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    exp = input('Que nivel de experiencia busca?(junior,mid,senior): ')
    n = int(input('Ingrese la cantidad de ciudades que desea ver: '))
    fecha= input('Escriba el anio') 

    ofertas = controller.req_6(control,n, exp, fecha)
    cantidad_ciudades = ofertas[1]
    empresas = ofertas[2]
    total = ofertas[0]
    mayor = ofertas[3]
    menor = ofertas[4]
    print('El total de ciudades que cumplen el requisito son:',cantidad_ciudades)
    print('El total de empresas que cumplen el requisito son:',empresas)
    print('El total de ofertas que cumplen el requisito son:',total)
    print('La ciudad con mayor cantidad de ofertas es:',mayor['city'],'con el total de ofertas:',mayor['count'])    
    print('La ciudad con menor cantidad de ofertas es:',menor['city'],'con el total de ofertas:',menor['count'])    
   


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    mem = int(input('Quiere observar el uso de memoria?\n 1: Si\n 2: No'))
    if mem == 1:
        memflag = True
    else:
        memflag = False
    n= int(input("Ingrese la cantidad de paises para la consulta: "))
    año = input("Ingrese el año de consulta (ej. 2022): ")
    mes = input("Ingrese el mes de consulta (ej. 03): ")
    total_ofertas, numero_ciudades, (pais_mayor, cuenta_pais_mayor), (ciudad_mayor, cuenta_ciudad_mayor), senior, mid, junior = controller.req_7(control, n, año, mes, memflag)
    
    
    print(f"El total de ofertas de empleo es {total_ofertas}")
    print(f"Número de ciudades donde se ofertó en los países resultantes de la consulta es {numero_ciudades}")
    print(f"{pais_mayor} es el pais con más ofertas y tiene {cuenta_pais_mayor}")
    print(f"{ciudad_mayor} es la ciudad con más ofertas y tiene {cuenta_ciudad_mayor}")

    
    for level, data in [('senior', senior), ('mid', mid), ('junior', junior)]:
        print(f"Para el nivel de experiencia {level}:")
        print(f"""
        La cantidad de habilidades diferentes son: {data[0]}
        La habilidad más solicitada es {data[1]['skill']} con {data[1]['count']} ofertas
        La habilidad menos solicitada es {data[2]['skill']} con {data[2]['count']} ofertas
        El nivel mínimo promedio es {data[3]}
        La cantidad de empresas que ofertaron es {data[4]}
        La empresa con más ofertas es {data[5]['empresa']} con {data[5]['count']} ofertas
        La empresa con menos ofertas es {data[6]['empresa']} con {data[6]['count']} ofertas
        """)

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
tipo = None
size_archivo = 1
default_limit = 1000

# main del reto
if __name__ == "__main__":
    #threading.stack_size(67108864*2)
    sys.setrecursionlimit(default_limit*1000000)
    #thread = threading.Thread(target=menu_cycle)
   # thread.start()
    
    control = new_controller()

    """
    Menu principal
    """
    
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            """poner parametro de archivo"""
            data = load_data(control)
            print('Skills cargados:',data[0])
            print('Ubicaciones cargadas:',data[2])
            print('Tipos de empleo cargados:',data[3])
            print('Trabajos cargados:',data[1])
            print_data(control)
            
        
        elif int(inputs) == 2:

            tup = print_req_1(control)
            print('La cantidad de ofertas en el pais que escogio: ',tup[0])
            print('La cantidad de ofertas según la condición escogida', tup[1])
            
            
        elif int(inputs) == 3:

            tup = print_req_2(control)
            print('La cantidad de ofertas segun la ciudad y empresa que escogio: ',tup[0])
            
      
            

        elif int(inputs) == 4:
            tup = print_req_3(control)
            print('La cantidad de ofertas total con estos requerimientos es de:',tup[0])
            print('La cantidad de ofertas "junior" es',tup[1]['value'])
            print('La cantidad de ofertas "mid" es',tup[2]['value'])
            print('La cantidad de ofertas "senior" es',tup[3]['value'])
            prnt = tup[4]['first']
            for i in range(0,tup[0]):
                info = prnt['info']
                print(info)
                prnt = prnt['next']
            
            
        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)
        
        elif int(inputs) == 10:
            size_archivo = int(input('Escoga el Tamaño:\n1.10%\n2.20%\n3.small%\n4.50%\n5.80%\n6.100%\nOpcion: '))
            
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)