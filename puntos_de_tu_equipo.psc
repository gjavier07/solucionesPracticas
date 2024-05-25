Algoritmo puntos_de_tu_equipo
	Escribir "ingrese la cantidad de partidos ganados: "
	Leer partidos_ganados
	Escribir "ingrese la cantidad de partidos empatados: "
	Leer partidos_empatados
	Escribir "ingrese la cantidad de partidos perdidos: "
	Leer partidos_perdididos
	
	puntos_ganados= partidos_ganados * 3
	puntos_empatados= partidos_empatados * 1
	puntos_perdidos= partidos_perdididos * 0
	
	total_puntos= puntos_ganados+puntos_empatados+puntos_perdidos
	
	Escribir  " la cantidad de puntos acumulados por el equipo es: ", total_puntos
	
FinAlgoritmo
