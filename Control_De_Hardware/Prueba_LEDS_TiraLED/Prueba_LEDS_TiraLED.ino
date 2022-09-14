// Leds de jugadores
int Led_J1 = 5,Led_J2 = 9; 
// Leds de categorías
int Led_GD = 6, Led_HC = 7, Led_RE = 8;
// Tira LED
int Tira_LED = 2;

int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by

void setup()
{
  pinMode(Led_J1, OUTPUT);
  pinMode(Led_J2, OUTPUT);
  pinMode(Led_GD, OUTPUT);
  pinMode(Led_HC, OUTPUT);
  pinMode(Led_RE, OUTPUT);
  pinMode(Tira_LED, OUTPUT);
}

void fade()
{
  analogWrite(Led_J1, brightness);
  analogWrite(Led_J2, brightness);
  brightness = brightness + fadeAmount;
  if (brightness <= 0 || brightness >= 255)
  {
    fadeAmount = -fadeAmount;
  }
  delay(30);
}

void loop()
{
//  digitalWrite(Led_J1,HIGH);
//  digitalWrite(Led_J2,HIGH);
  fade();
  digitalWrite(Led_GD,HIGH);
  digitalWrite(Led_HC,HIGH);
  digitalWrite(Led_RE,HIGH);
  digitalWrite(Tira_LED,HIGH);
//  delay(200);
//  digitalWrite(Led_J1,LOW);
//  digitalWrite(Led_J2,LOW);
//  digitalWrite(Led_GD,LOW);
//  digitalWrite(Led_HC,LOW);
//  digitalWrite(Led_RE,LOW);
//  digitalWrite(Tira_LED,LOW);
//  delay(200); 
}
