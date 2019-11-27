#include <SoftwareSerial.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(4, 5, 6, 7, 8, 9);
SoftwareSerial GSerial(11,12); 
void recv();
void transmit();
void setup()
{
  
  Serial.begin(9600);
  GSerial.begin(1000);
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("  LiFi Project");
  lcd.setCursor(0, 1);
  lcd.print("       By  ");
  delay(2000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("TONY J MATHEW");
  lcd.setCursor(0, 1);
  lcd.print("1BM17CS119");
  delay(3000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("SHREYAS K");
  lcd.setCursor(0,1); 
  lcd.print("1BM17CS098");
  delay(3000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("TARUN M KRISHNA");
  lcd.setCursor(0,1); 
  lcd.print("1BM17CS116");
  delay(3000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("TARUN VENKATESH ");
  lcd.setCursor(0,1); 
  lcd.print("1BM17CS117");
  delay(3000);
  lcd.clear();
  lcd.setCursor(0,0);
  Serial.println("Waiting...");
}

void loop()
{
  if(Serial.available())
    transmit();
  if(GSerial.available())
    recv();
}

void recv()
{
      char r=GSerial.read();
      Serial.print(r);
      lcd.print(r);
      
}

void transmit()
{ 
    String a=Serial.readString();
    int l=a.length();
    Serial.println("\nTRANSMITTER:");
    Serial.println(a);
    for(int i=0;i<l;i++)
    {   
      lcd.print(a[i]);
      GSerial.print(a[i]);
    }
}
