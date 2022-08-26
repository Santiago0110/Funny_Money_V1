# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:22:56 2022

@author: usuario
"""

import random 

cats = {
    'Ganar Dinero': ['A1','A2','A3','A4','A5','A6','A7','A8'],
    'Hacer Compras': ['B1','B2','B3','B4','B5','B6','B7','B8'],
    'Recompensas': ['C1','C2','C3','C4','C5','C6','C7','C8']     
}

# Seleccionar el nombre de una categoría al random
cat_chosen = random.choice(list(cats.keys()))
print(cat_chosen)

# Seleccionar una opción dentro de una categoría
opt_chosen = random.choice(cats[cat_chosen][:])
print(opt_chosen)


"""
for key in categorias.keys():
    print(key)

print('\n')

for value in categorias.values():
    print(value)

print('\n')
    
for key,value in categorias.items():
    print(key,'-',value)
"""