# Tipos de variables

nombre = "Javier"  # String
apellidos = "Carrillo Pérez"
nombre_completo = nombre + " " + apellidos  # Concatenación de strings
edad = 30  # Integer
vivo = True  # Boolean

# Mostrar los tipos de variables
print("Tipo de variable nombre_completo:", type(nombre_completo))
print("Tipo de variable edad:", type(edad))
print("Tipo de variable vivo:", type(vivo))

# Mostrar por pantalla la presentación de la persona
print("\n\t****************************\n")
print("\tCarta de presentación\t")
print("\tMe llamo", nombre_completo,"y tengo", edad, "años.\n")
print("\t****************************\n")