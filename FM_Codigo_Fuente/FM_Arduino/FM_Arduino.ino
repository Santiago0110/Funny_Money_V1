#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

#define DFRx 11 
#define DFTx 12 
#define volumeMP3 30
#define DEBUG

// Botón principal y sensor del banco 
#define BP 3 
#define SB 4 

SoftwareSerial playerMP3Serial(DFRx, DFTx);
DFRobotDFPlayerMini playerMP3;

#include "protothreads.h"
pt ptBlink;
pt ptWaitBP;

// Botones de selección
int BS1=A0,BS2= A1,BS3=A2,BS4=A3;

// Leds de jugadores
int Led_J1=5,Led_J2=9; 
// Leds de categorías
int Led_GD=6,Led_HC=7,Led_RE=8;
// Tira LED
int Tira_LED=2,Led_Banco=10;

// variable for reading the pushbutton status
int BPstate = 1;
int RaspState = 0;    
int ronda_active = 0;    

char *s;
String data[10];
float saldoJ1=0,saldoJ2=0;
String turno_jugador,opt_elegida;

void blink_luces(struct pt *pt)
{
  PT_BEGIN(pt);

  do
  {
    digitalWrite(Led_J1,HIGH);
    digitalWrite(Led_J2,HIGH);
    digitalWrite(Led_GD,HIGH);
    digitalWrite(Led_HC,HIGH);
    digitalWrite(Led_RE,HIGH);
    digitalWrite(Led_Banco,HIGH);
    digitalWrite(Tira_LED,HIGH);

    PT_SLEEP(pt, 500);
    
    digitalWrite(Led_J1,LOW);
    digitalWrite(Led_J2,LOW);
    digitalWrite(Led_GD,LOW);
    digitalWrite(Led_HC,LOW);
    digitalWrite(Led_RE,LOW);
    digitalWrite(Led_Banco,LOW);
    digitalWrite(Tira_LED,LOW);
    
    PT_SLEEP(pt, 500);
    
  } while(true);
    PT_END(pt);
}

void rutina_wait_BP(struct pt *pt)
{
  PT_BEGIN(pt);

  do
  {
    digitalWrite(Led_GD,HIGH);
    digitalWrite(Led_HC,LOW);
    digitalWrite(Led_RE,LOW);
    PT_SLEEP(pt, 300);
    digitalWrite(Led_GD,LOW);
    digitalWrite(Led_HC,HIGH);
    digitalWrite(Led_RE,LOW);
    PT_SLEEP(pt, 300);
    digitalWrite(Led_GD,LOW);
    digitalWrite(Led_HC,LOW);
    digitalWrite(Led_RE,HIGH);
    PT_SLEEP(pt, 300);
    
  } while(true);
    PT_END(pt);
}

void setup()
{
  Serial.begin(9600); 
  Serial.println("BIENVENIDOS A FUNNY MONEY");

  playerMP3Serial.begin(9600);
  
  Serial.println();
  //Serial.println(F("Iniciando DFPlayer ... (Espere 3~5 segundos)"));
  if (!playerMP3.begin(playerMP3Serial)) 
  { 
    Serial.println(F("Falha:"));
    Serial.println(F("1.conexões!"));
    Serial.println(F("2.cheque o cartão SD!"));
    while(true){delay(0);}
  }
  
  //Serial.println(F("DFPlayer iniciado"));
  playerMP3.volume(volumeMP3);
  
  #ifdef DEBUG
    //Serial.println("o Setup acabou");
  #endif

  pinMode(BP,INPUT);
  pinMode(SB,INPUT);
  pinMode(BS1,INPUT);
  pinMode(BS2,INPUT);
  pinMode(BS3,INPUT);
  pinMode(BS4,INPUT);
  
  pinMode(Led_J1, OUTPUT);
  pinMode(Led_J2, OUTPUT);
  pinMode(Led_GD, OUTPUT);
  pinMode(Led_HC, OUTPUT);
  pinMode(Led_RE, OUTPUT);
  pinMode(Led_Banco, OUTPUT);
  pinMode(Tira_LED, OUTPUT);
  
  PT_INIT(&ptBlink);
  PT_INIT(&ptWaitBP);

  // Reproduce intro del juego
  playerMP3.playFolder(1, 1);
}

void leer_saldos_intro()
{
  String dato = Serial.readStringUntil('\n');
  //Serial.println(dato);
  s = strtok(dato.c_str(), ",");
  int i=0;
  while (s!=NULL)
  {
    data[i]=s;
    s=strtok(NULL, ",");
    i++;
  }
  //Serial.println("dato 1: "+data[0]);
  //Serial.println("dato 2: "+data[1]);
  //Serial.println("dato 3: "+data[2]);
  //Serial.println("dato 4: "+data[3]);
  saldoJ1 = data[1].toFloat();
  saldoJ2 = data[3].toFloat();
  Serial.println("Saldos actualizados: J1="+ String(saldoJ1)+" | J2="+String(saldoJ2));
}

