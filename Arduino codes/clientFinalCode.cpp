#include <SPI.h>
#include <LoRa.h>
void setup() {
  Serial.begin(9600);
  while (!Serial);
  if (!LoRa.begin(433E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}
void loop() {
  String data = "";
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    while (LoRa.available()) {
      data+=(char)LoRa.read();
    }
    Serial.print(data);
    Serial.print("\n");
    //Serial.print("' with RSSI ");
    //Serial.println(LoRa.packetRssi());
  }
}