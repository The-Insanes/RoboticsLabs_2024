import serial
import pyfirmata2
import time

board = pyfirmata2.Arduino('COM6')

class Motor():
    def __init__(self, ln1A, ln2A, ln1B, ln2B):
        self.ln1A = board.get_pin('d:{}:p'.format(ln1A))
        self.ln2A = board.get_pin('d:{}:p'.format(ln2A))
        self.ln1B = board.get_pin('d:{}:p'.format(ln1B))
        self.ln2B = board.get_pin('d:{}:p'.format(ln2B))

    def forward(self, speed):
        self.ln1A.write(speed)
        self.ln2A.write(0)

        board.digital[self.ln1B].write(speed)
        board.digital[self.ln2B].write(0)

if __name__ == '__main__':
    motor = Motor(5, 6, 9, 10)
    motor.forward(0.0)