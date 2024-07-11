# Lista de ventas
ventas = [
    {"fecha": "2024-01-01", "producto": "Manzanas", "cantidad": 10, "precio": 0.5},
    {"fecha": "2024-01-02", "producto": "Manzanas", "cantidad": 5, "precio": 0.5},
    {"fecha": "2024-01-01", "producto": "Naranjas", "cantidad": 8, "precio": 0.7},
    {"fecha": "2024-01-02", "producto": "Naranjas", "cantidad": 3, "precio": 0.7},
    {"fecha": "2024-01-01", "producto": "Peras", "cantidad": 7, "precio": 0.4},
    {"fecha": "2024-01-02", "producto": "Peras", "cantidad": 6, "precio": 0.4},
]

# Cálculo de ingresos totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print("Ingresos Totales:", ingresos_totales)

# Análisis del producto más vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    
    if producto not in ventas_por_producto:
        ventas_por_producto[producto] = 0
    ventas_por_producto[producto] += cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print("Producto Más Vendido:", producto_mas_vendido)

# Promedio de precio por producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    precio = venta["precio"]
    cantidad = venta["cantidad"]
    
    if producto not in precios_por_producto:
        precios_por_producto[producto] = (0, 0)
    suma_precios, cantidad_total = precios_por_producto[producto]
    precios_por_producto[producto] = (suma_precios + precio * cantidad, cantidad_total + cantidad)

precios_promedio_por_producto = {}
for producto, (suma_precios, cantidad_total) in precios_por_producto.items():
    precios_promedio_por_producto[producto] = suma_precios / cantidad_total
    print(f"Producto: {producto}, Precio Promedio: {precios_promedio_por_producto[producto]}")

# Ventas por día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingresos = venta["cantidad"] * venta["precio"]
    
    if fecha not in ingresos_por_dia:
        ingresos_por_dia[fecha] = 0
    ingresos_por_dia[fecha] += ingresos

print("Ingresos por Día:", ingresos_por_dia)

# Resumen de ventas
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto = precios_por_producto[producto][0]
    precio_promedio = precios_promedio_por_producto[producto]
    
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales_producto,
        "precio_promedio": precio_promedio
    }

print("Resumen de Ventas:", resumen_ventas)
