"""-------------------------------------------------
Librerías importadas de Python
-------------------------------------------------"""
import serial
import time
import copy
from random import shuffle
"""-------------------------------------------------
DECLARACIÓN DE VARIABLES GLOBALES
-------------------------------------------------"""
# Cantidad de dinero inicial
depoIni = 100000

# Diccionario princial de categorías y opciones/categoria
cats = {
    'Ganar Dinero': ['A1','A2','A3','A4','A5','A6','A7','A8'],
    'Hacer Compras': ['B1','B2','B3','B4','B5','B6','B7','B8'],
    'Recompensas': ['C1','C2','C3','C4','C5','C6','C7','C8']     
}

"""-------------------------------------------------
Configuración de puerto serial Raspberry - Arduino
-------------------------------------------------"""
#nombre del dispositivo serial : dmesg | grep -v disconnect | grep -Eo "tty(ACM|USB)." | tail -1
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.flushInput()

"""----------------------
DECLARACIÓN CLASE JUGADOR
----------------------"""
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

def leer_serial():
    lineBytes = ser.readline() #lee los datos del arduino
    line = lineBytes.decode('latin-1').strip()
    print(line)
    return line

def escribir_serial(l):
    l2 = l.encode('latin-1')
    ser.write(l2)
"""-------------------------------------------------
Se inicializan las variables globales
-------------------------------------------------"""
iniCash = 15000
on = 0 #variable para inicio de raspberry
x = 0 #variable para 
"""-------------------------------------------------
Rutina que envía al Arduino la señal cuando enciende
-------------------------------------------------"""
while(on<2): 
    l="INI_OK"
    l2 = l.encode('latin-1')
    print(l2)
    ser.write(l2)
    time.sleep(2)
    on=on+1
    
while True:
    """-------------------------------------------------
    Lectura de Botón Principal para iniciar juego
    -------------------------------------------------""" 
    lectura = leer_serial()
        
    if lectura == "BP_PRESIONADO":
        
        # Instancia de objetos
        J1 = Jugador()
        J2 = Jugador()
        banco = Banco()
        
        # Deposito Inicial
        banco.asignarDineroInicial(depoIni)
        J1.depositoInicial(depoIni)
        banco.asignarDineroInicial(depoIni)
        J2.depositoInicial(depoIni)
    
        saldoJ1 = J1.calcularSaldoTotal()
        saldoJ2 = J2.calcularSaldoTotal()
        # Imprime saldo inicial de cada jugador
        print('\n' + 'DEPÓSITO INICIAL:')
        print('J1 = $' + str(J1.calcularSaldoTotal()))
        print('J2 = $' + str(J2.calcularSaldoTotal()))
        
        time.sleep(2)

        l="DEPO_INI"
        print(l)
        escribir_serial(l)
        
        time.sleep(2)
        
        l="J1,"+str(saldoJ1)+",J2,"+str(saldoJ2)
        #print(l)
        escribir_serial(l)
        
        print('\n' + 'INICIO DE JUEGO:')
    
#     if lectura == "INICIO":
#     while (x==1):
# 
#         lineBytes = ser.readline() #lee los datos del arduino
#         line = lineBytes.decode('latin-1').strip()
#         print(line)
        
#         if line == "GANAR":
#             d1 = banco.sacarDinero(5000)
#             d2 = banco.sacarDinero(3500)
#             J1.ganarDinero(d1)
#             J2.ganarDinero(d2)
#             print ("El saldo de J1 es = ",J1.calcularSaldoTotal(),"Pesos")
#             print ("El saldo de J2 es = ",J2.calcularSaldoTotal(),"Pesos")
#             print ("El saldo del banco es = ",banco.calcularSaldoTotal(),"Pesos")
#             
#             l="MONEY"
#             l2 = l.encode('latin-1')
#             ser.write(l2)      