# -*- coding: utf-8 -*-
"""-----------------------------
LIBRERÍAS Y VARIABLES GLOBALES
-----------------------------"""
from tqdm.auto import tqdm
msn_serial = ''
depoIni = 20000

# Lista de categorías
cats = ['Ganar Dinero', 'Hacer Compras', 'Recompensas']

#Lista de opciones por categoría
ganarDinero = ['A1','A2','A3','A4','A5','A6','A7','A8']
hacerCompras = ['B1','B2','B3','B4','B5','B6','B7','B8']
recompensas = ['C1','C2','C3','C4','C5','C6','C7','C8']

"""-----------------------------
DECLARACIÓN CLASE JUGADOR
-----------------------------"""
class Jugador(object):
    
  """-----------------------------------
  Método Constructor de la Clase Jugador
  -----------------------------------"""

  def __init__(self):
    #self.depositoInicial = depositoInicial
    self.ingresos = []
    self.egresos = []
    self.ahorros = []
    self.totalIngresos = 0
    self.totalEgresos = 0
    self.totalAhorros = 0
    self.saldoParcial = 0
    self.saldoTotal = 0

  """-----------------------------------
  Métodos principales para los jugadores
  -----------------------------------"""
  
  def depositoInicial(self,valor):
    self.ingresos.append(valor)    

  def ganarDinero(self,valor):
    self.ingresos.append(valor)

  def hacerCompras(self,valor):
    self.egresos.append(valor)

  def ahorrarDinero(self,valor,porcentaje):
    porcentaje_ahorro = (porcentaje * valor) / 100
    self.ahorros.append(porcentaje_ahorro)
    self.egresos.append(porcentaje_ahorro)

  def calcularTotalIngresos(self):
    self.totalIngresos = sum(self.ingresos)
    return self.totalIngresos

  def calcularTotalEgresos(self):
    self.totalEgresos = sum(self.egresos)
    return self.totalEgresos

  def calcularTotalAhorros(self):
    self.totalAhorros = sum(self.ahorros)
    return self.totalAhorros

  def calcularSaldoTotal(self):
    self.saldoTotal = sum(self.ingresos) - sum(self.egresos)
    return self.saldoTotal

"""-----------------------------
DECLARACIÓN CLASE BANCO
-----------------------------"""
class Banco(object):

    """---------------------------------
    Método Constructor de la Clase Banco
    ---------------------------------"""

    def __init__(self):
        self.entradas = []
        self.salidas = []
        self.totalEntradas = 0
        self.totalSalidas = 0
        self.saldoInicial = 200000
        self.saldoTotal = 0

    """-----------------------------------------
    Métodos principales para el manejo de dinero
    -----------------------------------------""" 

    # Variable: "salidas" ; se ejecuta cuando inicia el juego
    def asignarDineroInicial(self,valor):
        self.salidas.append(valor)
        return valor

    # Variable: "entradas" ; se ejecuta cada vez que un jugador hace una compra
    def recibirDinero(self,valor):
        self.entradas.append(valor)
        return valor
    
    # Variable: "salidas" ; se ejecuta cada vez que un jugador gana dinero   
    def entregarDinero(self,valor):
        self.salidas.append(valor)
        return valor
    
    def calcularTotalEntradas(self):
        self.totalEntradas = sum(self.entradas)
        return self.totalEntradas
    
    def calcularTotalSalidas(self):
        self.totalSalidas = sum(self.salidas)
        return self.totalSalidas
    
    def calcularSaldoTotal(self):
        self.saldoTotal = self.saldoInicial + sum(self.entradas) - sum(self.salidas)
        return self.saldoTotal 

"""--------------------------
FUNCIÓN ENCENDER
--------------------------"""
def encender():
    
  print('BIENVENIDOS A FUNNY MONEY'+'\n')
  
  #for i in tqdm(range(10001)):
  #  print(" ", end = '\r')
      
  print('\n'+'RP to Arduino -->')
  msn_serial = 'READY_ON'
  print(msn_serial)
  
  input('Bienvenido a Funny Money'+'\n'+'Presiona el botón para empezar: ')

"""--------------------------
FUNCIÓN ELEGIR CATEGORÍA
--------------------------"""
# Retorna el nombre de la categoría elegida
def elegirCat(lista):
    pass

"""-------------------------------
FUNCIÓN ELEGIR OPCIÓN DE CATEGORÍA
-------------------------------"""
# Retorna una opción de la lista elegida
def elegirOpcCat(cat):
  pass

"""--------------------------
FUNCIÓN MAIN (PRINCIPAL)
--------------------------"""
if __name__ == '__main__':
    
    encender()
    
    # Instancia de objetos
    J1 = Jugador()
    J2 = Jugador()
    banco = Banco()
    
    # Deposito Inicial
    banco.asignarDineroInicial(depoIni)
    J1.depositoInicial(depoIni)
    banco.asignarDineroInicial(depoIni)
    J2.depositoInicial(depoIni)
    
    # Imprime saldo inicial de cada jugador
    print('\n' + 'DEPÓSITO INICIAL:')
    print('J1 = $' + str(J1.calcularSaldoTotal()))
    print('J2 = $' + str(J2.calcularSaldoTotal()))
    
    