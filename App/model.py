﻿"""
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
               'multilocations': None,
               'jobs': None,
               'employment-types':None,
               'arbolFecha': None,
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

    catalog['multilocations'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )
    catalog['employment-types'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )
    
    catalog['arbolFecha'] = om.newMap(omaptype='RBT',cmpfunction=compareDates)
    
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

def add_locations(catalog, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    mp.put(catalog['multilocations'],data['id'], data)

def add_skills(catalog, skills):
    """
    Función para agregar nuevos elementos a la lista
    """
    habilidad = skills['name']
    contiene = mp.contains(catalog['mapaHabilidad'], habilidad)
    if contiene == False:
        arbol_nivel = om.newMap(omaptype='RBT',cmpfunction=compareDates)
        lista_id = lt.newList('ARRAY_LIST')
        lt.addLast(lista_id, skills['id'])
        om.put(arbol_nivel, skills['level'], lista_id)
        mp.put(catalog['mapaHabilidad'], habilidad, arbol_nivel)
    else:
        pareja = mp.get(catalog['mapaHabilidad'], habilidad)
        arbol_nivel = me.getValue(pareja)
        contiene_nivel = om.contains(arbol_nivel, skills['level'])
        if contiene_nivel == False:
            lista_id = lt.newList('ARRAY_LIST')
            lt.addLast(lista_id, skills['id'])
            om.put(arbol_nivel, skills['level'], lista_id)
        else:
            pareja_nivel = om.get(arbol_nivel, skills['level'])
            lista_id_nivel = me.getValue(pareja_nivel)
            lt.addLast(lista_id_nivel, skills['id'])
    
    mp.put(catalog['skills'],skills['id'],skills)

def add_jobs(catalog, data):
    mp.put(catalog['jobs'], data['id'], data)
    # Se crea un arbol, cuyas llaves son la fecha en la que se publicaron y sus valores son una lista de datos. 
    fecha = data['published_at']
    data['published_at'] = datetime.strptime(fecha, '%Y-%m-%dT%H:%M:%S.%fZ')
    if not om.contains(catalog['arbolFecha'], data['published_at']):
        lista_fecha = lt.newList('ARRAY_LIST')
        om.put(catalog['arbolFecha'], data['published_at'], lista_fecha)
    else:
        lista_fecha = me.getValue(om.get(catalog['arbolFecha'], data['published_at']))
    lt.addLast(lista_fecha, data)
    '''

    # Se crea un mapa,cuyas llaves son el pais, y sus valores son un diccionario cuyas cuyas llaves son los niveles de experticia y valores lista de datos
    pais = data['country_code']
    experticia_data = data['experience_level']
    if not mp.contains(catalog['mapaPais'], pais):
        experticia = {'junior': None,
                        'mid': None,
                        'senior': None,
                        'indeterminado': None
                        }
        experticia['junior'] = lt.newList('ARRAY_LIST')
        experticia['mid'] = lt.newList('ARRAY_LIST')
        experticia['senior'] = lt.newList('ARRAY_LIST')
        experticia['indeterminado'] = lt.newList('ARRAY_LIST')
        mp.put(catalog['mapaPais'], pais, experticia)
    
    paisLista = me.getValue(om.get(catalog['mapaPais'], pais))
    lt.addLast(paisLista[experticia_data], data)
    lt.addLast(paisLista['indeterminado'], data)
    
    # Mapa cuyas llaves son ciudades, y adentro se puede buscar en 3 categorias, todos, ubicacion, fechas:
    ciudad = data['city']
    work_type = data['workplace_type']
    if not mp.contains(catalog['mapaCiudad'], ciudad):
        fecha_ubicacion = {'fecha': None,
                           'ubicacion': None,
                           'todos': None
                           }
        fecha_ubicacion['fecha'] = om.newMap(omaptype='RBT',cmpfunction=compareDates)
        fecha_ubicacion['ubicacion'] = {'remote': None,
                                        'partly_remote': None,
                                        'office':None
                                        }
        fecha_ubicacion['ubicacion']['remote'] = lt.newList('ARRAY_LIST')
        fecha_ubicacion['ubicacion']['partly_remote'] = lt.newList('ARRAY_LIST')
        fecha_ubicacion['ubicacion']['office'] = lt.newList('ARRAY_LIST')
        
        fecha_ubicacion['todos'] = lt.newList()
        mp.put(catalog['mapaCiudad'], ciudad, fecha_ubicacion)
    mapa = me.getValue(mp.get(catalog['mapaCiudad'], ciudad))
    if not om.contains(mapa['fecha'], data['published_at']):
        lista_fecha_ciudad = lt.newList('ARRAY_LIST')
        om.put(mapa['fecha'], data['published_at'], lista_fecha_ciudad)
    else:
        lista_fecha_ciudad = me.getValue(om.get(mapa['fecha'], data['published_at']))
    lt.addLast(lista_fecha_ciudad, data)
    lt.addLast(mapa['ubicacion'][work_type], data)
    lt.addLast(mapa['todos'], data)
    
    #crear un arbol por tamaño de la empresa, si el tamaño es undefined este se categorizara con -1
    tamaño = data['company_size']
    empresa = data['company_name']
    if tamaño == 'Undefined':
        tamaño = -1
    else:
        tamaño = float(tamaño)
        
    if not om.contains(catalog['arbolTamaño'], tamaño):
        mapa_companys = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )
        om.put(catalog['arbolTamaño'], tamaño, mapa_companys)
    else:
        mapa_companys = me.getValue(om.get(catalog['arbolTamaño'], tamaño))
    
    if not mp.contains(mapa_companys, empresa):
        lista_empresa = lt.newList('ARRAY_LIST')
        mp.put(mapa_companys, empresa, lista_empresa)
    else:
        pareja_empresa = mp.get(mapa_companys, empresa)
        lista_empresa = me.getValue(pareja_empresa)
    lt.addLast(lista_empresa, data)
    '''
    
    
def convertirSalario(salario, moneda):
    if moneda == 'eur':
        salario = salario *1.07
    elif moneda == 'pln':
        salario = salario*0.25
    
    return salario


def add_employment_types(catalog, oferta):
    salario = oferta['salary_from']
    currency = oferta['currency_salary']
    
    if salario != '' and salario != ' ':
        oferta['salary_from'] = convertirSalario(float(salario), currency)
        oferta['currency_salary'] = 'usd'
        om.put(catalog['arbolSalary'], oferta['salary_from'], oferta['id'])
    mp.put(catalog['employment-types'], oferta['id'], oferta)

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
    valores = mp.keySet(data_structs)
    return lt.size(valores)

def req_1(catalog, initialDate, finalDate):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    initialDate = datetime.strptime(initialDate,'%Y-%m-%d')
    finalDate= datetime.strptime(finalDate, '%Y-%m-%d')
    lst = om.values(catalog["arbolFecha"], initialDate, finalDate)
    totjobs = 0
    for date in lt.iterator(lst):
        totjobs += lt.size(date)
        print(lt.size(date))
        
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
    elif (date1 < date2):
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


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
