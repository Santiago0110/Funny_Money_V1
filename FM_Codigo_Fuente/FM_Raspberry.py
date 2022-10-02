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
# Controla el numero de rodas que va ligado al numero de opciones x jugador
numMaxRondas = 12 

# Diccionario princial de categorías y opciones/categoria
cats = {
    'Ganar Dinero': ['A1','A2','A3','A4','A5','A6','A7','A8'],
    'Hacer Compras': ['B1','B2','B3','B4','B5','B6','B7','B8'],
    'Recompensas': ['C1','C2','C3','C4','C5','C6','C7','C8']     
}

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

cantidades = {
    'A1' :  {
        'a'  : 130000, 'b' : 233000},
    'A2' :  {
        'a'  : 45000, 'b' : 63000},
    'A3' : {
        'a'  : 95500, 'b' : 20000},
    'A4' :  {
        'a'  : 37000, 'b' : 67000},
    'A5' : {
        'a'  : 39000, 'b' : 150000},
    'A6' : {
        'a'  : 75000, 'b' : 59000},
    'A7' : {
        'a'  : 28000, 'b' : 15800},
    'A8' : {
        'a'  : 80000, 'b' : 50000},
    'B1' :  {
        'a'  : 26000, 'b' : 44000},
    'B2' :  {
        'a' :  20000, 'b' : 67000},
    'B3' :  {
        'a' : 30000, 'b' : 48000},
    'B4' :  {
        'a' : 15000,  'b' : 15000},
    'B5' :  {
        'a' : 57000,  'b' : 32000},
    'B6' :  {
        'a' : 43000,  'b' : 73000},
    'B7' :  {
        'a' : 55000,  'b' : 38000},
    'B8' :  {
        'a' : 26000,  'b' : 57000}
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

"""------------------------------
DECLARACIÓN FUNCIÓN DE EVALUACIÓN
------------------------------"""
def ahorrar(jugador,valor):
    jugador.ahorrarDinero(valor,10)

def evaluar_opcion_elegida_opt(jugador,opcion,decision):
    
    if opcion[0] == "A":
        
        if decision != "c":
            
            cantidad = cantidades[opcion][decision]
            banco.entregarDinero(cantidad)
            jugador.ganarDinero(cantidad)
            print('El jugador ha ganado = $' + str(cantidad))
            
            #var_save = input('¿Quieres ahorrar el 10% de lo que acabas de ganar? a) Sí b) No: ')
            # Enviar trama de datos seriales
            l="AHORRO"
            print(l)
            escribir_serial(l)

            wait=1
            while(wait==1):
                var_save = leer_serial()
                print("FUNCIONAAAAA")
                if var_save == "SI":
                    ahorrar(jugador,cantidad)
                    print("Ahorro exitoso")
                    wait = 0
                elif var_save == "NO":
                    wait = 0
                    
        else:
            pass

    elif opcion[0] == "B":
        
        if decision != "c":
            
            cantidad = cantidades[opcion][decision]
            banco.recibirDinero(cantidad)
            jugador.hacerCompras(cantidad)
            print('El jugador ha gastado = $' + str(cantidad))
            
        else:
            pass

    elif opcion[0] == "C":
        
        if decision != "b":
            
            pass
        else:
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
DECLARACIÓN FUNCIONES SERIALES
-----------------------------"""
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
        
    if lectura == "INI_RONDAS":
        print('INICIO DE JUEGO:')
        
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
        for i in range(numMaxRondas):
            
            print("Turno",i+1, "  Ronda:",(i//3)+1, "  Etapa en la ronda:",(i%3)+1)
            # Elige una opción para J1
            opt_J1 = jugador1.getAction(i)
            print("\n--> Acción jugador 1:", opt_J1)
            str_opt_elegida = mostrar_opcion_elegida(opt_J1,str_opciones)
            print(str_opt_elegida)
            # Enviar trama de datos seriales
            l="J1,"+str(opt_J1)
            print(l)
            escribir_serial(l)
            # Toma de decisión Jugador 1
            #decision_J1 = input('Elige una opción: ')
            loopJ1 = 1
            while(loopJ1==1):
                lectura = leer_serial()
                if lectura == "a":
                    decision_J1 = "a"
                    print(decision_J1)
                    evaluar_opcion_elegida_opt(J1,opt_J1,decision_J1)
                    loopJ1 = 0
                elif lectura == "b":
                    decision_J1 = "b"
                    print(decision_J1)
                    evaluar_opcion_elegida_opt(J1,opt_J1,decision_J1)
                    loopJ1 = 0
                elif lectura == "c":
                    decision_J1 = "c"
                    print(decision_J1)
                    evaluar_opcion_elegida_opt(J1,opt_J1,decision_J1)
                    loopJ1 = 0
            
            # Actualizar saldo de banco y jugador
            banco.calcularSaldoTotal()
            J1.calcularSaldoTotal()
        
            # Elige una opción para J2
            opt_J2 = jugador2.getAction(i)
            print("\n--> Acción jugador 2:", opt_J2)
            str_opt_elegida = mostrar_opcion_elegida(opt_J2,str_opciones)
            print(str_opt_elegida)
            # Enviar trama de datos seriales
            l="J2,"+str(opt_J2)
            print(l)
            escribir_serial(l)
            #decision_J2 = input('Elige una opción: ')
            loopJ2 = 1
            while(loopJ2==1):
                lectura = leer_serial()
                if lectura == "a":
                    decision_J2 = "a"
                    evaluar_opcion_elegida_opt(J2,opt_J2,decision_J2)
                    loopJ2 = 0
                elif lectura == "b":
                    decision_J2 = "b"
                    evaluar_opcion_elegida_opt(J2,opt_J2,decision_J2)
                    loopJ2 = 0
                elif lectura == "c":
                    decision_J2 = "c"
                    evaluar_opcion_elegida_opt(J2,opt_J2,decision_J2)
                    loopJ2 = 0
            
            # Actualizar saldo de banco y jugador
            banco.calcularSaldoTotal()
            J2.calcularSaldoTotal()
        
            print("--------------------------------------")
            
        mostrarResultados()