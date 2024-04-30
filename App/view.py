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
from DISClib.ADT import orderedmap as om
assert cf
from tabulate import tabulate
import traceback
from datetime import datetime

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
    initial_Date = input('Ingrese una fecha inicial: ')
    final_Date = input('Ingrese una fecha final: ')
    result = controller.req_1(control, initial_Date, final_Date)
    print('El total de ofertas en ese rango de fechas es de: '+ str(result[0]))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    minSalary = float(input('Ingrese el salario minimo: '))
    maxSalary = float(input('Ingrese el salario maximo: '))
    total, lst = controller.req_2(control, minSalary, maxSalary)
    print(f'El total de ofertas en el rango de {minSalary}-{maxSalary} es de: {total}')
    oferta1 = lt.lastElement(lt.firstElement(lst))
    print(f'''Los datos de la primera oferta son: 
Fecha publicación oferta:  {datetime.strftime(oferta1['published_at'], '%Y-%m-%d')}
Título de la oferta: {oferta1['title']}
Nombre de la empresa de la oferta: {oferta1['company_name']}
Nivel de experticia de la oferta: {oferta1['experience_level']}
País de la empresa de la oferta: {oferta1['country_code']}
Ciudad de la empresa de la oferta: {oferta1['city']}
Tamaño de la empresa de la oferta: {oferta1['company_size']}
Tipo de ubicación de trabajo (remote, partialy, remote, office): {oferta1['workplace_type']}
Salario mínimo ofertado: {oferta1['salary_from']}
Habilidades solicitadas: {oferta1['skills']}
''')
    


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pais = input('Escriba el nombre del pais')
    n= input('Escriba el numero de ofertas:')
    exp=input('Escriba el nivel de exp:')
    return  controller.req_3(control,n,pais,exp)
    


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
    anio = int(input('Ingrese el año a consultar: '))
    pais = input('Ingrese el codigo de pais a consultar: ')
    print('''
          1. Habilidad
          2. Ubicacion de trabajo
          3. Nivel de experticia
          ''')
    conteo_sel = int(input('Ingrese una de las anteriores propiedades de conteo: '))
    
    if conteo_sel == 1:
        conteo = 'habilidad'
    elif conteo_sel == 2:
        conteo = 'ubicacion'
    else:
        conteo = 'experiencia'
    
    respuesta = controller.req_7(control, anio, pais, conteo, memflag)
    
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
            print_req_1(control)
            
        elif int(inputs) == 3:
            print_req_2(control)     

        elif int(inputs) == 4:
            tup = print_req_3(control)
            print('La cantidad de ofertas segun los requisitos es',tup[0])
            print(tup[1])
            """
            prnt = tup[1]
            for i in range(0,tup[1]):
                info = prnt['info']
                print(info)
                prnt = prnt['next']
            """
            
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