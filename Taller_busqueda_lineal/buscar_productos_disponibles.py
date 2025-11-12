# Datos de ejemplo (ampliados para mejores pruebas)
productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True},
    {'id': 6, 'nombre': 'iPad Air', 'marca': 'Apple', 'categoria': 'Tablet', 'precio': 599.99, 'stock': 3, 'disponible': True},
    {'id': 7, 'nombre': 'Samsung Galaxy Tab', 'marca': 'Samsung', 'categoria': 'Tablet', 'precio': 449.99, 'stock': 0, 'disponible': False},
    {'id': 8, 'nombre': 'AirPods Pro', 'marca': 'Apple', 'categoria': 'Audífonos', 'precio': 249.99, 'stock': 20, 'disponible': True},
    {'id': 9, 'nombre': 'Logitech MX Keys', 'marca': 'Logitech', 'categoria': 'Accesorios', 'precio': 99.99, 'stock': 12, 'disponible': True},
    {'id': 10, 'nombre': 'HP Pavilion', 'marca': 'HP', 'categoria': 'Laptop', 'precio': 799.99, 'stock': 2, 'disponible': True}
]

def buscar_productos_disponibles(productos):
    """
    Busca productos con stock disponible (stock > 0 y disponible=True)
    
    Args:
        productos: Lista de productos
    
    Returns:
        list: Productos disponibles
    """
    productos_disponibles = []
    for producto in productos:
        if producto['stock'] > 0 and producto['disponible']:
            productos_disponibles.append(producto)
    return productos_disponibles

def buscar_productos_sin_stock(productos):
    """
    Busca productos sin stock (stock = 0)
    
    Args:
        productos: Lista de productos
    
    Returns:
        list: Productos sin stock
    """
    productos_sin_stock = []
    for producto in productos:
        if producto['stock'] == 0:
            productos_sin_stock.append(producto)
    return productos_sin_stock

def buscar_productos_por_rango_precio(productos, precio_min, precio_max):
    """
    Busca productos dentro de un rango de precios
    
    Args:
        productos: Lista de productos
        precio_min: Precio mínimo
        precio_max: Precio máximo
    
    Returns:
        list: Productos en el rango de precios
    """
    productos_en_rango = []
    for producto in productos:
        if precio_min <= producto['precio'] <= precio_max:
            productos_en_rango.append(producto)
    return productos_en_rango

def buscar_productos_por_marca(productos, marca_buscada):
    """
    Busca productos de una marca específica
    
    Args:
        productos: Lista de productos
        marca_buscada: Marca a buscar
    
    Returns:
        list: Productos de la marca
    """
    productos_marca = []
    for producto in productos:
        if producto['marca'].lower() == marca_buscada.lower():
            productos_marca.append(producto)
    return productos_marca

def contar_productos_por_categoria(productos, categoria_buscada=None):
    """
    Cuenta productos por categoría
    
    Args:
        productos: Lista de productos
        categoria_buscada: Categoría específica (opcional)
    
    Returns:
        int or dict: Cantidad de productos o diccionario con conteos por categoría
    """
    if categoria_buscada:
        # Contar productos de una categoría específica
        contador = 0
        for producto in productos:
            if producto['categoria'].lower() == categoria_buscada.lower():
                contador += 1
        return contador
    else:
        # Contar productos por todas las categorías
        contador_categorias = {}
        for producto in productos:
            categoria = producto['categoria']
            if categoria in contador_categorias:
                contador_categorias[categoria] += 1
            else:
                contador_categorias[categoria] = 1
        return contador_categorias

def buscar_productos_por_stock_minimo(productos, stock_minimo):
    """
    Busca productos con stock igual o superior al mínimo especificado
    
    Args:
        productos: Lista de productos
        stock_minimo: Stock mínimo requerido
    
    Returns:
        list: Productos con stock suficiente
    """
    productos_con_stock = []
    for producto in productos:
        if producto['stock'] >= stock_minimo:
            productos_con_stock.append(producto)
    return productos_con_stock

def buscar_productos_bajo_stock(productos, limite_stock=5):
    """
    Busca productos con stock bajo (para reabastecimiento)
    
    Args:
        productos: Lista de productos
        limite_stock: Límite para considerar stock bajo
    
    Returns:
        list: Productos con stock bajo
    """
    productos_bajo_stock = []
    for producto in productos:
        if 0 < producto['stock'] <= limite_stock:
            productos_bajo_stock.append(producto)
    return productos_bajo_stock

