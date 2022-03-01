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
### Suma
"+" Adición entre los operadores
```python
sum1=3
sum2=4
print(sum1+sum2) 
output=7
````
ejercicio 2
````python
edades=12,13,14,22,12,10.11
suma_edades=sum(edades)
print(suma_edades)
outout=94
````
### Resta
"-"sustracciòn de valores
````python
r1= 4
r2= 2
print(r1-r2)
output= 2 
````
ejercicio 2
````python
x=6
x=3
x=6-3
print(x)
output= 3
````
### Multiplicación
"*"Multiplicación entre los operadores
````python
m1=4
m2=2
print(m1*m2)
output= 8
````

### División
````python
"/"Division entre los operadores
d1=8
d2=2
print(d1/d2)
output= 4
````
### Módulo
"%" módulo entre los operadores
````python
d1=7
d2=2
print(d1/d2)
output=1
````

# Tipos de datos en Python

## Integer
Enteros o integer(int) son un tipo de datos que permite representar números enteros, es decir, positivos y negativos no decimales. 
ejemplo 1
````python
````


## Float
El tipo numérico float permite representar un número positivo o negativo con decimales, es decir, números reales.

## String
Los cadenas (o strings) son un tipo de datos compuestos por secuencias de caracteres que representan texto. Estas cadenas de texto son de tipo str y se delimitan mediante el uso de comillas simples o dobles.
por ejemplo:
print("numero mayor")

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
2. <clase 'flotar'>
    10.0
3. <clase 'flotar'>
    21,0
4. <clase 'flotar'>
Conversión explícita: Es realizada expresamente por nosotros, como por ejemplo convertir de str a int con str().
## List

## Tuple

## Dictionary

# Tomando decisiones

## Sentencia if

## Ciclo For

## Ciclo While

## Break

## Continue
