# ejercicio 1
# Realizar un programa que pregunte la edad y muestre por pantalla si es mayor de edad o no.
edad = int(input("ingrese edad:"))
if edad < 18: 
    print ("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
    
#ejercicio 2
#realize una programa en donde se ingrese un número y verificamos si es par o impar
número= int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")
    
#ejercicio 3 
#solicitar y ver si el numero entero es positivo o negativo
num=-20

if num==0:
    print("cero")
if num>0:
    print("es positivo")
if num<0:
    print("es negativo")
