#include <Arduino.h>

#include <WiFi.h>
#include <WiFiMulti.h>

#include <HTTPClient.h>

#define USE_SERIAL Serial

const int buttonPin = 10;
int buttonState = 0;

WiFiMulti wifiMulti;
void setup() {

  // Start serial connection
  Serial.begin(115200);
  
  // Wait for boot
  for(uint8_t t = 4; t > 0; t--) {
        Serial.printf("[SETUP] WAIT %d...\n", t);
        Serial.flush();
        delay(1000);
  }
    
  // Wifi Information
  wifiMulti.addAP("wifi_name", "wifi_password");

  // Setup button pin
  pinMode(buttonPin, INPUT);
}

void loop() {
   // Read button state
   buttonState = digitalRead(buttonPin);

   
   // wait for WiFi connection
   if((wifiMulti.run() == WL_CONNECTED)) {
       WiFiClient client;
       HTTPClient http;

       // Server ip
       http.begin(client, "http://192.168.1.13:8080/addMoneyTest");

       // Check if button is pushed
       if (buttonState == HIGH){
           // Make post request
           http.POST("a");

           // Alert user request made
           Serial.println("Post request made");
           delay(500);
       }

   }
}
