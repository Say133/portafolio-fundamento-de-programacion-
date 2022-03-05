#ejercicio 1
diccionario = {
        'int': 10,
        'str': 'Hola3
        'float':8.0
        }
print(diccionario)

# ejercicio 2
#Escribir un programa que guarde en una variable el diccionario
#{'Euro':'€', 'Yen':'¥'}, pregunte al usuario por una 
#divisa" moneda" y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
monedas = {'Euro':'€', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")
    
#Ejercicio 3
diccionario = {
"cartera": "Chanel",
"zapatos": "Aquazzura",
}

print(diccionario)
print(type(diccionario))


