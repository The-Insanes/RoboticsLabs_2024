import serial
import time

arduino = serial.Serial('/dev/tty.usbserial-10', 9600)

setPoint = 100  # Set point for speed control, using ultrasonic sensor
time_PID = 0
integral = 0
time_prev = -1e-6
e_prev = 0
curSpeed = 0
deltat = 0.1

def PID(Kp, Ki, Kd, setpoint, measurement):
    global time_PID, integral, time_prev, e_prev
    offset = 320  # Valor de offset cuando el error es igual a cero
    e = setpoint - measurement
    P = Kp * e
    integral = integral + Ki * e * (time_PID - time_prev)
    D = Kd * (e - e_prev) / (time_PID - time_prev)
    MV = offset + P + integral + D
    e_prev = e
    time_prev = time_PID
    return MV

if __name__ == "__main__":
    while True:
        data = arduino.readline().decode().strip()
        try:
            distancia = int(data)
            print(f"Distancia: {distancia}")
            time_PID += deltat
            pid_out = PID(0.6, 0.2, 0.1, setPoint, distancia)
            print(f"PID output: {pid_out}")

            # Ajuste de velocidad basado en la distancia
            if distancia < 200:
                curSpeed = 50  # Velocidad baja
            elif distancia < 500:
                curSpeed = 100  # Velocidad media
            else:
                curSpeed = 255  # Velocidad alta

            arduino.write(f"{curSpeed}\n".encode())
            time.sleep(0.1)

        except ValueError:
            print("Error de lectura de distancia")
