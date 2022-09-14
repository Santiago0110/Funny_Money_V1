// Leds de jugadores
int Led_J1 = 5,Led_J2 = 9; 
// Leds de categorías
int Led_GD = 6, Led_HC = 7, Led_RE = 8;

void setup()
{
  pinMode(Led_J1, OUTPUT);
  pinMode(Led_J2, OUTPUT);
  pinMode(Led_GD, OUTPUT);
  pinMode(Led_HC, OUTPUT);
  pinMode(Led_RE, OUTPUT);
}

void loop()
{
  digitalWrite(Led_J1,HIGH);
  digitalWrite(Led_J2,HIGH);
  digitalWrite(Led_GD,HIGH);
  digitalWrite(Led_HC,HIGH);
  digitalWrite(Led_RE,HIGH);
  delay(200);
  digitalWrite(Led_J1,LOW);
  digitalWrite(Led_J2,LOW);
  digitalWrite(Led_GD,LOW);
  digitalWrite(Led_HC,LOW);
  digitalWrite(Led_RE,LOW);
  delay(200); 
}
