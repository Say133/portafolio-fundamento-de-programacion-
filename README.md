# portafolio fundamento de programación
# Qué es Python?
Python es un lenguaje de programación de alto nivel, orientado a objetos, con una semántica dinámica integrada, principalmente para el desarrollo web y de aplicaciones informáticas. Es una aplicación muy fácil de utilizar, es la mas recomendable para  personas que recién estan empezando en el mundo de la programación.

# Qué es una variable?
En algunos lenguajes de programación, a manera de analogía las variables se pueden entender como "cajas" en las cuales se guardan los datos. 

## Nombrando una variable
MANERA CORRECTA DE NOMBRAR UNA VARIABLE.
````
_variable
variable1
variable
vari_able
var1able
````
LA MANERA INCORRECTA DE NOMBRAR UNA VARIABLE. 
````
1variable
vari able
vari-able
````

## Asignando valores a una variable
```python
edad = 19
```
Asignar varios valores a una variable
```python
x, y,z= 10, 4, 5
```
# Operadores básicos
suma'+'
Resta'-'
Multiplicación'*'
Dición'/'
Módulo'%'
Potencia'**' 

### Suma
"+" Adición entre los operadores

### Resta
"-"sustracciòn de valores

### Multiplicación
"*"Multiplicación entre los operadores


### División



### Módulo
"%" módulo entre los operadores

### potencia
"**" potencia entre operadores

#Tipos de datos en Python

## Integer
Enteros o integer(int) son un tipo de datos que permite representar números enteros, es decir, positivos y negativos no decimales. 
````python
p1=4
p2=2
x= 4**2
print(x)
output= 16 
````
## Float
El tipo numérico float permite representar un número positivo o negativo con decimales, es decir, números reales.
````
0.43
12.4
````

## String
Los cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles.
por ejemplo:
```
a="10"
b="5"
operación= a+b
print("15")
print("numero mayor")
```
## Casting en Python
Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro.
Hay dos tipos de cast o conversión de tipos que se pueden hacer :
Conversión implícita: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciones con dos tipos distintos.
ejemplo:
````python
1
a = 7
print(type(a))  
2
b = 3.0
print(type(b))  
3  
c = a + b  
print(c)  
print(type(c)) 
4  
d = a * b 
print(d) 
print(type(d))

output
1. <clase 'int'>
2. <clase 'float'>
    10.0
3. <clase 'float'>
    21,0
4. <clase 'float'>
````
Conversión explícita: Es realizada expresamente por nosotros, como por ejemplo convertir de str a int con str().
````python
a = 5
n = float(a) 
  
print(n) 
print(type(n))
5,0
<clase 'float'>
````
## List
list es un tipo contenedor, compuesto, que se usan para almacenar conjuntos de elementos relacionados del mismo tipo o de tipos distintos. para crear una lista en Python, simplemente hay que encerrar una secuencia de elementos separados por comas entre paréntesis cuadrados`[] 
````
para crear una lista con los números del 1 al 10 se haría del siguiente modo:
numeros=[1,2,3,4,5,6]
````
## Tuple
Un tuple es una colección de datos cuyo orden es inalterable, o sea, son elementos ordenados en una secuencia específica y que posee importancia,a los tuple los escribimos en parentesis.
````
paises=("ecuador","perú","colombia")
````

## Dictionary
Un Diccionario es una estructura de datos y un tipo de dato en Python con características especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. Estos diccionarios nos permiten además identificar cada elemento por una clave.
- Todos los elementos en el diccionario se encuentran encerrados en un par de corchetes {}.
````
ejemplo
diccionario = {"key1":<value1>,"key2":<value2>,"key3":<value3>,"key4":<value4>}
````
# Tomando decisiones
## Sentencia if
La sentencia if se utiliza para ejecutar un bloque de código si, y solo si, se cumple una determinada condición. Por esta manera esque if es usado para la toma de decisiones.
````
x=5
if x < 6:
   print(" es menor")
output= es menor 
````
## Ciclo For
'for' es un bucle que repite el bloque de instrucciones un número prederminado de veces. Entonces el ciclo for se repite varias veces.
````
for k in range (5):
    print(k)
output=0
       1
       2
       3
       4
````
  
## Ciclo While
Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True)

## Break
La sentencia break nos permite alterar el comportamiento de los bucles while y for. Concretamente, permite terminar con la ejecución del bucle.
La instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción if condicional.177
Esto significa que una vez se encuentra la palabra break, el bucle se habrá terminado.
## Continue
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle. Es decir, la iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior del bucle.
La instrucción continue se encuentra dentro del bloque de código abajo de la instrucción del bucle, generalmente después de una instrucción if condicional.

