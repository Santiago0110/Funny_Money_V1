"""-------------------------------------------------
Librerías importadas de Python
Creado por: Santiago Lasso
-------------------------------------------------"""
import serial
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
#Inicia el programar con el led apagado
GPIO.output(8,False)
"""-------------------------------------------------
Configuración de puerto serial Raspberry - Arduino
-------------------------------------------------"""
#nombre del dispositivo serial : dmesg | grep -v disconnect | grep -Eo "tty(ACM|USB)." | tail -1
ser = serial.Serial('/dev/ttyUSB1',9600)
ser.flushInput()
"""-------------------------------------------------
CREACIÓN CLASE JUGADOR
-------------------------------------------------"""
class Jugador(object):
    
    #---------------------------------------
    #Método Constructor de la Clase Jugador
    #---------------------------------------
    def __init__(self,n_player):
        self.n_player = n_player
        self.ingresos = []
        self.egresos = []
        self.ahorros = []
        self.totalIngresos = 0
        self.totalEgresos = 0
        self.saldo = 0

    def ganarDinero(self,valor):
        self.ingresos.append(valor)

    def hacerCompras(self,valor):
        self.egresos.append(valor)

    def calcularTotalIngresos(self):
        self.totalIngresos = sum(self.ingresos)
        return self.totalIngresos
    
    def calcularTotalEgresos(self):
        self.totalEgresos = sum(self.egresos)
        return self.totalEgresos

    def calcularSaldoTotal(self):
        saldoTotal = sum(self.ingresos)-sum(self.egresos)
        return saldoTotal
"""-------------------------------------------------
CREACIÓN CLASE BANCO
-------------------------------------------------"""
class Banco(object):
    
    #---------------------------------------
    #Método Constructor de la Clase Banco
    #---------------------------------------
    def __init__(self):
        self.entradas = []
        self.salidas = []
        self.totalEntradas = 0
        self.totalSalidas = 0
        self.saldoInicial = 200000
        self.saldoTotal = 0
        
    def asignarDineroInicial(self,valor):
        self.salidas.append(valor)
        return valor
    
    def guardarDinero(self,valor):
        self.entradas.append(valor)
        return valor
    
    def sacarDinero(self,valor):
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
    lineBytes = ser.readline() #lee los datos del arduino
    line = lineBytes.decode('latin-1').strip()
    print(line)
        
    if line == "INICIO":
        GPIO.output(8,True)
        # Crear jugadores
        J1 = Jugador(1)
        J2 = Jugador(2)
        banco = Banco()
        
        depositoInicial = banco.asignarDineroInicial(iniCash)
        J1.ganarDinero(depositoInicial)
        depositoInicial = banco.asignarDineroInicial(iniCash)
        J2.ganarDinero(depositoInicial)
        print ("J1 ha ganado = ",J1.calcularTotalIngresos(),"Pesos")
        print ("J2 ha ganado = ",J2.calcularTotalIngresos(),"Pesos")
        x = 1 

    while (x==1):

        lineBytes = ser.readline() #lee los datos del arduino
        line = lineBytes.decode('latin-1').strip()
        print(line)
        
        if line == "GANAR":
            d1 = banco.sacarDinero(5000)
            d2 = banco.sacarDinero(3500)
            J1.ganarDinero(d1)
            J2.ganarDinero(d2)
            print ("El saldo de J1 es = ",J1.calcularSaldoTotal(),"Pesos")
            print ("El saldo de J2 es = ",J2.calcularSaldoTotal(),"Pesos")
            print ("El saldo del banco es = ",banco.calcularSaldoTotal(),"Pesos")
            
            l="MONEY"
            l2 = l.encode('latin-1')
            ser.write(l2)      
