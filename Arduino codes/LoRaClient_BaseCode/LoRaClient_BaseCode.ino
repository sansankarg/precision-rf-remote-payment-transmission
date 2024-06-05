/*
 
The transmitter code arduino for sending data packet lora radio module 433MHz  ra02 lora
 
*/
 
#include <SPI.h> 
#include <LoRa.h>
#include <Keypad.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3F, 16, 2);

const byte ROWS = 4; // Four rows
const byte COLS = 4; // Four columns

char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS] = {31, 33, 35, 37}; // Connect to the row pinouts of the keypad
byte colPins[COLS] = {39, 41, 43, 45}; // Connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );


int counter = 0;
String sid1 = ""; // String to store the entered phone number for sid1
String sid2 = ""; // String to store the entered phone number for sid2
String ar = ""; 
 
void setup() {

  lcd.init();   // initializing the LCD
  lcd.backlight(); // Enable or Turn On the backlight 
 LoRa.setPins(10, 9, 2);//NSS, NRESET, and DIO0 pins can be changed by using LoRa.setPins(ss, reset, dio0).
  Serial.begin(9600);
 
  while (!Serial);
 
  Serial.println("LoRa Sender");
 
  if (!LoRa.begin(433E6)) {
 
    Serial.println("Starting LoRa failed!");
 
    while (1);
 
  }
 
 
 LoRa.crc();
  lcd.setCursor(0, 0);
  lcd.print("Press any key to");
  lcd.setCursor(0, 1);
  lcd.print("start");

 
 
}
 
void loop() {
   char key;
  while (!keypad.getKey()) {
    delay(100);
  }
  
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Enter sid1:");

  while (sid1.length() < 10) {
    key = keypad.getKey();
    if (key >= '0' && key <= '9') {
      sid1 += key;
      lcd.setCursor(0, 1);
      lcd.print(sid1);
    }
    delay(100);
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Enter sid2:");
  while (sid2.length() < 10) {
    key = keypad.getKey();
    if (key >= '0' && key <= '9') {
      sid2 += key;
      lcd.setCursor(0, 1);
      lcd.print(sid2);
    }
    delay(100);
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Enter AR:");
  while (ar.length() < 5) {
    key = keypad.getKey();
    if (key >= '0' && key <= '9') {
      ar += key;
      lcd.setCursor(0, 1);
      lcd.print(ar);
    }
    delay(100);
  }
  String combinedString = sid1 + sid2 + ar;
  Serial.println("Combined String: " + combinedString);
  String payload = combinedString;
  Serial.println("payload");
  Serial.print("Sending packet: ");
  lcd.clear();
  lcd.print("package sent");
  Serial.println(counter);
  LoRa.beginPacket();
  LoRa.print("payload");
  Serial.println(counter);
  LoRa.endPacket();
  counter++;

  delay(2000);
 
}