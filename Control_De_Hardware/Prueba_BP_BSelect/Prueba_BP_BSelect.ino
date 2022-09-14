#include <SoftwareSerial.h>
int BS1 = A0; //Botón de selección 1
int BS2 = A1; //Botón de selección 2
int BS3 = A2; //Botón de selección 3
int BS4 = A3; //Botón de selección 4
int BP = 3;   //Botón principal
int SB = 4;   //Sensor del banco

void setup()
{
  Serial.begin(9600);
  pinMode(BP,INPUT);
  pinMode(SB,INPUT);
  pinMode(BS1,INPUT);
  pinMode(BS2,INPUT);
  pinMode(BS3,INPUT);
  pinMode(BS4,INPUT);
}

void loop()
{
  int BP_Read = digitalRead(BP);
  int SB_Read = digitalRead(SB);
  int BS1_Read = analogRead(BS1);
  int BS2_Read = analogRead(BS2);
  int BS3_Read = analogRead(BS3);
  int BS4_Read = analogRead(BS4);
  
  Serial.print("BP: ");
  Serial.print(BP_Read);
  Serial.print(" ");
  Serial.print("SB: ");
  Serial.print(SB_Read);
  Serial.print(" ");
  Serial.print("BS1: ");
  Serial.print(BS1_Read);
  Serial.print(" ");
  Serial.print("BS2: ");
  Serial.print(BS2_Read);
  Serial.print(" ");
  Serial.print("BS3: ");
  Serial.print(BS3_Read);
  Serial.print(" ");
  Serial.print("BS4: ");
  Serial.println(BS4_Read);
}
