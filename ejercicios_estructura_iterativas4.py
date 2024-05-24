#En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas 
#(las notas van de 0 a 10) de los alumnos de un curso. 
#Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8), 
#aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). 
#Desarrollar un algoritmo que resuelva este problema. 
#Para tener en cuenta: las autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.

cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes que han rendido el examen: "))

suma_notas = 0

for i in range(cantidad_estudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    suma_notas += nota

promedio = suma_notas / cantidad_estudiantes

if promedio > 8:
    rendimiento = "elevado"
elif promedio >= 6:
    rendimiento = "aceptable"
else:
    rendimiento = "bajo"

print(f"El promedio de las notas es: {promedio:.2f}")
print(f"El rendimiento del curso es: {rendimiento}")
