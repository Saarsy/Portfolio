#include <AFMotor.h>

AF_DCMotor motor(4); // M4 port on the shield

void setup() {
  Serial.begin(9600);
  motor.setSpeed(255);   // full speed — lower this if the motor runs too fast/jerky
  motor.run(RELEASE);    // start stopped
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();

    if (cmd == 'O') {
      motor.run(FORWARD);   // "open" direction — swap to BACKWARD if blinds go the wrong way
    } else if (cmd == 'C') {
      motor.run(BACKWARD);  // "close" direction
    } else if (cmd == 'S') {
      motor.run(RELEASE);   // stop
    }
  }
}
