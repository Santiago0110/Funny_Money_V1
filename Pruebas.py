# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:47:11 2022

@author: LASSODS
"""

"""------------------------------------------------------
LIBRERÍAS IMPORTADAS
------------------------------------------------------"""
import random
import copy
from collections import deque

"""------------------------------------------------------
DECLARACIÓN DE VARIABLES
------------------------------------------------------"""
cont_turno = 0
turno = deque([1,2])

cats = {
    'Ganar Dinero': ['A1','A2','A3','A4','A5','A6','A7','A8'],
    'Hacer Compras': ['B1','B2','B3','B4','B5','B6','B7','B8'],
    'Recompensas': ['C1','C2','C3','C4','C5','C6','C7','C8']     
}

cats2 = copy.deepcopy(cats)

"""------------------------------------------------------
DECLARACÍÓN DE FUNCIONES
------------------------------------------------------"""
def select_cat(opciones):
    opciones = opciones
    while True:
        r = random.choice(opciones)
        opciones.remove(r)
        yield r

def removeOption(d,key,opt):
    r = dict(d)
    del r[key][opt]
    return r

def rotar_turno():
	turno.rotate()
	return turno[0]

"""------------------------------------------------------
PROGRAMA PRINCIPAL
------------------------------------------------------"""
if __name__ == '__main__':
    
    # Indica a qué jugador le corresponde el turno
    jugador = rotar_turno()
    
    if jugador == 2:    
        categorias = list(cats2.keys())
        
        while cont_turno < 3:
       
            select = select_cat(categorias)
            cat_selected = next(select)
            
            opt_selected = random.choice(cats[cat_selected])
            index_opt = cats[cat_selected].index(opt_selected)
            
            removeOption(cats2,cat_selected,index_opt)
            cont_turno+=1

"""
Código que elige una opción de una lista al random
y la guarda en una variable SIN REPETIR
"""
# import random

# def aleatorio(opciones):
#     opciones = opciones
#     while True:
#         r = random.choice(opciones)
#         opciones.remove(r)
#         yield r

# a = ['Ganar Dinero','Hacer Compras','Recompensas']
# gen = aleatorio(a)

# L1 = next(gen)
# L2 = next(gen)
# L3 = next(gen)

"""
Código para rotar turnos de jugador
"""

# from collections import deque
 
# turno = deque(["1", "2"])
# cont = 0

# def rotar_turno():
# 	turno.rotate()
# 	return turno[0]

# while cont <= 10:
#     jugador = rotar_turno()
#     print(jugador)
#     cont+=1