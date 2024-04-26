# Preguntas laboratorio 2

## Participantes:

- Matías Bugueño
- Francisco Cortés

### ¿Para qué sirve la librería Pyserial?

> La descripción de la biblioteca PySerial indica que su función principal es facilitar el acceso a los puertos seriales desde programas escritos en Python, permitiendo el envio y recepción de datos desde un dispositivo externo. Lo hace proporcionando una interfaz común sin importar el sistema operativo en el que se ejecute el código.

### ¿Para qué sirve la librería pyFirmata2?

> PyFirmata2 es una biblioteca en Python diseñada para interactuar con placas Arduino,  permite utilizar un Arduino como si fuera una tarjeta de adquisición de datos, lo cual significa que puedes utilizarlo para recolectar y analizar datos desde sensores conectados a la placa Arduino directamente desde un script de Python. Su gran diferencia con PySerial es que PyFirmata está especializada para el uso de Arduino sin poder comunicarse a otros dispositivos, en cambio PySerial puede servir para cualquier conexión a la computadora en cuestión.

### ¿Qué significa la letra p y d en la configuración get_pin(‘d:{}:p’.format())?

> Las letras 'd' y 'p' en la función get_pin('d:{}:p'.format()) se utilizan para configurar pines en una placa Arduino usando PyFirmata o una biblioteca similar. La 'd' se refiere a un pin digital y la 'p' indica que el pin se configura para usar PWM.

### ¿Qué indica que el puerto sea PWM?, ¿Cuál es el símbolo para representar PWM en el Arduino UNO?

> PWM se refiere a la Modulación por Ancho de Pulso, una técnica que permite controlar la potencia enviada a dispositivos como LEDs y motores. En el Arduino UNO, los pines capaces de generar PWM están marcados con el símbolo ~, específicamente los pines 3, 5, 6, 9, 10 y 11. 

### ¿El parámetro speed cuál es el valor máximo y mínimo que soporta? (para esto debe probar el funcionamiento y cambiar los valores)

> El parámetro speed soporta como minimo 0 y como maximo 128.