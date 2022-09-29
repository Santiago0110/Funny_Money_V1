#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

SoftwareSerial DFplayer(11, 12); // RX, TX
DFRobotDFPlayerMini myDFPlayer;

#include "protothreads.h"
pt ptBlink;

// Botones de selección
int BS1=A0,BS2= A1,BS3=A2,BS4=A3;
// Botón de selección y sensor del banco 
int BP=3,SB=4; 

// Leds de jugadores
int Led_J1=5,Led_J2=9; 
// Leds de categorías
int Led_GD=6,Led_HC=7,Led_RE=8;
// Tira LED
int Tira_LED=2,Led_Banco=10;

// variable for reading the pushbutton status
int buttonState = 0; 
int RaspState = 0;        

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

void setup()
{
  Serial.begin(9600); 
  Serial.println("BIENVENIDOS A FUNNY MONEY");

  DFplayer.begin(9600);

  if(!myDFPlayer.begin(DFplayer))
  {while(true){delay(0);}}

  myDFPlayer.volume(25);
  myDFPlayer.play(1);

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
      myDFPlayer.play(2);
      Serial.println("PRESIONA EL BOTÓN PRINCIPAL PARA INICIAR");
      RaspState=1;
    }
  } 
}
