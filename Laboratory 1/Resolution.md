1-  Hacer el esquema de conexión en TinkerCard. (**15 ptos**) 

2-  Responder las siguientes preguntas: (**10 pto**) 

a-  Información del datasheet del sensor SR04 y de la fotoresistencia (LDR).  

Deberá consultar las propiedades del sensor algunas son: costo, velocidad de operación, tasa de error, robustez, peso, tamaño, etc.

b-  Información del datasheet de Arduino UNO y consultar el tipo de 

microcontrolador, memoria, y número de puertos análogos y digitales. 

    El tipo de microcontrolar que posee el arduino UNO es el ATMega328P el cuál está basado en 8-bit y pertenece a la familia AVR-RISC,
    también posee una memoria de 32KB Flash, 2KB SRAM, 1KB EEPROM, posee 14 puertos digitales y 6 análogos.

c-  ¿Para qué sirve la resistencia en fija unida con la fotoresistencia? 
    
    La resistencia fija junto al sensor de foto resistencia sirve para generar un divisor de voltaje el cuál 
    genera un cambio medible para el arduino UNO y no sobrepase el voltaje máximo aceptado.

d-  ¿Cuál es la diferencia entre pull-down y pull-up? 

3-  Hacer el programa realizando el IDE de Arduino (Código). Debe instalar la 

librería Servo para poner a funcionar el actuador. (**10 ptos**) 

4-  Una vez se encuentre funcionando su circuito con Arduino UNO. Responder 

las siguientes preguntas: (**10 ptos**) 

a-  ¿Qué pasa si se cambia el ancho del pulso en que se activa y desactiva el 

Trigger? 

b-  ¿Cuáles es el rango de valores que se reciben del puerto A0? 

    Los valores que se reciben del puerto A0 varian entre 295 y 300
    
c-  ¿Qué pasa si la resistencia R1 cambia de valor, ¿cómo afecta el valor? 

¿Qué valores de resistencia han usado?

    Al hacer un cambio de resistencia de 1K homios a 4K homios se notó una variación en los valores recibidos con un 
    aumento de 100.

5-  Funcionamiento del circuito. Mostrar el funcionamiento al profesor para 

validar este punto. (**20 ptos**) 

6-  Enviar el link del repositorio donde se encuentre el desarrollo del laboratorio 

(diagrama, código y respuesta de preguntas). Colocar en el repositorio un readme.md con el nombre de los integrantes **(5ptos)** 
