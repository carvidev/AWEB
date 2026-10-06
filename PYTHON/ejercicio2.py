# Crea una calculadora de compras que calcule:

# Precio unitario de un producto: €15.99
# Cantidad a comprar: 4 unidades
# Calcula el subtotal (precio × cantidad)
# Aplica un descuento del 10% (subtotal × 0.10)
# Calcula el total final (subtotal - descuento)
# Calcula el IVA 21% sobre el total (total × 0.21)
# Muestra todos los valores

precio = 15.99
cantidad = 4
subtotal = precio * cantidad
descuento = subtotal * 0.10
total = subtotal - descuento
iva = total * 0.21
total_con_iva = total + iva

print(f"Precio unitario: {precio}€")
print(f"Cantidad a comprar: {cantidad} unidades")
print(f"Subtotal: {subtotal}€")
print(f"Descuento: {descuento}€")
print(f"Total: {total}€")
print(f"IVA (21%): {iva}€")
print(f"Total con IVA: {total_con_iva}€")
