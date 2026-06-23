compra = float(input("Ingrese el monto de compra: "))
if compra > 100:
    descuento = compra * 0.10
else:
    descuento = 0
total = compra - descuento
print("Descuento:", descuento)
print("Total a pagar:", total)