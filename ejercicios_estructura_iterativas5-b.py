numero = int(input("Ingrese un número entre 1 y 10, para calcular su tabla de multiplicar: "))

if 1 <= numero <= 10:
    for i in range(1, 11):
        producto = numero * i
        print(f"{numero} x {i}= {producto}")
else:
    print("ingrese un valor valido entre 1 o 10.")
