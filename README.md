# portafolio fundamento de programación
# Qué es Python?
Python es un lenguaje de programación de alto nivel, orientado a objetos, con una semántica dinámica integrada, principalmente para el desarrollo web y de aplicaciones informáticas. Es una aplicación muy fácil de utilizar, es la mas recomendable para  personas que recién estan empezando en el mundo de la programación.

# Qué es una variable?
En algunos lenguajes de programación, a manera de analogía las variables se pueden entender como "cajas" en las cuales se guardan los datos. 

## Nombrando una variable
MANERA CORRECTA DE NOMBRAR UNA VARIABLE.
_variable
variable1
variable
vari_able
var1able
LA MANERA INCORRECTA DE NOMBRAR UNA VARIABLE. 
1variable
vari able
vari-able

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


## Tuple
Un tuple es una colección de datos cuyo orden es inalterable, o sea, son elementos ordenados en una secuencia específica y que posee importancia,a los tuple los escribimps en parentesis 
````
paises=("ecuador","perú","colombia")
print(paises)
````

## Dictionary
Un Diccionario es una estructura de datos y un tipo de dato en Python con características especiales que nos permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. Estos diccionarios nos permiten además identificar cada elemento por una clave.

# Tomando decisiones
## Sentencia if



## Ciclo For
'for' es un bucle que repite el bloque de instrucciones un número prederminado de veces. El bloque de instrucciones que se repite se suele llamar cuerpo del bucle y cada repetición se suele llamar iteración
## Ciclo While
Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True)

## Break
En Python, la instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa. Debe poner la instrucción break dentro del bloque de código bajo la instrucción de su bucle, generalmente después de una instrucción if condicional.

## Continue
La instrucción continue da la opción de omitir la parte de un bucle en la que se activa una condición externa, pero continuar para completar el resto del bucle. Es decir, la iteración actual del bucle se interrumpirá, pero el programa volverá a la parte superior del bucle.

La instrucción continue se encuentra dentro del bloque de código abajo de la instrucción del bucle, generalmente después de una instrucción if condicional.

