#EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo
#que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
#cliente le indica que necesita conocer el costo de mano de obra para pintar una
#pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro
#cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
#pintar la pared.

ancho = float(input("Ingrese el ancho de la pared en metros: "))

altura = float(input("Ingrese la altura de la pared en metros: "))

costo_por_metro = float(input("Ingrese el costo por metro cuadrado: "))

area = ancho * altura

costo_total = area * costo_por_metro

print("El costo total de la mano de obra para pintar la pared es:", costo_total)
