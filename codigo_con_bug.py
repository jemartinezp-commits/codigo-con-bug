edad = input("Ingresa tu edad: ")

# Debug
print("DEBUG tipo:", type(edad))
print("DEBUG valor:", [edad])
print("DEBUG longitud:", len(edad))

# Bug aquí 👇
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad") 