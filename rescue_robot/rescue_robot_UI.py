import serial
import json
import threading
import time

def send_command(ser, command):
    ser.write((command + '\n').encode())
    time.sleep(1)  # Espera un momento para que el Arduino procese el comando
    if ser.in_waiting > 0:
        response = ser.readline().decode('utf-8').strip()
        return response
    return None

bluetooth_port = 'COM5'
baud_rate = 9600

rescue_robot = serial.Serial(bluetooth_port, baud_rate)
time.sleep(2)

json_file = './sensor_data.json'
data_list = []

try:
    while True:
        print('') 
        command = input().strip()
        if command == "stop":
            rescue_robot.write((command).encode())
            break

        response = send_command(rescue_robot, command)
        if response:
            try:
                data = json.loads(response)
                data_list.append(data)
                
                with open(json_file, 'w') as f:
                    json.dump(data_list, f, indent=4)
                
                print("Datos recibidos:", data)  # Imprime los datos en la consola
            except json.JSONDecodeError:
                print("Respuesta del Arduino:", response)
except KeyboardInterrupt:
    print("Programa terminado por el usuario")

rescue_robot.close()
