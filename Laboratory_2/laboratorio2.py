import serial
import pyfirmata2
import time

board = pyfirmata2.Arduino('COM5')

class Motor():
    def __init__(self, ln1A, ln2A, ln1B, ln2B):
        self.ln1A = board.get_pin('d:{}:p'.format(ln1A))
        self.ln2A = board.get_pin('d:{}:p'.format(ln2A))
        self.ln1B = board.get_pin('d:{}:p'.format(ln1B))
        self.ln2B = board.get_pin('d:{}:p'.format(ln2B))

    def forward(self, speed):
        self.ln1A.write(speed)
        self.ln2A.write(0)

        self.ln1B.write(speed)
        self.ln2B.write(0)

    def turn_left(self, speed):
        self.ln1A.write(0)
        self.ln2A.write(0)

        self.ln1B.write(speed)
        self.ln2B.write(0)

    def turn_right(self, speed):
        self.ln1A.write(speed)
        self.ln2A.write(0)

        self.ln1B.write(0)
        self.ln2B.write(0)


    def turn_stop(self):
        self.ln1A.write(0)
        self.ln2A.write(0)
        self.ln1B.write(0)
        self.ln2B.write(0)

if __name__ == '__main__':
    motor = Motor(5, 6, 9, 10)

    for i in range(10):
        motor.forward(10.0)
        time.sleep(5)
        motor.turn_left(10.0)
        time.sleep(5)
        motor.turn_right(10.0)
        time.sleep(5)
        motor.turn_stop()