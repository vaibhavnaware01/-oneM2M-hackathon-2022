#include <BH1750.h>
#include <Wire.h>
#include <WiFi.h>
#include "ThingSpeak.h" //include library for thingspeak to send data on server  
const char* ssid = "TP-Link_1EF4";
const char* password = "!th3sw9sT^uZ0";
BH1750 lightMeter(0x23);
unsigned long myChannelNumber = 1654574; //things speak channel id for communication
const char * myWriteAPIKey = "5HRQKSON0R3P8Y3Q"; // things speak api key for write data on server
WiFiClient  client;
int flag = 0;

void get_network_info()
{
    if(WiFi.status() == WL_CONNECTED) 
    {
        Serial.print("[*] Network information for ");
        Serial.println(ssid);

        Serial.println("[+] BSSID : " + WiFi.BSSIDstr());
        Serial.print("[+] Gateway IP : ");
        Serial.println(WiFi.gatewayIP());
        Serial.print("[+] Subnet Mask : ");
        Serial.println(WiFi.subnetMask());
        Serial.println((String)"[+] RSSI : " + WiFi.RSSI() + " dB");
        Serial.print("[+] ESP32 IP : ");
        Serial.println(WiFi.localIP());
    }
}
void setup() {
    Serial.begin(115200);
    delay(1000);
    WiFi.begin(ssid, password);
    Serial.println("\nConnecting");
    while(WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(100);
    }
    Serial.println("\nConnected to the WiFi network");
    get_network_info();
    ThingSpeak.begin(client); //Initialize ThingSpeak

    Wire.begin();
    if (lightMeter.begin(BH1750::CONTINUOUS_HIGH_RES_MODE)) 
    {
    Serial.println(F("BH1750 Advanced begin"));
    } 
    else 
    {
    Serial.println(F("Error initialising BH1750"));
    }
}

void loop() {
  if (lightMeter.measurementReady()) 
  {
    float lux = lightMeter.readLightLevel();
    Serial.print("Light: ");
    Serial.print(lux);
    Serial.println(" lx");
    int x = ThingSpeak.writeField(myChannelNumber, 1, lux , myWriteAPIKey);
    if(x == 200)
        {
          Serial.println("Channel update successful.");
        }
    else
        {
          Serial.println("Problem updating channel. HTTP error code " + String(x));
        }
     if (lux < 40 && flag == 0) {
    Serial.println(" => Dark");
    flag = 1;
  } 
else if(lux > 40 && flag == 1) {
    Serial.println(" => Very bright");
    flag = 0;
  }
  }
  delay(60000);
}
