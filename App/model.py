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
from datetime import datetime as datetime
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
               'offers': None
              }    

    catalog['jobs'] = om.newMap(omaptype='RBT',cmpfunction=sort_criteria_date)
    catalog['skills'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria)

    catalog['multi-locations'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )
    catalog['emplyment-types'] = om.newMap(omaptype='RBT',cmpfunction=sort_criteria)




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
    mp.put(catalog['skills'],skills['id'],skills)

def add_jobs(data_structs, data):
    occurreddate = data["published_at"]
    oferta_date = datetime.strptime(occurreddate, "%Y-%m-%d")
    entry = om.get(map)

def updateDateIndex(map, job):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = job['OCCURRED_ON_DATE']
    jobdate = datetime.strptime(occurreddate, '%Y-%m-%d')
    entry = om.get(map, jobdate.date())
    if entry is None:
        datentry = newDataEntry(job)
        om.put(map, jobdate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, job)
    return map

def newDataEntry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'dateIndex': None, 'jobs': None}
    entry['dateIndex'] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     cmpfunction=compareOffenses)
    entry['jobs'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

def addDateIndex(datentry, job):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['jobs']
    lt.addLast(lst, job)
    offenseIndex = datentry['dateIndex']
    offentry = mp.get(offenseIndex, job['OFFENSE_CODE_GROUP'])
    if (offentry is None):
        entry = newOffenseEntry(job['published_at'], job)
        lt.addLast(entry['lstoffenses'], crime)
        m.put(offenseIndex, job['published_at'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstoffenses'], job)
    return datentry

def add_employment(data_structs,oferta):
    salario = oferta['salary_from']
    if salario != '':
        om.put(data_structs['employment-types'],salario,oferta['id'])

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
