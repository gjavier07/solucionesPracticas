#Pedir que el usuario ingrese (input) nombre de personas
#y mostrarlos hasta que el valor de lo que ingresa sea “fin”

while True:
    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    
    print(nombre)
