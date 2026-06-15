## Problema 3: Sistema de Descuento en Supermercado (20 pts)

'''**Enunciado:**
Un supermercado aplica descuentos especiales a sus clientes. Para acceder al descuento, el cliente debe ser mayor de 60 años o tener una tarjeta de socio, y además el total de su compra debe superar los $10.000.

**Indicaciones paso a paso:**
1. Solicita al usuario su edad, si tiene tarjeta de socio (sí/no) y el monto total de su compra.
2. Verifica si cumple las condiciones: el monto debe superar $10.000 y debe ser mayor de 60 años o tener tarjeta de socio.
3. Muestra un mensaje indicando si obtiene el descuento del 15% o si no califica, mostrando el monto final en cada caso.'''


edad = int(input("ingrese su edad: "))
tarjeta_socio = input("¿tiene tarjeta de socio? si/no: ")
monto_total = int(input("ingrese e monto total de su compra: "))

if edad >= 60 and tarjeta_socio == "si" and monto_total >= 10000:
    print("obtiene el descuento del 15%")
elif edad < 60 and tarjeta_socio == "no" and monto_total >= 10000:
    print("obtiene el descuento del 15%")
else:
    print("no califica para el descuento")