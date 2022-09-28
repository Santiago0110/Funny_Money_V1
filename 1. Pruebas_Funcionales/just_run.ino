//Declaración de variables
int c1=8,c2=7,c3=6;
int BP=3,lBanco=4;
int J1=A5,J2=A4;

int x=0;
int RaspState = 0;
int BPstate = 1;

void AllOff()
{
  digitalWrite(c1,LOW);
  digitalWrite(c2,LOW);
  digitalWrite(c3,LOW);
  digitalWrite(lBanco,LOW);
  analogWrite(J1,0);
  analogWrite(J2,0);
}

void AllOn()
{
  digitalWrite(c1,HIGH);
  digitalWrite(c2,HIGH);
  digitalWrite(c3,HIGH);
  digitalWrite(lBanco,HIGH);
  analogWrite(J1,1023);
  analogWrite(J2,1023);
}

void rutiIni()
{
  for(int i=0; i<255; i++)
  {
    analogWrite(c3, i);
    digitalWrite(c1,HIGH);
    digitalWrite(c2,HIGH);
    digitalWrite(lBanco,HIGH);
    delay(5);
  }
  for(int i=255; i>0; i--)
  {
    analogWrite(c3, i);
    digitalWrite(c1,LOW);
    digitalWrite(c2,LOW);
    digitalWrite(lBanco,LOW);
    delay(5);
  }
}

void setup() 
{
  pinMode(c1,OUTPUT);
  pinMode(c2,OUTPUT);
  pinMode(c3,OUTPUT);
  pinMode(BP,INPUT);
  pinMode(lBanco,OUTPUT);
  pinMode(J1,OUTPUT);
  pinMode(J2,OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  
  if(RaspState==0)
  {rutiIni();}

  if(Serial.available()>0)
  { 
    String dato = Serial.readStringUntil('\n');
    Serial.println(dato);
    //--------------------------------------------
    //Dato de entrada cuando la raspberry enciende
    //--------------------------------------------
    if(dato == "INI_OK")
    {
      AllOn();
      delay(2000);
      AllOff();
      RaspState=1;
    }
    //--------------------------------------------
    //Rutina LCD hasta que se presiona el BP
    //--------------------------------------------
    while(BPstate == 1)
    {
      int ButtonState = digitalRead(BP);  
      if(ButtonState == 0)
      {
        Serial.println("INICIO");
        delay(300);
        x = 1;
        BPstate=0;
      }
    }
    
    while(x==1)
    {
      int ButtonState = digitalRead(BP);  
      if(ButtonState == 0)
      {
        Serial.println("GANAR");
        delay(50);
        String dato = Serial.readStringUntil('\n');
        if(dato == "MONEY")
        {
          analogWrite(J1,1023);
          analogWrite(J2,1023);
          delay(600);
          analogWrite(J1,0);
          analogWrite(J2,0);
        }
      }
    } 

    
  }
 delay(100);
}
