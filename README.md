##### Cómo usamos la pila en este programa
##### 
##### En este evaluador de expresiones matemáticas usamos pilas para que todo funcione sin romperse.
##### Básicamente tenemos dos pilas:
##### 
##### 1. Pila de operadores:
#####    - Guarda los signos +, -, *, / y los paréntesis mientras construimos la expresión postfija.
#####    - El último operador que pusimos es el primero que se revisa (LIFO: Last In, First Out).
#####    - Así respetamos la jerarquía de operaciones: primero *, /; luego +, -; y los paréntesis se resuelven en orden.
##### 
##### 2. Pila de operandos:
#####    - Una vez que tenemos la expresión en postfijo, guardamos los números en la pila.
#####    - Cada operador saca los últimos dos números, hace la operación y pone el resultado de vuelta.
#####    - Esto asegura que los cálculos se hagan en el orden correcto automáticamente.
##### 
##### Con estas pilas podemos manejar paréntesis anidados, respetar jerarquía de operaciones
##### y evaluar expresiones complejas sin preocuparnos por el orden de las operaciones.
