import random
import copy
from collections import deque

from random import shuffle

cats = {
    'Ganar Dinero': ['A1','A2','A3','A4','A5','A6','A7','A8'],
    'Hacer Compras': ['B1','B2','B3','B4','B5','B6','B7','B8'],
    'Recompensas': ['C1','C2','C3','C4','C5','C6','C7','C8']     
}


class Jugador(object):
    
    def __init__(self, categorias, turnosxronda=3):
        self.turnosxronda = turnosxronda
        self.categorias = copy.deepcopy(categorias)
        total_turnos=0
        cat =[]
        for k in categorias:
            # Baraja las acciones de cada categoría
            shuffle(self.categorias[k])
            total_turnos+=len(self.categorias[k])
            cat.append(k)
            
        
        self.rondasxcategoria = []
        for ironda in range(total_turnos//turnosxronda):
            temp = cat[:]
            shuffle(temp)
            self.rondasxcategoria +=temp 
        
    def getAction(self, numeroTurno):
        ronda = numeroTurno//self.turnosxronda
        categoria = self.rondasxcategoria[numeroTurno]
        action = self.categorias[categoria][ronda]
        return action
        

#Inicia los jugadores
# parte las opciones entre los dos jugadores
cats1={}
cats2={}
for k in cats:
  shuffle(cats[k])
  cats1[k]=cats[k][:4]
  cats2[k]=cats[k][4:]
jugador1 = Jugador(cats1,turnosxronda=3)
jugador2 = Jugador(cats2,turnosxronda=3)
for i in range(12):
    print("\nTurno",i+1, "  Ronda:",(i//3)+1, "  Etapa en la ronda:",(i%3)+1)
    print("    Acción jugador 1:", jugador1.getAction(i))
    print("    Acción jugador 2:", jugador2.getAction(i))