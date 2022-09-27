#include <Servo.h>

Servo base_servomotor;

void setup() {
  Serial.begin(9600);
  delay(1000);
  
  base_servomotor.attach(7);
  base_servomotor.write(0);
  delay(50);
  
} 

void loop() {
  for(int angle = 0; angle < 45; angle++){
    base_servomotor.write(angle);
    Serial.println(angle);
    delay(1000);
  }

  exit(0);
}
