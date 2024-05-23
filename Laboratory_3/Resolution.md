# Preguntas laboratorio 3

## Participantes: 

- Matías Bugueño
- Francisco Cortés

### ¿Cuál es el radio (en cms) de las ruedas (Ri y y Rd) la distancia entre las ruedas base del robot móvil asignado?

> El radio de las ruedas es de 2,75 y la distancia entre ellas es 6,5.

### Si se quiere que el robot recorra 1 metro desde un punto inicio a un punto destino de manera recta, ¿Cuál es el número de vueltas de las ruedas del robot? (para este punto considere una velocidad máxima)

> El numero de vueltas de la rueda del robot al recorrer un metro es de 5,787.

### ¿Cuál es la distancia mínima del robot?

> La distancia del robot es 13,5 cm.

### ¿De acuerdo el centro de masa del robot cual es la distancia a la base del robot (parte delantera)?

> Considerando que el centro de masa del robot está en su centro geométrico y la base delantera se encuentra en uno de los extremos de la base, la distancia desde el centro de masa hasta la base delantera sería la mitad de la altura del robot. Dado que la altura del robot es de 10.5 unidades, la distancia sería aproximadamente la mitad de eso, es decir, 5.25 unidades.

### Dibuje el diagrama del control de lazo cerrado teniendo como entrada un sensor de obstáculos.

<img src=./Images/Diagrama-Control-Lazo.png>

### ¿Cuál fue el rango de velocidades que ha asignado?

> El código asigna diferentes niveles de velocidad basados en la distancia medida por el sensor ultrasónico. Si la distancia es menor que 200 unidades, se establece una velocidad baja de 50. Para distancias entre 200 y 500 unidades, se asigna una velocidad media de 100. Y si la distancia supera las 500 unidades, se establece una velocidad alta de 255.

### ¿Cuál es el valor máximo (distancia) que logra calcular el sensor SR04?

> El valor máximo de distancia registrado por el sensor SR04 es de 1196 unidades.





