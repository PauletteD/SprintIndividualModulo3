import random

# Lista con los nombres de los usuarios
nombres_usuarios = ["Juan", "Maria", "Luis", "Ana", "Pedro", "Lucia", "Carlos", "Sofia", "Miguel", "Carmen"]

# Función para crear una cuenta y asignar una contraseña aleatoria
def crear_cuenta(nombre):
    # Crear una contraseña aleatoria con mayúsculas, minúsculas y números
    longitud = 8  # Longitud de la contraseña
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # Caracteres posibles
    contraseña = "".join(random.choices(caracteres, k=longitud))  # Contraseña aleatoria
    
    # Guardar la cuenta y la contraseña en un diccionario
    cuenta = {"nombre": nombre, "contraseña": contraseña, "teléfono": ""}
    
    return cuenta

# Crear una cuenta para cada usuario
cuentas = []
for nombre in nombres_usuarios:
    cuenta = crear_cuenta(nombre)
    cuentas.append(cuenta)

# Pedir el número de teléfono de cada usuario
while any(cuenta["teléfono"] == "" for cuenta in cuentas):
    for i, cuenta in enumerate(cuentas):
        if cuenta["teléfono"] == "":
            telefono = input(f"Ingrese el número de teléfono de {cuenta['nombre']}: ")
            cuentas[i]["teléfono"] = telefono

# Imprimir las cuentas y los números de teléfono asignados
for cuenta in cuentas:
    print(f"La cuenta de {cuenta['nombre']} tiene la contraseña {cuenta['contraseña']} y el número de teléfono {cuenta['teléfono']}.")
