// Leds de jugadores
int Led_J1 = 5,Led_J2 = 9; 

void setup()
{
  pinMode(Led_J1, OUTPUT);
  pinMode(Led_J2, OUTPUT);
}

void loop()
{
  digitalWrite(Led_J1,HIGH);
  digitalWrite(Led_J2,HIGH);
  delay(200);
  digitalWrite(Led_J1,LOW);
  digitalWrite(Led_J2,LOW);
  delay(200); 
}
