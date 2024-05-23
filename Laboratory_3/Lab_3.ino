#include <Servo.h>
#include <string.h>
#include <SoftwareSerial.h>

class Motor {
private:
   int MOTOR_1A;
   int MOTOR_2A;
   int MOTOR_1B;
   int MOTOR_2B;

public:
   Motor(int pin_1A, int pin_2A, int pin_1B, int pin_2B) {
      MOTOR_1A = pin_1A;
      MOTOR_2A = pin_2A;
      MOTOR_1B = pin_1B;
      MOTOR_2B = pin_2B;

      pinMode(MOTOR_1A, OUTPUT);
      pinMode(MOTOR_2A, OUTPUT);
      pinMode(MOTOR_1B, OUTPUT);
      pinMode(MOTOR_2B, OUTPUT);
   }

   void forward(int speed) {
      analogWrite(MOTOR_1A, speed);
      analogWrite(MOTOR_1B, speed);
      digitalWrite(MOTOR_2A, LOW);
      digitalWrite(MOTOR_2B, LOW);
   }

   void backward(int speed) {
      analogWrite(MOTOR_1A, LOW);
      analogWrite(MOTOR_1B, LOW);
      analogWrite(MOTOR_2A, speed);
      analogWrite(MOTOR_2B, speed);
   }
 
   void turn_right(int speed) {
      analogWrite(MOTOR_1A, LOW);
      analogWrite(MOTOR_1B, speed);
      analogWrite(MOTOR_2A, speed);
      analogWrite(MOTOR_2B, LOW);
   }

   void turn_left(int speed) {
      analogWrite(MOTOR_1A, speed);
      analogWrite(MOTOR_1B, LOW);
      analogWrite(MOTOR_2A, LOW);
      analogWrite(MOTOR_2B, speed);
   }

   void stop() {
      digitalWrite(MOTOR_1A, LOW);
      digitalWrite(MOTOR_2A, LOW);
      digitalWrite(MOTOR_1B, LOW);
      digitalWrite(MOTOR_2B, LOW);
   }
};

SoftwareSerial BT(10, 11); 	
int TRIGGER = 7;
int ECHO = 8;
int degree_head;
int init_degree_head;
Motor motor(3, 5, 6, 9);
Servo servo_1;
String option;
long distance;

long ultrasonic_sensor(int trigger, int echo) {
   long time;

   digitalWrite(trigger, HIGH);
   delayMicroseconds(10);
   digitalWrite(trigger, LOW);

   time = pulseIn(echo, HIGH);

   return time / 58.2;
}

void setup(){
   pinMode(TRIGGER, OUTPUT);
   pinMode(ECHO, INPUT);

   degree_head = 97;
   init_degree_head = degree_head;
   servo_1.attach(4, 500, 2500);
   servo_1.write(degree_head);

   Serial.begin(9600);
   BT.begin(9600);
}

void loop(){
   distance = ultrasonic_sensor(TRIGGER, ECHO);
   Serial.println(distance);

   if (Serial.available() > 0) {
      int speedMotor = Serial.parseInt();
      motor.forward(speedMotor);
   }

   delay(100);
}
