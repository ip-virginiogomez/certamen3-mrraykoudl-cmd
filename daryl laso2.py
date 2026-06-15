## Problema 2: Registro de Ventas de una Tienda (35 pts)

'''**Enunciado:**
Una pequeña tienda registra las ventas diarias de 3 vendedores durante 3 días de la semana. El dueño quiere saber el rendimiento de cada vendedor y si alguno tuvo bajo desempeño.

**Indicaciones paso a paso:**
1. Crea una matriz 3x3 para guardar los montos de ventas (cada fila es un vendedor, cada columna es un día).
2. Calcula el total de ventas de cada vendedor (suma por fila solamente).
3. Identifica qué vendedor tuvo el mayor total de ventas.
4. Muestra una alerta si el total de algún vendedor es menor a $30.000.'''


montos_ventas = [
    [300, 200, 100],
    [50, 60, 600],
    [10, 50, 30]
]
vendedor_numero = 0
mayor_venta = 0
mejor_vendedor = 0

for i in range(len(montos_ventas)):
    total_vendedor = sum(montos_ventas[i])
    vendedor_numero = i + 1
    print(f"Vendedor {vendedor_numero} Total de ventas = {total_vendedor}")
    
    
    if total_vendedor > mayor_venta:
        mayor_venta = total_vendedor
        mejor_vendedor = vendedor_numero
        
    
    if total_vendedor < 30000:
        print (f"Vendedor {vendedor_numero}: Total de ventas = {total_vendedor}")

print("el mejor vendedor es el 2 :)")