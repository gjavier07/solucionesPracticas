#Un profesor de matemática necesita generar la tabla de multiplicar de un número entero 
#comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:
#3x1=3
#3x2=6
#3x3=9
#…. y así hasta 10
#5.1 Resuelva este problema utilizando un mientras (while)
# y de modo que por la salida se emita la tabla tal como se propone.
#5.2 Resuelva este problema utilizando un para (for)
# y de modo que por la salida se emita la tabla tal como se propone.

numero = int(input("Ingrese un número entre 1 y 10, para calcular su tabla de multiplicar: "))

if 1 <= numero <= 10:
        i = 1
        while i <= 10:
            producto = numero * i
            print(f"{numero} x {i}= {producto}")
            i += 1
else:
    print("El número ingresado no es valido, vuelva a ingresar un numero entre 1-10.")