def obtener_productos_mas_caros(productos, cantidad=3):
    """
    Obtiene los productos más caros
    
    Args:
        productos: Lista de productos
        cantidad: Cantidad de productos a retornar
    
    Returns:
        list: Productos más caros
    """
    # Ordenar productos por precio descendente
    productos_ordenados = sorted(productos, key=lambda x: x['precio'], reverse=True)
    return productos_ordenados[:cantidad]

def obtener_productos_mas_baratos(productos, cantidad=3):
    """
    Obtiene los productos más baratos
    
    Args:
        productos: Lista de productos
        cantidad: Cantidad de productos a retornar
    
    Returns:
        list: Productos más baratos
    """
    # Ordenar productos por precio ascendente
    productos_ordenados = sorted(productos, key=lambda x: x['precio'])
    return productos_ordenados[:cantidad]

def calcular_valor_inventario_total(productos):
    """
    Calcula el valor total del inventario
    
    Args:
        productos: Lista de productos
    
    Returns:
        float: Valor total del inventario
    """
    valor_total = 0.0
    for producto in productos:
        valor_total += producto['precio'] * producto['stock']
    return valor_total

def buscar_productos_con_filtros_multiples(productos, **filtros):
    """
    Búsqueda avanzada con múltiples filtros
    
    Args:
        productos: Lista de productos
        **filtros: Filtros a aplicar
    
    Returns:
        list: Productos que cumplen con todos los filtros
    """
    productos_filtrados = []
    
    for producto in productos:
        cumple_filtros = True
        
        for clave, valor in filtros.items():
            if clave == 'precio_min':
                if producto['precio'] < valor:
                    cumple_filtros = False
                    break
            elif clave == 'precio_max':
                if producto['precio'] > valor:
                    cumple_filtros = False
                    break
            elif clave == 'stock_min':
                if producto['stock'] < valor:
                    cumple_filtros = False
                    break
            elif clave == 'stock_max':
                if producto['stock'] > valor:
                    cumple_filtros = False
                    break
            elif clave == 'disponible':
                if producto['disponible'] != valor:
                    cumple_filtros = False
                    break
            elif clave in producto:
                if isinstance(valor, str):
                    if producto[clave].lower() != valor.lower():
                        cumple_filtros = False
                        break
                else:
                    if producto[clave] != valor:
                        cumple_filtros = False
                        break
            else:
                cumple_filtros = False
                break
        
        if cumple_filtros:
            productos_filtrados.append(producto)
    
    return productos_filtrados

# Pruebas de las funciones
print("=== BÚSQUEDA POR DISPONIBILIDAD Y CRITERIOS CONDICIONALES ===\n")

# Prueba 1: Productos disponibles
print("1. PRODUCTOS DISPONIBLES:")
disponibles = buscar_productos_disponibles(productos)
print(f"   Total de productos disponibles: {len(disponibles)}")
for producto in disponibles:
    print(f"   - {producto['nombre']} (Stock: {producto['stock']}, Precio: ${producto['precio']})")

# Prueba 2: Productos sin stock
print("\n2. PRODUCTOS SIN STOCK:")
sin_stock = buscar_productos_sin_stock(productos)
print(f"   Total de productos sin stock: {len(sin_stock)}")
for producto in sin_stock:
    print(f"   - {producto['nombre']} ({producto['categoria']})")

# Prueba 3: Búsqueda por rango de precios
print("\n3. PRODUCTOS ENTRE $500 Y $1000:")
en_rango = buscar_productos_por_rango_precio(productos, 500, 1000)
print(f"   Productos encontrados: {len(en_rango)}")
for producto in en_rango:
    print(f"   - {producto['nombre']}: ${producto['precio']}")

# Prueba 4: Búsqueda por marca
print("\n4. PRODUCTOS APPLE:")
productos_apple = buscar_productos_por_marca(productos, "Apple")
print(f"   Total productos Apple: {len(productos_apple)}")
for producto in productos_apple:
    print(f"   - {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")

# Prueba 5: Conteo por categoría
print("\n5. CONTEO DE PRODUCTOS POR CATEGORÍA:")
conteo_categorias = contar_productos_por_categoria(productos)
for categoria, cantidad in conteo_categorias.items():
    print(f"   - {categoria}: {cantidad} producto(s)")

