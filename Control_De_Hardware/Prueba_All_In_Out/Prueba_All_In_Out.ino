#include <SoftwareSerial.h>

// Botones de selección
int BS1=A0,BS2= A1,BS3=A2,BS4=A3;
// Botón de selección y sensor del banco 
int BP=3,SB=4; 

// Leds de jugadores
int Led_J1=5,Led_J2=9; 
// Leds de categorías
int Led_GD=6,Led_HC=7,Led_RE=8;
// Tira LED
int Tira_LED=2;

void setup()
{
  Serial.begin(9600);
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
  pinMode(Tira_LED, OUTPUT);

  digitalWrite(Led_J1,LOW);
  digitalWrite(Led_J2,LOW);
  digitalWrite(Led_GD,LOW);
  digitalWrite(Led_HC,LOW);
  digitalWrite(Led_RE,LOW);
  digitalWrite(Tira_LED,LOW);
}

void loop()
{
  int BP_Read = digitalRead(BP);
  int SB_Read = digitalRead(SB);
  int BS1_Read = analogRead(BS1);
  int BS2_Read = analogRead(BS2);
  int BS3_Read = analogRead(BS3);
  int BS4_Read = analogRead(BS4);

  Serial.println(BS4_Read);
  
  if(BP_Read == 1)
  {
    digitalWrite(Led_J1,HIGH);
    digitalWrite(Led_J2,HIGH);
    digitalWrite(Led_GD,HIGH);
    digitalWrite(Led_HC,HIGH);
    digitalWrite(Led_RE,HIGH);
    digitalWrite(Tira_LED,HIGH);
  }else
  {
    digitalWrite(Led_J1,LOW);
    digitalWrite(Led_J2,LOW);
    digitalWrite(Led_GD,LOW);
    digitalWrite(Led_HC,LOW);
    digitalWrite(Led_RE,LOW);
    digitalWrite(Tira_LED,LOW);
  }

//  if(BS1_Read < 500)
//  { digitalWrite(Led_J1,HIGH);
//    digitalWrite(Led_J2,HIGH);
//  }else{
//    digitalWrite(Led_J1,LOW);
//    digitalWrite(Led_J2,LOW);
//  }

//  if(BS2_Read < 10)
//  { digitalWrite(Led_GD,HIGH);
//    digitalWrite(Led_HC,HIGH);
//    digitalWrite(Led_RE,HIGH);
//  }else{
//    digitalWrite(Led_GD,LOW);
//    digitalWrite(Led_HC,LOW);
//    digitalWrite(Led_RE,LOW);
//  }

//  if(BS3_Read < 50)
//  { digitalWrite(Tira_LED,HIGH);
//  }else{digitalWrite(Tira_LED,LOW);}
  
}
