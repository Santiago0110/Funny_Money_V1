import random
import copy
from collections import deque

from random import shuffle

cats = {
    'Ganar Dinero': ['A1','A2','A3','A4','A5','A6','A7','A8'],
    'Hacer Compras': ['B1','B2','B3','B4','B5','B6','B7','B8'],
    'Recompensas': ['C1','C2','C3','C4','C5','C6','C7','C8']     
}

str_opciones = {
    
'A1': """a) Ganar $130.000 b) $233.000 c) No hacer nada """,
'A2': """a) Ganar $5.000 b) $3.000 c) No hacer nada """,
'A3': """a) Ganar $95.500 b) $20.000 c) No hacer nada """,
'A4': """a) Ganar $37.000 b) $67.000 c) No hacer nada """,
'A5': """a) Ganar $39.000 b) $150.000 c) No hacer nada """,
'A6': """a) Ganar $5.000 b) $3.000 c) No hacer nada """,
'A7': """a) Ganar $28.000 b) $15.800 c) No hacer nada """,
'A8': """a) Ganar $80.000 b) $50.000 c) No hacer nada """,
'B1': """a) Comprar por $4.000 b) Comprar por $34.000 c) No hacer nada """,
'B2': """a) Comprar por $20.000 b) Comprar por $67.000 c) No hacer nada """,
'B3': """a) Comprar por $30.000 b) Comprar por $48.000 c) No hacer nada """,
'B4': """a) Comprar por $15.000 b) Comprar por $15.000 c) No hacer nada """,
'B5': """a) Comprar por $57.000 b) Comprar por $32.000 c) No hacer nada """,
'B6': """a) Comprar por $43.000 b) Comprar por $73.000 c) No hacer nada """,
'B7': """a) Comprar por $55.000 b) Comprar por $38.000 c) No hacer nada """,
'B8': """a) Comprar por $26.000 b) Comprar por $57.000 c) No hacer nada """,
'C1': """a) b) c) No hacer nada """,
'C2': """a) b) c) No hacer nada """,
'C3': """a) b) c) No hacer nada """,
'C4': """a) b) c) No hacer nada """,
'C5': """a) b) c) No hacer nada """,
'C6': """a) b) c) No hacer nada """,
'C7': """a) b) c) No hacer nada """,
'C8': """a) b) c) No hacer nada """,
} 

def mostrar_opcion_elegida(opt,dic):
  for i in dic.keys():
    if opt == i:
      opcion = dic[i]
      return opcion

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
        
# Inicia los jugadores
# Parte las opciones entre los dos jugadores
cats1={}
cats2={}

for k in cats:
  shuffle(cats[k])
  cats1[k]=cats[k][:4]
  cats2[k]=cats[k][4:]
  
jugador1 = Jugador(cats1,turnosxronda=3)
jugador2 = Jugador(cats2,turnosxronda=3)

for i in range(12):
    print("Turno",i+1, "  Ronda:",(i//3)+1, "  Etapa en la ronda:",(i%3)+1)

    opt_J1 = jugador1.getAction(i)
    print("\n--> Acción jugador 1:", opt_J1)
    str_opt_elegida = mostrar_opcion_elegida(opt_J1,str_opciones)
    print(str_opt_elegida)
    decision_J1 = input('Elige una opción: ')
    
    opt_J2 = jugador2.getAction(i)
    print("\n--> Acción jugador 2:", opt_J2)
    str_opt_elegida = mostrar_opcion_elegida(opt_J2,str_opciones)
    print(str_opt_elegida)
    decision_J2 = input('Elige una opción: ')

    print("--------------------------------------")