# Crea un programa que procese un email:

# Guarda un email en una variable: "USUARIO@EJEMPLO.COM"
# Convierte el email a minúsculas
# Separa el email en usuario y dominio (usa split con "@")
# Cuenta cuántos caracteres tiene el usuario
# Muestra toda la información formateada

email = "USUARIO@EJEMPLO.COM"
print(email.lower()) # Convierte a minúsculas

usuario = email.split("@")# Separa el usuario
print(usuario)

longitud_usuario = len(usuario[0]) # Cuenta los caracteres del usuario
print(longitud_usuario) 

print(usuario[0])
print(usuario[1])