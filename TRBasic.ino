#include <SoftwareSerial.h>
//SoftwareSerial GSerial(11,12);
SoftwareSerial GSerial(11,12);
//int tr=1; 

void setup()
{
  Serial.begin(9600);
  GSerial.begin(1000);
  //Serial.println("Waiting...");
}

void loop()
{
  if(Serial.available()){
    digitalWrite(12,HIGH);
    delayMicroseconds(1);
    transmit();}
  else
    digitalWrite(12,LOW);
  if(GSerial.available())
    recv();
}

void recv()
{
      String s=GSerial.readString();
      Serial.println(s);
}

void transmit()
{ 
    String a=Serial.readString();
    int l=a.length();
    //Serial.print("\nTRANSMITTER:");
    //Serial.println(a);
    for(int i=0;i<l;i++)
    {   
      GSerial.print(a[i]);
    }
}
