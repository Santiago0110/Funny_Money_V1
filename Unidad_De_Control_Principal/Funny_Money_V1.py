# -*- coding: utf-8 -*-
"""-----------------------------
LIBRERÍAS Y VARIABLES GLOBALES
-----------------------------"""
import copy
from random import shuffle

# Valor de dinero inicial
depoIni = 100000

# Diccionario princial de categorías y opciones/categoria
cats = {
    'Ganar Dinero': ['A1','A2','A3','A4','A5','A6','A7','A8'],
    'Hacer Compras': ['B1','B2','B3','B4','B5','B6','B7','B8'],
    'Recompensas': ['C1','C2','C3','C4','C5','C6','C7','C8']     
}

# String de todas las opciones
str_opciones = {
    
'A1': """a) Ganar $130.000 b) Ganar $233.000 c) No hacer nada """,
'A2': """a) Ganar $45.000 b) Ganar $63.000 c) No hacer nada """,
'A3': """a) Ganar $95.500 b) Ganar $20.000 c) No hacer nada """,
'A4': """a) Ganar $37.000 b) Ganar $67.000 c) No hacer nada """,
'A5': """a) Ganar $39.000 b) Ganar $150.000 c) No hacer nada """,
'A6': """a) Ganar $75.000 b) Ganar $59.000 c) No hacer nada """,
'A7': """a) Ganar $28.000 b) Ganar $15.800 c) No hacer nada """,
'A8': """a) Ganar $80.000 b) Ganar $50.000 c) No hacer nada """,

'B1': """a) Comprar por $26.000 b) Comprar por $44.000 c) No hacer nada """,
'B2': """a) Comprar por $20.000 b) Comprar por $67.000 c) No hacer nada """,
'B3': """a) Comprar por $30.000 b) Comprar por $48.000 c) No hacer nada """,
'B4': """a) Comprar por $15.000 b) Comprar por $15.000 c) No hacer nada """,
'B5': """a) Comprar por $57.000 b) Comprar por $32.000 c) No hacer nada """,
'B6': """a) Comprar por $43.000 b) Comprar por $73.000 c) No hacer nada """,
'B7': """a) Comprar por $55.000 b) Comprar por $38.000 c) No hacer nada """,
'B8': """a) Comprar por $26.000 b) Comprar por $57.000 c) No hacer nada """,

'C1': """a) Aceptar reto b) No aceptar""",
'C2': """a) Aceptar reto b) No aceptar""",
'C3': """a) Aceptar reto b) No aceptar""",
'C4': """a) Aceptar reto b) No aceptar""",
'C5': """a) Aceptar reto b) No aceptar""",
'C6': """a) Aceptar reto b) No aceptar""",
'C7': """a) Aceptar reto b) No aceptar""",
'C8': """a) Aceptar reto b) No aceptar""",
} 
"""-----------------------------------------------------
Función que evalúa la decisión de un jugador
-----------------------------------------------------"""
#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
def ahorrar(jugador,valor):
    jugador.ahorrarDinero(valor,10)
    
def evaluar_opcion_elegida(jugador,opcion,decision):

    if opcion == 'A1':

        if decision == 'a':
            # Valor: $130.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 130000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
            
    
        if decision == 'b':     
            # Valor: $233.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 233000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'c':
            pass
        
    elif opcion == 'A2':

        if decision == 'a':
            # Valor: $45.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 45000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'b':     
            # Valor: $63.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 63000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'c':
            pass
        
    if opcion == 'A3':

        if decision == 'a':
            # Valor: $95.500 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 95500
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'b':     
            # Valor: $20.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 20000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'c':
            pass
        
    if opcion == 'A4':

        if decision == 'a':
            # Valor: $37.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 37000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'b':     
            # Valor: $67.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 67000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'c':
            pass
        
    if opcion == 'A5':

        if decision == 'a':
            # Valor: $39.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 39000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'b':     
            # Valor: $150.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 150000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'c':
            pass
        
    if opcion == 'A6':

        if decision == 'a':
            # Valor: $75.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 75000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'b':     
            # Valor: $59.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 59000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'c':
            pass
        
    if opcion == 'A7':

        if decision == 'a':
            # Valor: $28.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 28000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'b':     
            # Valor: $15.800 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 15800
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'c':
            pass
        
    if opcion == 'A8':

        if decision == 'a':
            # Valor: $80.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 80000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'b':     
            # Valor: $50.000 --> El banco ENTREGAR y el jugador GANAR
            cantidad = 50000
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            
            if var_save == 'a':
                ahorrar(jugador,cantidad)
            else:
                pass
    
        if decision == 'c':
            pass

    elif opcion == 'B1':
        
        if decision == 'a':
            # Valor: $26.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 26000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'b':             
            # Valor: $44.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 44000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'c':
            pass
        
    elif opcion == 'B2':
        
        if decision == 'a':
            # Valor: $20.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 20000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'b':             
            # Valor: $67.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 67000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'c':
            pass
        
    elif opcion == 'B3':
        
        if decision == 'a':
            # Valor: $30.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 30000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'b':             
            # Valor: $48.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 48000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'c':
            pass
        
    elif opcion == 'B4':
        
        if decision == 'a':
            # Valor: $15.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 15000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'b':             
            # Valor: $15.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 15000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'c':
            pass
        
    elif opcion == 'B5':
        
        if decision == 'a':
            # Valor: $57.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 57000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'b':             
            # Valor: $32.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 32000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'c':
            pass
        
    elif opcion == 'B6':
        
        if decision == 'a':
            # Valor: $43.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 43000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'b':             
            # Valor: $73.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 73000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'c':
            pass
        
    elif opcion == 'B7':
        
        if decision == 'a':
            # Valor: $55.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 55000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'b':             
            # Valor: $38.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 38000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'c':
            pass
        
    elif opcion == 'B8':
        
        if decision == 'a':
            # Valor: $26.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 26000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'b':             
            # Valor: $57.000 --> El banco RECIBIR y el jugador GASTAR
            cantidad = 57000
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
    
        if decision == 'c':
            pass
