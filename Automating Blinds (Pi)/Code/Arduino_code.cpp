#include <AFMotor.h>

AF_DCMotor motor(4);

void setup() {
  motor.setSpeed(255);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char cmd = Serial.read();
    if      (cmd == 'O') motor.run(FORWARD);
    else if (cmd == 'C') motor.run(BACKWARD);
    else if (cmd == 'S') motor.run(RELEASE);
  }
}
