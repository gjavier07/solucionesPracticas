#Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.

persona = {}

persona["nombre"] = input("Ingrese el nombre de la persona: ")
persona["apellido"] = input("Ingrese el apellido de la persona: ")
persona["dni"] = input("Ingrese el DNI de la persona: ")
persona["email"] = input("Ingrese el email de la persona: ")
persona["fecha_nacimiento"] = input("Ingrese la fecha de nacimiento de la persona: ")

print("Los datos de la persona son:", persona)