#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
"""-----------------------------------------------------
Función que muestra los resultados finales el juego
-----------------------------------------------------"""
def mostrarResultados():
    print('FIN DEL JUEGO')
    print('--------------------')
    
    print('ENTRADAS Y SALIDAS:')
    print('--------------------')
    J1_ingresos = J1.calcularTotalIngresos()
    J2_ingresos = J2.calcularTotalIngresos()
    J1_egresos = J1.calcularTotalEgresos()
    J2_egresos = J2.calcularTotalEgresos()
    print('El JUGADOR 1 ganó: ${:,.2f}'.format(J1_ingresos).replace(".", ",").replace("@", ".") + ' y gastó: ${:,.2f}'.format(J1_egresos).replace(".", ",").replace("@", "."))
    print('El JUGADOR 2 ganó: ${:,.2f}'.format(J2_ingresos).replace(".", ",").replace("@", ".") + ' y gastó: ${:,.2f}'.format(J2_egresos).replace(".", ",").replace("@", "."))
    print('--------------------')    
    print('SALDOS TOTALES:')
    print('--------------------')
    J1_saldo = J1.calcularSaldoTotal()
    J2_saldo = J2.calcularSaldoTotal()
    print('El saldo total del JUGADOR 1 es: ${:,.2f}'.format(J1_saldo).replace(".", ",").replace("@", "."))
    print('El saldo total del JUGADOR 2 es: ${:,.2f}'.format(J2_saldo).replace(".", ",").replace("@", "."))
    print('--------------------')    
    print('TOTAL AHORROS:')
    print('--------------------')
    J1_ahorros = J1.calcularTotalAhorros()
    J2_ahorros = J2.calcularTotalAhorros()
    print('El JUGADOR 1 ahorró: ${:,.2f}'.format(J1_ahorros).replace(".", ",").replace("@", "."))
    print('El JUGADOR 2 ahorró: ${:,.2f}'.format(J2_ahorros).replace(".", ",").replace("@", "."))
    
    
"""-----------------------------------------------------
Función que muestra el String de la opción seleccionada
-----------------------------------------------------"""
def mostrar_opcion_elegida(opt,dic):
  for i in dic.keys():
    if opt == i:
      opcion = dic[i]
      return opcion
"""-----------------------------
DECLARACIÓN CLASE RONDA JUGADOR
-----------------------------"""
class RondaJugador(object):
    
    """-----------------------------------------
    Método Constructor de la Clase Ronda Jugador
    -----------------------------------------"""
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
        self.saldoInicial = 2000000
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
      
  print('\n'+'RP to Arduino -->')
  msn_serial = 'READY_ON'
  print(msn_serial)
  
  input('Bienvenido a Funny Money'+'\n'+'Presiona el botón para empezar: ')

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
    
    # Inicia el juego
    print('\n' + 'INICIO DE JUEGO:')
    
    # Inicia los jugadores
    # Parte las opciones entre los dos jugadores
    cats1={}
    cats2={}
    
    for k in cats:
      shuffle(cats[k])
      cats1[k]=cats[k][:4]
      cats2[k]=cats[k][4:]
      
    jugador1 = RondaJugador(cats1,turnosxronda=3)
    jugador2 = RondaJugador(cats2,turnosxronda=3)
    
    """--------------------------
    LOOP DE RONDAS DE JUEGO
    --------------------------"""
    for i in range(12):
        print("Turno",i+1, "  Ronda:",(i//3)+1, "  Etapa en la ronda:",(i%3)+1)
    
        # Elige una opción para J1
        opt_J1 = jugador1.getAction(i)
        print("\n--> Acción jugador 1:", opt_J1)
        str_opt_elegida = mostrar_opcion_elegida(opt_J1,str_opciones)
        print(str_opt_elegida)
        decision_J1 = input('Elige una opción: ')
        evaluar_opcion_elegida(J1,opt_J1,decision_J1)
        
        # Actualizar saldo de banco y jugador
        banco.calcularSaldoTotal()
        J1.calcularSaldoTotal()
    
        # Elige una opción para J2
        opt_J2 = jugador2.getAction(i)
        print("\n--> Acción jugador 2:", opt_J2)
        str_opt_elegida = mostrar_opcion_elegida(opt_J2,str_opciones)
        print(str_opt_elegida)
        decision_J2 = input('Elige una opción: ')
        evaluar_opcion_elegida(J2,opt_J2,decision_J2)
        
        # Actualizar saldo de banco y jugador
        banco.calcularSaldoTotal()
        J2.calcularSaldoTotal()
    
        print("--------------------------------------")   
        
    mostrarResultados()
