#En un nuevo diccionario llamado familia guardar 4 personas,
# cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)

familia = {}

for i in range(4):
    persona = {}
    persona["nombre"] = input(f"Ingrese el nombre de la persona {i+1}: ")
    persona["apellido"] = input(f"Ingrese el apellido de la persona {i+1}: ")
    persona["dni"] = input(f"Ingrese el DNI de la persona {i+1}: ")
    persona["email"] = input(f"Ingrese el email de la persona {i+1}: ")
    persona["fecha_nacimiento"] = input(f"Ingrese la fecha de nacimiento de la persona {i+1}: ")

    familia[f'persona_{i+1}'] = persona

print("Los datos de la familia son:", familia)