# Prueba específica por categoría
print(f"\n   Productos en categoría 'Laptop': {contar_productos_por_categoria(productos, 'Laptop')}")

# Prueba 6: Productos con stock mínimo
print("\n6. PRODUCTOS CON STOCK MÍNIMO DE 10 UNIDADES:")
stock_minimo = buscar_productos_por_stock_minimo(productos, 10)
for producto in stock_minimo:
    print(f"   - {producto['nombre']}: {producto['stock']} unidades")

# Prueba 7: Productos con stock bajo
print("\n7. PRODUCTOS CON STOCK BAJO (≤ 5 unidades):")
bajo_stock = buscar_productos_bajo_stock(productos, 5)
for producto in bajo_stock:
    print(f"   - {producto['nombre']}: {producto['stock']} unidades - ¡Necesita reabastecimiento!")

# Prueba 8: Productos más caros y más baratos
print("\n8. TOP 3 PRODUCTOS MÁS CAROS:")
mas_caros = obtener_productos_mas_caros(productos, 3)
for i, producto in enumerate(mas_caros, 1):
    print(f"   {i}. {producto['nombre']}: ${producto['precio']}")

print("\n   TOP 3 PRODUCTOS MÁS BARATOS:")
mas_baratos = obtener_productos_mas_baratos(productos, 3)
for i, producto in enumerate(mas_baratos, 1):
    print(f"   {i}. {producto['nombre']}: ${producto['precio']}")

# Prueba 9: Valor total del inventario
print(f"\n9. VALOR TOTAL DEL INVENTARIO: ${calcular_valor_inventario_total(productos):,.2f}")

# Prueba 10: Búsqueda con filtros múltiples
print("\n10. BÚSQUEDA AVANZADA:")
print("   a) Productos Apple disponibles entre $200 y $800:")
resultados = buscar_productos_con_filtros_multiples(
    productos, 
    marca='Apple', 
    disponible=True, 
    precio_min=200, 
    precio_max=800
)
for producto in resultados:
    print(f"      - {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")

print("\n   b) Laptops con stock disponible:")
resultados = buscar_productos_con_filtros_multiples(
    productos,
    categoria='Laptop',
    disponible=True,
    stock_min=1
)
for producto in resultados:
    print(f"      - {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")

# Estadísticas adicionales
print("\n=== ESTADÍSTICAS ADICIONALES ===")
total_productos = len(productos)
total_disponibles = len(buscar_productos_disponibles(productos))
porcentaje_disponibles = (total_disponibles / total_productos) * 100

print(f"Total de productos en el sistema: {total_productos}")
print(f"Productos disponibles: {total_disponibles} ({porcentaje_disponibles:.1f}%)")
print(f"Productos sin stock: {len(sin_stock)}")
print(f"Valor promedio por producto: ${calcular_valor_inventario_total(productos)/total_productos:.2f}")

#¿Cuál es la complejidad temporal ?
# La complejidad temporal de las funciones de búsqueda y filtrado en este código es generalmente O(n), donde n es el número de productos en la lista. Esto se debe a que la mayoría de las funciones recorren la lista completa de productos una vez para aplicar los criterios de búsqueda o filtrado. Algunas funciones que implican ordenamiento, como obtener los productos más caros o más baratos, tienen una complejidad temporal de O(n log n) debido al proceso de ordenamiento.

# ¿En qué casos la búsqueda lineal es eficiente?    
# La búsqueda lineal es eficiente cuando se trabaja con listas pequeñas o cuando los datos no están ordenados. También es útil cuando se necesita realizar búsquedas simples y rápidas sin la sobrecarga de estructuras de datos más complejas.

#¿Cuándo sería mejor usar otro algoritmo de búsqueda?
# Sería mejor usar otro algoritmo de búsqueda, como la búsqueda binaria, cuando la lista de productos está ordenada y es grande. La búsqueda binaria tiene una complejidad temporal de O(log n), lo que la hace mucho más eficiente para grandes conjuntos de datos en comparación con la búsqueda lineal. Además, para búsquedas frecuentes, podría ser beneficioso utilizar estructuras de datos como tablas hash o árboles balanceados para mejorar la eficiencia de las búsquedas.