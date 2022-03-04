#EJERCICIO 1
#Escribir un programa que almacene en una lista los siguientes números, 34, 7, 56, 20, 5, 25, 19, y muestre por pantalla el menor y el mayor de los números
num= [34, 7, 56, 20, 5, 25, 19]
min = max = num[0]
for num in nums:
    if num < min:
        min = num
    elif num > max:
        max = num 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))

#ejercicio 2
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i])
# ejercicio 3 
