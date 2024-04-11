// C++ code
//
#include <Servo.h>

long readUltrasonicDistance(int triggerPin, int echoPin) {
    pinMode(triggerPin, OUTPUT);  // Clear the trigger
    digitalWrite(triggerPin, LOW);
    delayMicroseconds(2);
    // Sets the trigger pin to HIGH state for 10 microseconds
    digitalWrite(triggerPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(triggerPin, LOW);
    pinMode(echoPin, INPUT);
    // Reads the echo pin, and returns the sound wave travel time in microseconds
    return pulseIn(echoPin, HIGH);
}

Servo servo_10;

void setup() {
    Serial.begin(9600);
    pinMode(A0, INPUT);
    servo_10.attach(10, 500, 2500);
    servo_10.write(0);
}

void loop() {
    int light = analogRead(A0);
    double distance = 0.01723 * readUltrasonicDistance(11, 12);
  
    Serial.println(light);
    Serial.println(distance);
  
    if (distance >= 80 && light >= 340) {
        servo_10.write(180);
    } 
    else if (distance <= 30 && (light > 2 && light < 340)) {
        servo_10.write(60);
    }
    else if (distance <= 5 && light == 2) {
        servo_10.write(0);
    }

    delay(10); // Delay a little bit to improve simulation performance
}
