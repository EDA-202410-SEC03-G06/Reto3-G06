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
import matplotlib.pyplot as plt
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
import folium


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
               'mapaAño': None,
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
    
    catalog['arbolFecha'] = om.newMap(omaptype='RBT',cmpfunction=sort_criteria_salary)
    
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
    catalog['arbolTamaño'] = om.newMap(omaptype='RBT',cmpfunction=sort_criteria_salary)
    
    catalog['arbolSalary'] = om.newMap(omaptype='RBT',cmpfunction=sort_criteria_salary)
    
    catalog['mapaHabilidad'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )
    catalog['mapaAño'] = mp.newMap(100,
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
    nivel = int(skills['level'])
    if not mp.contains(catalog['mapaHabilidad'], habilidad):
        arbolNivel = om.newMap(omaptype='RBT',cmpfunction=sort_criteria_salary)
        mp.put(catalog['mapaHabilidad'], habilidad, arbolNivel)
    else:
        arbolNivel = me.getValue(om.get(catalog['mapaHabilidad'], habilidad))
    
    if not om.contains(arbolNivel, nivel):
        listaNivel = lt.newList('ARRAY_LIST')
        om.put(arbolNivel, nivel, listaNivel)
    else:
        listaNivel = me.getValue(om.get(arbolNivel, nivel))
    lt.addLast(listaNivel, skills['id'])
        
    mp.put(catalog['skills'],skills['id'],skills)

def add_jobs(catalog, data):
    
    #Agregar la categoria skill a los datos y agregarlos a catalog jobs
    data['skills'] = me.getValue(mp.get(catalog['skills'], data['id']))
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
        fecha_ubicacion = {'ubicacion': None,
                           'todos': None
                           }
        fecha_ubicacion['ubicacion'] = {}
        fecha_ubicacion['ubicacion']['remote'] = lt.newList('ARRAY_LIST')
        fecha_ubicacion['ubicacion']['partly_remote'] = lt.newList('ARRAY_LIST')
        fecha_ubicacion['ubicacion']['office'] = lt.newList('ARRAY_LIST')
        
        fecha_ubicacion['todos'] = lt.newList('ARRAY_LIST')
        mp.put(catalog['mapaCiudad'], ciudad, fecha_ubicacion)
    mapa = me.getValue(mp.get(catalog['mapaCiudad'], ciudad))
    
    lt.addLast(mapa['ubicacion'][work_type], data)
    lt.addLast(mapa['todos'], data)
    
    #crear un arbol por tamaño de la empresa, si el tamaño es undefined este se categorizara con -1
    tamaño = data['company_size']
    
    if tamaño == 'Undefined':
        tamaño = -1
    else:
        tamaño = float(tamaño)
        
    if not om.contains(catalog['arbolTamaño'], tamaño):
        lista_companys = lt.newList('ARRAY_LIST')
        om.put(catalog['arbolTamaño'], tamaño, lista_companys)
    else:
        lista_companys = me.getValue(om.get(catalog['arbolTamaño'], tamaño))
    
    lt.addLast(lista_companys, data['id'])
    
    #mapa por años, que va a dividirse dentro en nivel de experiencia, habilidades, o ubicación.
    anio = int(datetime.strftime(data['published_at'], '%Y'))
    if not mp.contains(catalog['mapaAño'], anio):
        paises = mp.newMap(100,
                        maptype='CHAINING',
                        loadfactor=4,
                        cmpfunction=sort_criteria
                        )
        mp.put(catalog['mapaAño'], anio, paises)
        mp.put(paises, 'total', 0)
    mapaAño = me.getValue(mp.get(catalog['mapaAño'], anio))
    parejaTotal = mp.get(mapaAño, 'total')
    total = me.getValue(parejaTotal)
    total += 1
    me.setValue(parejaTotal, total)
    if not mp.contains(mapaAño, pais):
        categorias = {'experiencia': None,
                      'ubicacion': None,
                      'habilidad': None
                      }
        categorias['habilidad'] = mp.newMap(51,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   cmpfunction=sort_criteria
                                   )
        
        experticia = mp.newMap(7,
                                maptype='PROBING',
                                loadfactor=0.5,
                                cmpfunction=sort_criteria
                                   )
        junior = lt.newList('ARRAY_LIST')
        mid = lt.newList('ARRAY_LIST')
        senior = lt.newList('ARRAY_LIST')
        mp.put(experticia, 'junior', junior)
        mp.put(experticia, 'mid', mid)
        mp.put(experticia, 'senior', senior)
        
        categorias['experiencia'] = experticia
        
        categorias['todas'] = lt.newList('ARRAY_LIST')
        
        categorias['ubicacion'] = mp.newMap(1000,
                                            maptype='CHAINING',
                                            loadfactor=4,
                                            cmpfunction=sort_criteria
                                            )
        remote = lt.newList('ARRAY_LIST')
        partly_remote = lt.newList('ARRAY_LIST')
        office = lt.newList('ARRAY_LIST')
        mp.put(categorias['ubicacion'], 'remote', remote)
        mp.put(categorias['ubicacion'], 'partly_remote', partly_remote)
        mp.put(categorias['ubicacion'], 'office', office)
        mp.put(mapaAño, pais, categorias)
    else:
        categorias = me.getValue(mp.get(mapaAño, pais))
    lt.addLast(me.getValue(mp.get(categorias['experiencia'], experticia_data)), data)
    lt.addLast(me.getValue(mp.get(categorias['ubicacion'], work_type)), data)
    
    skill = me.getValue(mp.get(catalog['skills'], data['id']))
    if not mp.contains(categorias['habilidad'], skill['name']):
        lista_skill = lt.newList('ARRAY_LIST')
        mp.put(categorias['habilidad'], skill['name'], lista_skill)
    else:
        lista_skill = me.getValue(mp.get(categorias['habilidad'], skill['name']))
    lt.addLast(lista_skill, data)  
    
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
        oferta['salary_from'] = round(convertirSalario(float(salario), currency),2)
        oferta['currency_salary'] = 'usd'
    else:
        oferta['salary_from'] = -1
        oferta['currency_salary'] = "N/A"
    skills = me.getValue(mp.get(catalog['skills'], oferta['id']))
    parejaId = mp.get(catalog['jobs'], oferta['id'])
    datos_oferta = me.getValue(parejaId)
    datos_oferta['salary_from'] = oferta['salary_from']
    datos_oferta['skills'] = skills['name']
    if not om.contains(catalog['arbolSalary'], oferta['salary_from']):
        listaSalario = lt.newList('ARRAY_LIST')
        om.put(catalog['arbolSalary'], oferta['salary_from'], listaSalario)
    else:
        listaSalario = me.getValue(om.get(catalog['arbolSalary'], oferta['salary_from']))
    if oferta['salary_from'] == -1:
        oferta['salary_from'] = 'UNKNOWN'
    lt.addLast(listaSalario, datos_oferta)

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
    lst = om.values(catalog["arbolFecha"], initialDate, finalDate)
    
    totjobs = 0
    for date in lt.iterator(lst):
        totjobs += lt.size(date)
        
        
    return totjobs, lst


def req_2(catalog, minSalary, maxSalary):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    lst = om.values(catalog['arbolSalary'], minSalary, maxSalary)
    totjobs = 0
    for salary in lt.iterator(lst):
        totjobs += lt.size(salary)
   
    return totjobs, lst
    

def req_3(data_structs, n, pais, exp):
    """
    Función que soluciona el requerimiento 3
    """
    catalog = data_structs['mapaPais']
    ofertas = lt.newList("ARRAY_LIST")
    ofertas_filtro = lt.newList('ARRAY_LIST')
    emptype = data_structs['employment-types']
    skills = data_structs['skills']
    
    pareja = mp.get(catalog,pais)
    val_pais = me.getValue(pareja)
    valores = val_pais[exp]
    count = 1
    merg.sort(valores,compare)

    for ele in lt.iterator(valores):
        if count >n:
            break
        else:
            lt.addLast(ofertas,ele)
            count+=1
    
    for oferta in lt.iterator(ofertas):
        pareja_emp = mp.get(emptype,oferta['id'])
        oferta_emp = me.getValue(pareja_emp)
        pareja_skill = mp.get(skills,oferta['id'])
        oferta_skill = me.getValue(pareja_skill)
        datos = {'Date':oferta['published_at'],'Title':oferta['title'],'Company_name':oferta['company_name'],
                 'Experience':oferta['experience_level'],'Country':oferta['country_code'],'City':oferta['city'],
                 'Company Size':oferta['company_size'],'Workplace':oferta['workplace_type'],
                 'Salary':oferta_emp['salary_from'],'Skill':oferta_skill['name']}
        lt.addLast(ofertas_filtro,datos)
    return (lt.size(valores),ofertas_filtro)

    


def req_4(data_structs,n,ciudad,workplace):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    catalog = data_structs['mapaCiudad']
    ofertas = lt.newList("ARRAY_LIST")
    ofertas_filtro = lt.newList('ARRAY_LIST')
    emptype = data_structs['employment-types']
    skills = data_structs['skills']    
    
    pareja = mp.get(catalog,ciudad)
    val_pais = me.getValue(pareja)
    valores = val_pais[workplace]
    
    count = 1
    merg.sort(valores,compare)
    for ele in lt.iterator(valores):
        if count > n:
            break
        else:
            lt.addLast(ofertas,ele)
            
    for oferta in lt.iterator(ofertas):
        pareja_emp = mp.get(emptype,oferta['id'])
        oferta_emp = me.getValue(pareja_emp)
        pareja_skill = mp.get(skills,oferta['id'])
        oferta_skill = me.getValue(pareja_skill)
        datos = {'Date':oferta['published_at'],'Title':oferta['title'],'Company_name':oferta['company_name'],
                 'Experience':oferta['experience_level'],'Country':oferta['country_code'],'City':oferta['city'],
                 'Company Size':oferta['company_size'],'Workplace':oferta['workplace_type'],
                 'Salary':oferta_emp['salary_to'],'Skill':oferta_skill['name']}
        lt.addLast(ofertas_filtro,datos)
    return (lt.size(valores),ofertas_filtro)
    


def req_5(catalog, n, minSize, maxSize, skill, minLevel, maxLevel):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    filtroSize = mp.newMap()
    filtroSkill = mp.newMap()
    jobs = catalog['jobs']
    skills = catalog['mapaHabilidad']
    size = catalog['arbolTamaño']
    sizeRango = om.values(size, minSize, maxSize)
    
    habilidad = me.getValue(mp.get(skills, skill))
    habilidadRango = om.values(habilidad, minLevel, maxLevel)
    
    #pasar los valores de listas a un diccionario con todos los valores que contienen
    for tamaño in lt.iterator(sizeRango):
        for idJob in lt.iterator(tamaño):
            ofertaJob = me.getValue(mp.get(jobs, idJob))
            mp.put(filtroSize, idJob, ofertaJob)
    
    for hab in lt.iterator(habilidadRango):
        for idSkill in lt.iterator(hab):
            ofertaSkill = me.getValue(mp.get(jobs, idSkill))
            mp.put(filtroSkill, idSkill, ofertaSkill)
    #Comparar los dos mapas y si esta la oferta en ambos lo añade a ofertasFiltro y filtrar por los datos a presentar
    habilidades = mp.keySet(filtroSkill)
    ofertasFiltro = lt.newList('ARRAY_LIST')
    for skillId in lt.iterator(habilidades):
        if mp.contains(filtroSize, skillId):
            oferta = me.getValue(mp.get(filtroSize, skillId))
            datos = {'Date':oferta['published_at'],'Title':oferta['title'],'Company_name':oferta['company_name'],
                 'Experience':oferta['experience_level'],'Country':oferta['country_code'],'City':oferta['city'],
                 'Company Size':oferta['company_size'],'Workplace':oferta['workplace_type'],
                 'Salary':oferta['salary_from'],'Skill': skill}
            lt.addLast(ofertasFiltro, datos)
            
    tamaño = lt.size(ofertasFiltro)
    conteo = 0
    oferta_final = lt.newList('ARRAY_LIST')
    for offer in lt.iterator(ofertasFiltro):
        lt.addLast(oferta_final, offer)
        conteo +=1
        if conteo == n:
            break
        
    return tamaño, oferta_final
    
def req_6(catalog,n,fecha_in,fecha_fin,sal_min:float,sal_max:float):
    """
    Función que soluciona el requerimiento 6
    """
    emptype = catalog['employment-types']
    skills = catalog['skills']
    ofertas = lt.newList("ARRAY_LIST")
    salarios = mp.newMap()
    ciudades = mp.newMap()
    n_ciudades = lt.newList("ARRAY_LIST")
    ofertas_ciudad = lt.newList('ARRAY_LIST')
    
    #filtrar los datos
    lst = om.values(catalog["arbolFecha"], fecha_in, fecha_fin)
    lst_salario = om.values(catalog['arbolSalary'],sal_min,sal_max)
    for value in lt.iterator(lst_salario):
        for oferta in lt.iterator(value):
            mp.put(salarios,oferta['id'],oferta)
    
    for lista in lt.iterator(lst):
        for oferta in lt.iterator(lista):
            ispresent =mp.contains(salarios,oferta['id'])
            if ispresent:
                lt.addLast(ofertas,oferta)
        #crear una lista de ofertas por ciudad
           
            incitylist = mp.contains(ciudades,oferta['city'])
            if incitylist==False:
                mp.put(ciudades,oferta['city'], 1)
            elif incitylist:
                valor = mp.get(ciudades,oferta['city'])
                cant = me.getValue(valor)
                cant +=1
                me.setValue(valor,cant)
    #fin filtro

    #Ordenar las ciudades y filtrar a n
    city_list = mp.keySet(ciudades)
    ordered_city = lt.newList('ARRAY_LIST')
    for city in lt.iterator(city_list):
        pareja = mp.get(ciudades,city)  
        valor = me.getValue(pareja)
        lt.addLast(ordered_city,{'city':city,'count':valor})
    merg.sort(ordered_city,sort_criteria_req6)  

    for city in lt.iterator(ordered_city):
        if lt.size(n_ciudades)<n:
            lt.addLast(n_ciudades,city['city'])
        else:
            break
    ciudad_1 = lt.firstElement(n_ciudades)
    merg.sort(n_ciudades,sort)
    
    #crear el formato para la lista
    
    merg.sort(ofertas,compare)
    for oferta in lt.iterator(ofertas):
        if oferta['city']==ciudad_1:
            pareja_emp = mp.get(emptype,oferta['id'])
            oferta_emp = me.getValue(pareja_emp)
            pareja_skill = mp.get(skills,oferta['id'])
            oferta_skill = me.getValue(pareja_skill)
            datos = {'Date':oferta['published_at'],'Title':oferta['title'],'Company_name':oferta['company_name'],
                     'Experience':oferta['experience_level'],'Country':oferta['country_code'],'City':oferta['city'],
                     'Company Size':oferta['company_size'],'Workplace':oferta['workplace_type'],
                     'Salary':oferta_emp['salary_to'],'Skill':oferta_skill['name']}
            lt.addLast(ofertas_ciudad,datos)


    return (lt.size(ofertas),lt.size(city_list),n_ciudades,(ciudad_1,ofertas_ciudad))
    
    
        
     
    


def req_7(catalog, año, pais, conteo):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    años = catalog['mapaAño']
    paisesAño= me.getValue(mp.get(años, año))
    totalOfertas = me.getValue(mp.get(paisesAño,'total'))
    paisConteos =me.getValue(mp.get(paisesAño, pais))
    tipoConteo = paisConteos[conteo]
    
    filtro = lt.newList('ARRAY_LIST')
    
    ejes = mp.keySet(tipoConteo)
    valores = []
    llaves = []
    valor_min = 30040602
    valor_max = 0
    total = 0
    for key in lt.iterator(ejes):
        
        llaves.append(key)
        valor = lt.size(me.getValue(mp.get(tipoConteo, key)))
        
        valores.append(valor)
        if valor > valor_max:
            valor_max = valor
        if valor < valor_min:
            valor_min = valor
        total += valor
    plt.bar(llaves, valores, color='blue')
    if conteo == 'experiencia':
        plt.xlabel('Niveles de experiencia')
    else:
        plt.xlabel(conteo+'es')
    
    plt.ylabel('Valores')
    plt.title('Grafica de barras para '+ conteo+ ' en el año '+ str(año))
    plt.show()
    
    return totalOfertas, total, valor_min, valor_max, tipoConteo
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
    if data_1['published_at']>data_2['published_at']:
        return True
    elif data_1['published_at']<data_2['published_at']:
        False
    else:
        return data_1['id']>data_2['id']
    pass

# Funciones de ordenamiento

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
    

def sort_criteria_date(date1, date2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    dateentry = date1
    datecurrent = date2   
    if dateentry == datecurrent:
        return 0
    elif datecurrent > dateentry:
        return 1
    else:
        return -1
    
def sort_criteria_salary(salary1, salary2):
    
    if salary1 == salary2:
        return 0
    elif salary1 > salary2:
        return 1
    else:
        return -1

def sort(data_1,data_2):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    return data_1<data_2

def sort_criteria_req6(data_1,data_2):
    return data_1['count']>data_2['count']

def sort_criteria_req5(data1, data_2):
    
    fecha1 = data1['Date']
    fecha2 = data_2['Date']
    
    if fecha1 == fecha2:
        return 0
    elif fecha1> fecha2:
        return -1
    else:
        return 1