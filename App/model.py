"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from datetime import datetime
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(tipo):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {'skills':None,
               'multi-locations': None,
               'jobs': None,
               'employment-types':None,
               'arbolFechas': None,
               'mapaPais': None,
               'mapaCiudad': None,
               'arbolTamaño': None,
               'arbolSalary': None,
               'mapaHabilidad': None
              }    

    catalog['jobs'] =  mp.newMap(17,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria)
    catalog['skills'] = mp.newMap(5,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria)

    catalog['multi-locations'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )
    catalog['employment-types'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )
    
    catalog['arbolFechas'] = om.newMap(omaptype='RBT',cmpfunction=compareDates)
    
    catalog['mapaPais'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )
    catalog['mapaCiudad'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )
    catalog['arbolTamaño'] = om.newMap(omaptype='RBT',cmpfunction=compareDates)
    
    catalog['arbolSalary'] = om.newMap(omaptype='RBT',cmpfunction=compareDates)
    
    catalog['mapaHabilidad'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )

    return catalog


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    
    pass

def add_skills(catalog, skills):
    """
    Función para agregar nuevos elementos a la lista
    """
    habilidad = skills['name']
    contiene = mp.contains(catalog['mapaHabilidad'], habilidad)
    if contiene == False:
        arbol_nivel = om.newMap(omaptype='RBT',cmpfunction=compareDates)
        lista_id = lt.newList('Array_List')
        lt.addLast(lista_id, skills['id'])
        om.put(arbol_nivel, skills['level'], lista_id)
        mp.put(catalog['mapaHabilidad'], habilidad, arbol_nivel)
    else:
        pareja = mp.get(catalog['mapaHabilidad'], habilidad)
        arbol_nivel = me.getValue(pareja)
        contiene_nivel = om.contains(arbol_nivel, skills['level'])
        if contiene_nivel == False:
            lista_id = lt.newList('Array_List')
            lt.addLast(lista_id, skills['id'])
            om.put(arbol_nivel, skills['level'], lista_id)
        else:
            pareja_nivel = om.get(pareja, skills['level'])
            lista_id_nivel = me.getValue(pareja_nivel)
            lt.addLast(lista_id_nivel, skills['id'])
    
    mp.put(catalog['skills'],skills['id'],skills)

def add_jobs(catalog, data):
    # Se crea un arbol, cuyas llaves son la fecha en la que se publicaron y sus valores son una lista de datos. 
    fecha = data['published_at']
    data['published_at'] = datetime.strptime(fecha, '%Y-%m-%dT%H:%M:%S.%fZ')
    if not om.contains(catalog['arbolFecha'], data['published_at']):
        lista_fecha = lt.newList('ARRAY_LIST')
        om.put(catalog['arbolFecha'], data['published_at'], lista_fecha)
    else:
        lista_fecha = me.getValue(om.get(catalog['arbolFecha'], data['published_at']))
    lt.addLast(lista_fecha, data)
    # Se crea un mapa, cuyas llaves son el pais, y sus valores son un mapa cuyas cuyas llaves son los niveles de experticia y valores lista de datos
    pais = data['country_code']
    experticia_data = data['experience_level']
    if not om.contains(catalog['mapaPais'], pais):
        experticia = mp.newMap(11,
                                maptype='CHAINING',
                                loadfactor=4,
                                cmpfunction=sort_criteria
                                )
        junior = lt.newList('ARRAY_LIST')
        mid = lt.newList('ARRAY_LIST')
        senior = lt.newList('ARRAY_LIST')
        
        mp.put(experticia, 'junior', junior)
        mp.put(experticia, 'mid', mid)
        mp.put(experticia, 'senior', senior)
        
        mp.put(catalog['mapaPais'], pais, experticia)
    
    paisMapa = me.getValue(om.get(catalog['mapaPais'], pais))
    listaExperticia = me.getValue(om.get(paisMapa, experticia_data))
        
    lt.addLast(listaExperticia, data)
    #
        
        
def convertirSalario(salario, moneda):
    if moneda == 'eur':
        salario = salario *1.07
    elif moneda == 'pln':
        salario = salario*0.25
    
    return salario


def add_employment(catalog, oferta):
    salario = oferta['salary_from']
    currency = oferta['currency_salary']
   
    if salario != '' and salario != ' ':
        oferta['salary_from'] = convertirSalario(float(salario), currency)
        oferta['currency_salary'] = 'usd'
        om.put(catalog['arbolSalary'], oferta['salary_from'], oferta['id'])
    mp.put(catalog['multi-locations'], oferta['id'], oferta)

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
     
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, initialDate, finalDate):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    lst = om.values(data_structs, initialDate, finalDate)
    totjobs = 0
    for job in lt.iterator(lst):
        totjobs +=lt.size(job['jobs'])
    return totjobs, lst


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
    
def compareOffenses(offense1, offense2):
    """
    Compara dos tipos de crimenes
    """
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1
    
def sort_criteria(id, entry):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    identry = me.getKey(entry)
    if id == identry:
        return 0
    elif id > identry:
        return 1
    else:
        return -1
    pass

def sort_criteria_date(date1, date2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    dateentry = date1['published_at']
    datecurrent = date2['published_at']    
    if dateentry == datecurrent:
        return 0
    elif datecurrent > dateentry:
        return 1
    else:
        return -1


def sort_criteria(fecha, entry):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    identry = me.getKey(entry)
    if id == identry:
        return 0
    elif id > identry:
        return 1
    else:
        return -1
    pass
def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
