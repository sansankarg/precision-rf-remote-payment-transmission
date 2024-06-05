
#include <LiquidCrystal_I2C.h>
#include <Key.h>
#include <Keypad.h>
#include <Keypad_I2C.h>
#include <SPI.h>
#include <LoRa.h>

LiquidCrystal_I2C lcd(0x3F,16,2);
#define I2CADDR 0x20

const byte ROWS = 4;
const byte COLS = 4;

// Set the Key at Use (4x4)
char keys [ROWS] [COLS] = {
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'*', '0', '#', 'D'}
};

int counter = 0;
String sid1 = "";
String sid2 = "";
String ar = "";

#define ss 15
#define rst 16
#define dio0 2


byte rowPins [ROWS] = {0, 1, 2, 3};
byte colPins [COLS] = {4, 5, 6, 7};
Keypad_I2C keypad (makeKeymap (keys), rowPins, colPins, ROWS, COLS, I2CADDR, PCF8574);


void setup() {

  Wire.begin(2,0);
  Serial.begin (9600);
  while (!Serial);
  Serial.println("LoRa Sender");
  LoRa.setPins(ss, rst, dio0);
    if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    delay(100);
    while (1);
  }
  Serial.println("LoRa achieved");
  lcd.init();
  lcd.clear();
  lcd.backlight();
  Serial.println("Lcd connected");


  keypad.begin (makeKeymap (keys));
  lcd.setCursor(0, 0);
  lcd.print("Press any key to");
  lcd.setCursor(0, 1);
  lcd.print("start");
  Serial.println("forwarding to loop");
}
void loop () {

  char key;
  while (!keypad.getKey()) {
    delay(100);
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Enter Sender sid");
  Serial.print("Enter Sender sid");
  while (sid1.length() < 11) {
    key = keypad.getKey();
    if (key >= '0' && key <= '9') {
      sid1 += key;
    }else if(key == 'B'){
      lcd.setCursor(0, 1);
      lcd.print("                        ");
      sid1.remove(sid1.length()-1);
    }else if(key == 'A'){
      break;
    }
    lcd.setCursor(0, 1);
    lcd.print(sid1);
    delay(100);
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Enter Reciever sid");
  Serial.print("Enter Reciever sid");
  while (sid2.length() < 11) {
    key = keypad.getKey();
    if (key >= '0' && key <= '9') {
      sid2 += key;
    }else if(key == 'B'){
      lcd.setCursor(0, 1);
      lcd.print("                        ");
      sid2.remove(sid2.length()-1);
    }else if(key == 'A'){
      break;
    }
    lcd.setCursor(0, 1);
    lcd.print(sid2);
    delay(100);
  }
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Enter ar:");
  Serial.print("Enter ar:");
  while (ar.length() < 11) {
    key = keypad.getKey();
    if (key >= '0' && key <= '9') {
      ar += key;
    }else if(key == 'B'){
      lcd.setCursor(0, 1);
      lcd.print("                        ");
      ar.remove(ar.length()-1);
    }else if(key == 'A'){
      break;
    }
    lcd.setCursor(0, 1);
    lcd.print(ar);
    delay(100);
  }
  String combinedString = sid1 + sid2 + ar;
  Serial.println("Combined String: " + combinedString);
  String payload = combinedString;
  Serial.println(payload);
  LoRa.beginPacket();
  LoRa.print(payload);
  LoRa.endPacket();
  Serial.println("Payload Sent");
  lcd.clear();
  lcd.print("package sent");
  String final = "Sender sid : "+sid1+", Reciever sid : "+sid2+" Amount of Ar transferred : "+ar;
  scrollMessage(1, final, 250, 16);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Press reset to end");
}
void scrollMessage(int row, String message, int delayTime, int totalColumns) {
  for (int i=0; i < totalColumns; i++) {
    message = " " + message;
  }
  message = message + " ";
  for (int position = 0; position < message.length(); position++) {
    lcd.setCursor(0, row);
    lcd.print(message.substring(position, position + totalColumns));
    delay(delayTime);
  }
}