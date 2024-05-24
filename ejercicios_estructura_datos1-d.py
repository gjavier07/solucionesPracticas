#Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input).
# Luego mostrar los datos de la tupla.

n = int(input("Ingrese un número entero para determinar la cantidad de números pares: "))

numeros_pares = []

for i in range(1,n+1):
    if i % 2 == 0:
        numeros_pares.append(i)

numeros_pares_tupla = tuple(numeros_pares)

print("Los primeros números pares son:", numeros_pares_tupla)