void leer_rondas()
{
  String dato = Serial.readStringUntil('\n');
  s = strtok(dato.c_str(), ",");
  int i=0;
  String data[10];
  
  while (s!=NULL)
  {
    data[i]=s;
    s=strtok(NULL, ",");
    i++;
  }
  turno_jugador = data[0];
  opt_elegida = data[1];
  //Serial.println("Turno: "+ turno_jugador +" | Opción: " + opt_elegida);
}

void loop()
{

  if(RaspState==0){blink_luces(&ptBlink);}

  if(Serial.available()>0)
  { 
    String dato = Serial.readStringUntil('\n');
    Serial.println(dato);
    //--------------------------------------------
    //Dato de entrada cuando la raspberry enciende
    //--------------------------------------------
    if(dato == "INI_OK")
    {
      digitalWrite(Led_J1,LOW);
      digitalWrite(Led_J2,LOW);
      digitalWrite(Led_GD,LOW);
      digitalWrite(Led_HC,LOW);
      digitalWrite(Led_RE,LOW);
      digitalWrite(Led_Banco,LOW);
      digitalWrite(Tira_LED,LOW);

      // Reproduce sonido de encendido
      playerMP3.playFolder(1, 2);
      delay(1000);

      digitalWrite(Led_J1,HIGH);
      digitalWrite(Led_J2,HIGH);
      digitalWrite(Led_GD,HIGH);
      digitalWrite(Led_HC,HIGH);
      digitalWrite(Led_RE,HIGH);
      digitalWrite(Led_Banco,HIGH);
      digitalWrite(Tira_LED,HIGH);

      Serial.println("ENCENDIO LA RASPBERRY!");
      Serial.println("PRESIONA EL BOTON PRINCIPAL PARA INICIAR");
      RaspState=1;
    }

    while(RaspState==1 && BPstate==1)
    {
      if (digitalRead(BP) == HIGH)
      {
        Serial.println("BP_PRESIONADO");
        delay(300);
        BPstate=0;
        RaspState=0;
      }else{
          rutina_wait_BP(&ptWaitBP);
      }   
    }

    if(dato == "DEPO_INI")
    {
      digitalWrite(Led_J1,LOW);
      digitalWrite(Led_J2,LOW);
      digitalWrite(Led_GD,LOW);
      digitalWrite(Led_HC,LOW);
      digitalWrite(Led_RE,LOW);
      digitalWrite(Led_Banco,LOW);
      digitalWrite(Tira_LED,HIGH);

      // Reproduce pista caja registradora
      playerMP3.playFolder(1, 3);
      leer_saldos_intro();
      BPstate=1;
      Serial.println("RETIRA EL DINERO DEL BANCO");
      Serial.println("Y PRESIONA EL BOTON PARA CONTINUAR");

      while(BPstate==1)
      { 
        if (digitalRead(BP) == HIGH)
        {
          Serial.println("INI_RONDAS");
          digitalWrite(Led_J1,LOW);
          digitalWrite(Led_J2,LOW);
          digitalWrite(Led_GD,LOW);
          digitalWrite(Led_HC,LOW);
          digitalWrite(Led_RE,LOW);
          digitalWrite(Led_Banco,LOW);
          digitalWrite(Tira_LED,LOW);
          delay(300);
          BPstate=0;
          ronda_active=1;
        }else{
          rutina_wait_BP(&ptWaitBP);
          if (digitalRead(SB) == HIGH)
          {
            digitalWrite(Led_Banco,LOW);
          }else{
            digitalWrite(Led_Banco,HIGH);
          }
        }
      }
    }
    while(ronda_active==1)
    {
      leer_rondas();
      if(turno_jugador == "J1")
      {
        digitalWrite(Led_J1,HIGH);
        digitalWrite(Led_J2,LOW);
      }

      if(turno_jugador == "J2")
      {
        digitalWrite(Led_J1,LOW);
        digitalWrite(Led_J2,HIGH);
      }

      if (opt_elegida.charAt(0) == 'A') 
      {
        digitalWrite(Led_GD,HIGH);
        digitalWrite(Led_HC,LOW);
        digitalWrite(Led_RE,LOW);
      } 
      else if (opt_elegida.charAt(0) == 'B') 
      {
        digitalWrite(Led_GD,LOW);
        digitalWrite(Led_HC,HIGH);
        digitalWrite(Led_RE,LOW);
      }   
      else if (opt_elegida.charAt(0) == 'C') 
      {
        digitalWrite(Led_GD,LOW);
        digitalWrite(Led_HC,LOW);
        digitalWrite(Led_RE,HIGH);
      } 
    }
  }
  delay(100); 
}
