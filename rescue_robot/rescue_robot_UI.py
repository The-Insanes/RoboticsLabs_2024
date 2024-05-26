import platform
import select
import serial
import json
import time
import sys
import msvcrt

def non_blocking_input_w():
    sys.stdout.flush()
    
    data = ""
    while True:
        if msvcrt.kbhit():  # Verifica si hay entrada disponible en el teclado
            char = msvcrt.getche().decode()  # Lee un carácter
            if char == '\r':  # Si es Enter, termina de leer la entrada
                print()  # Imprime un salto de línea para mantener el formato
                break
            elif char == '\003':  # Si es Ctrl+C, termina el programa
                sys.exit()
            else:
                data += char
        else:
            break  # No hay entrada disponible, termina la función
            
    return data

def non_blocking_input_ml():
    sys.stdout.flush()
    
    ready, _, _ = select.select([sys.stdin], [], [], 0)
    if ready:
        return sys.stdin.readline().rstrip()
    else:
        return None


def read_robot(ser, data, json_file):
    if ser.in_waiting > 0:
        response = ser.readline().decode('utf-8').strip()
    
    if response:
        try:
            data = json.loads(response)
            data_list.append(data)
            
            with open(json_file, 'w') as f:
                json.dump(data_list, f, indent=4)
            
            print("Datos recibidos:", data)
        except json.JSONDecodeError:
            print("Respuesta del Arduino:", response)

def read_user():
    system = platform.system()

    if system == 'Windows':
        promp = non_blocking_input_w()
    if system == 'Linux' or system == 'macOS':
        promp == non_blocking_input_ml()

    return promp

if __name__ == '__main__':
    bluetooth_port = 'COM5'
    baud_rate = 9600

    rescue_robot = serial.Serial(bluetooth_port, baud_rate)
    time.sleep(2)

    json_file = './sensor_data.json'
    data_list = []
    command = ''

    print('Menú Rescue Robot:')
    print('indique la acción que desee realizar:')
    print('1) Empezar la ejecución del robot')
    print('2) Frenar la ejecución del robot')
    print('3) Cerrar programa')


    while True:
        option = read_user()
        if option ==  '1':
            command = 'run'
            rescue_robot.write((command).encode())

        if option == '2':
            command = 'stop'
            rescue_robot.write((command).encode())
        
        if option == '3':
            break

        if command == 'run':
            read_robot(rescue_robot, data_list, json_file)

    rescue_robot.close()
