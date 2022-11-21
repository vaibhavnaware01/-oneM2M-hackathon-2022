#include <SoftwareSerial.h>
#include <EEPROM.h>
const int RelayPin = A3;
SoftwareSerial mySerial(7, 8);//rx,tx
int relayState;      // variable to store the read value
#define Mesh_led 2
#define Test_led 6
const String Node= "WN-LP18-01"; //node id
const String Node_OFF="LP18OFF";
const String Node_ON="LP18ON";
const String Node_Check="LP18CHK";
const String Node_Sts="LP18STS";
void setup()
{
delay(5000);
Serial.begin(9600);
mySerial.begin(9600);
pinMode(LED_BUILTIN, OUTPUT);
pinMode(Mesh_led, OUTPUT);
pinMode(Test_led, OUTPUT);
pinMode(RelayPin, OUTPUT);
mySerial.println("wisun connect");
digitalWrite(RelayPin, HIGH);
Serial.println("sending connect command");
Serial.println(F("Initialize System"));
checkRelayState();   //function to check and set the relay status
}
void loop()
{
String str="";
while(mySerial.available())
{
str=mySerial.readStringUntil('\n');
Serial.println(str);
delay(5);
if(str.substring(1,13)=="IPv6 address")
{
Serial.println("working");
digitalWrite(Mesh_led, HIGH);
mySerial.println("wisun udp_server 5001");
mySerial.println("wisun udp_client fd12:3456::1 5005");
delay(1000);
mySerial.println("wisun socket_write 4 \""+Node+" is connected to BR\"");
delay(1000);
mySerial.println("wisun get wisun");
}
if(str.substring(1,19)=="isun.border_router")
{
str=mySerial.readStringUntil(']');
String data = str.substring(17);
delay(700);
Serial.println(data);

mySerial.println("wisun socket_write 4 "+Node+"_to_"+data);  //connected device status
}
if(str.substring(1,7)==Node_ON)
{
mySerial.println("wisun socket_write 4 \""+Node+" is on\"");
digitalWrite(RelayPin,LOW);
digitalWrite(LED_BUILTIN, HIGH);
relayState = digitalRead(RelayPin);
EEPROM.update(0, relayState);
Serial.println("on");
}
if(str.substring(1,8)==Node_OFF)
{
mySerial.println("wisun socket_write 4 \""+Node+" is off\"");
digitalWrite(RelayPin,HIGH);
digitalWrite(LED_BUILTIN, LOW);
relayState = digitalRead(RelayPin);
EEPROM.update(0, relayState);
Serial.println("off");
}
if(str.substring(1,8)==Node_Check)
{
 mySerial.println("wisun get wisun");
 delay(5);
}
if(str.substring(1,8)==Node_Sts)
{
  if (relayState == HIGH)
  {
mySerial.println("wisun socket_write 4 \"sts "+Node+" is off\""); //sts node id is off
  Serial.println("off");

  }
 else
 {
mySerial.println("wisun socket_write 4 \"sts "+Node+" is on\"");  //sts node id is on
Serial.println("on");
 }
}
if (Serial.available()) 
{ 
mySerial.write(Serial.read());
}
}
}
 void checkRelayState() {
    Serial.println("Relay status after restart: ");
    relayState = EEPROM.read(0);
     if (relayState == 0) {
       Serial.println ("ON");
       digitalWrite(RelayPin, LOW);
     } 
     if (relayState == 1) {
       Serial.println ("OFF");
       digitalWrite(RelayPin, HIGH);
     }
}
