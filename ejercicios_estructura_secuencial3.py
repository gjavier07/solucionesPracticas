#EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su
#equipo lleva acumulados en el campeonato, para ello recibe cada semana la
#información de la cantidad total de partidos, desde el inicio del campeonato, que
#el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
#recibe un punto, por cada partido ganado tres puntos y por los perdidos cero puntos.

partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))

partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))

partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))

puntos_ganados = partidos_ganados * 3

puntos_empatados = partidos_empatados * 1

puntos_perdidos = partidos_perdidos * 0

total_puntos = puntos_ganados + puntos_empatados + puntos_perdidos

print("La cantidad de puntos acumulados por el equipo es:", total_puntos)
