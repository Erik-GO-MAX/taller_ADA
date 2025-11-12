# Datos de ejemplo
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

empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True},
    {'id': 105, 'nombre': 'Laura', 'apellido': 'Hernández', 'departamento': 'Técnico', 'salario': 45000, 'activo': True},
    {'id': 106, 'nombre': 'Pedro', 'apellido': 'Gómez', 'departamento': 'Administración', 'salario': 32000, 'activo': False}
]

# ===============================
# FUNCIONES DE BÚSQUEDA DE PRODUCTOS
# ===============================

def buscar_producto_por_nombre(productos, nombre_buscado):
    """Busca un producto por nombre"""
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscado.lower():
            return producto
    return None

def buscar_producto_por_id(productos, id_buscado):
    """Busca un producto por ID"""
    for producto in productos:
        if producto['id'] == id_buscado:
            return producto
    return None

def buscar_productos_por_categoria(productos, categoria_buscada):
    """Busca productos por categoría"""
    productos_encontrados = []
    for producto in productos:
        if producto['categoria'].lower() == categoria_buscada.lower():
            productos_encontrados.append(producto)
    return productos_encontrados

def buscar_productos_por_marca(productos, marca_buscada):
    """Busca productos por marca"""
    productos_encontrados = []
    for producto in productos:
        if producto['marca'].lower() == marca_buscada.lower():
            productos_encontrados.append(producto)
    return productos_encontrados

def buscar_productos_disponibles(productos):
    """Busca productos disponibles"""
    productos_disponibles = []
    for producto in productos:
        if producto['disponible'] and producto['stock'] > 0:
            productos_disponibles.append(producto)
    return productos_disponibles

def buscar_productos_por_rango_precio(productos, precio_min, precio_max):
    """Busca productos por rango de precio"""
    productos_en_rango = []
    for producto in productos:
        if precio_min <= producto['precio'] <= precio_max:
            productos_en_rango.append(producto)
    return productos_en_rango

def contar_productos_por_categoria(productos):
    """Cuenta productos por categoría"""
    contador = {}
    for producto in productos:
        categoria = producto['categoria']
        if categoria in contador:
            contador[categoria] += 1
        else:
            contador[categoria] = 1
    return contador

# ===============================
# FUNCIONES DE BÚSQUEDA DE EMPLEADOS
# ===============================

def buscar_empleado_por_id(empleados, id_buscado):
    """Busca empleado por ID"""
    for empleado in empleados:
        if empleado['id'] == id_buscado:
            return empleado
    return None

def buscar_empleado_por_nombre_completo(empleados, nombre_completo):
    """Busca empleado por nombre completo"""
    partes = nombre_completo.strip().split()
    for empleado in empleados:
        nombre_empleado = f"{empleado['nombre']} {empleado['apellido']}"
        if nombre_completo.lower() == nombre_empleado.lower():
            return empleado
        if len(partes) >= 2:
            if (empleado['nombre'].lower() == partes[0].lower() and 
                empleado['apellido'].lower() == partes[1].lower()):
                return empleado
    return None

def buscar_empleados_por_departamento(empleados, departamento_buscado):
    """Busca empleados por departamento"""
    empleados_encontrados = []
    for empleado in empleados:
        if empleado['departamento'].lower() == departamento_buscado.lower():
            empleados_encontrados.append(empleado)
    return empleados_encontrados

def buscar_empleados_activos(empleados):
    """Busca empleados activos"""
    empleados_activos = []
    for empleado in empleados:
        if empleado['activo']:
            empleados_activos.append(empleado)
    return empleados_activos

# ===============================
# FUNCIONES DE VALIDACIÓN Y UTILIDAD
# ===============================

def validar_entero(mensaje):
    """Valida que la entrada sea un número entero"""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("❌ Error: Por favor ingrese un número entero válido.")

def validar_flotante(mensaje):
    """Valida que la entrada sea un número flotante"""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("❌ Error: Por favor ingrese un número válido.")

def validar_opcion(mensaje, opciones_validas):
    """Valida que la opción esté en la lista de opciones válidas"""
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in opciones_validas:
                return opcion
            else:
                print(f"❌ Error: Opción {opcion} no válida. Opciones válidas: {opciones_validas}")
        except ValueError:
            print("❌ Error: Por favor ingrese un número válido.")

def presionar_para_continuar():
    """Espera a que el usuario presione Enter para continuar"""
    input("\n📝 Presione Enter para continuar...")

def mostrar_producto(producto):
    """Muestra la información de un producto formateada"""
    if producto:
        estado = "✅ Disponible" if producto['disponible'] and producto['stock'] > 0 else "❌ No disponible"
        print(f"   📦 ID: {producto['id']}")
        print(f"   🏷️  Nombre: {producto['nombre']}")
        print(f"   🏭 Marca: {producto['marca']}")
        print(f"   📂 Categoría: {producto['categoria']}")
        print(f"   💰 Precio: ${producto['precio']:.2f}")
        print(f"   📊 Stock: {producto['stock']}")
        print(f"   🟢 Estado: {estado}")
    else:
        print("   ❌ Producto no encontrado")

def mostrar_empleado(empleado):
    """Muestra la información de un empleado formateada"""
    if empleado:
        estado = "✅ Activo" if empleado['activo'] else "❌ Inactivo"
        print(f"   👤 ID: {empleado['id']}")
        print(f"   📛 Nombre: {empleado['nombre']} {empleado['apellido']}")
        print(f"   🏢 Departamento: {empleado['departamento']}")
        print(f"   💵 Salario: ${empleado['salario']:,}")
        print(f"   🟢 Estado: {estado}")
    else:
        print("   ❌ Empleado no encontrado")

# ===============================
# MENÚS DEL SISTEMA
# ===============================

def menu_principal():
    """Menú principal del sistema"""
    while True:
        print("\n" + "="*50)
        print("🏢 SISTEMA INTEGRADO DE BÚSQUEDA")
        print("="*50)
        print("1. 🔍 Búsqueda de Productos")
        print("2. 👥 Búsqueda de Empleados")
        print("3. 📊 Estadísticas del Sistema")
        print("4. 🚪 Salir")
        print("="*50)
        
        opcion = validar_opcion("Seleccione una opción (1-4): ", [1, 2, 3, 4])
        
        if opcion == 1:
            menu_productos()
        elif opcion == 2:
            menu_empleados()
        elif opcion == 3:
            mostrar_estadisticas()
        elif opcion == 4:
            print("\n👋 ¡Gracias por usar el sistema! ¡Hasta pronto!")
            break

def menu_productos():
    """Menú de búsqueda de productos"""
    while True:
        print("\n" + "-"*40)
        print("📦 MÓDULO DE BÚSQUEDA DE PRODUCTOS")
        print("-"*40)
        print("1. 🔎 Buscar producto por ID")
        print("2. 🔎 Buscar producto por nombre")
        print("3. 📂 Buscar productos por categoría")
        print("4. 🏭 Buscar productos por marca")
        print("5. ✅ Buscar productos disponibles")
        print("6. 💰 Buscar por rango de precio")
        print("7. 📊 Conteo por categoría")
        print("8. ↩️ Volver al menú principal")
        print("-"*40)
        
        opcion = validar_opcion("Seleccione una opción (1-8): ", [1, 2, 3, 4, 5, 6, 7, 8])
        
        if opcion == 1:
            buscar_producto_id()
        elif opcion == 2:
            buscar_producto_nombre()
        elif opcion == 3:
            buscar_productos_categoria()
        elif opcion == 4:
            buscar_productos_marca()
        elif opcion == 5:
            buscar_productos_disponibles_menu()
        elif opcion == 6:
            buscar_productos_rango_precio()
        elif opcion == 7:
            contar_productos_categoria_menu()
        elif opcion == 8:
            break

def menu_empleados():
    """Menú de búsqueda de empleados"""
    while True:
        print("\n" + "-"*40)
        print("👥 MÓDULO DE BÚSQUEDA DE EMPLEADOS")
        print("-"*40)
        print("1. 🔎 Buscar empleado por ID")
        print("2. 🔎 Buscar empleado por nombre")
        print("3. 🏢 Buscar empleados por departamento")
        print("4. ✅ Buscar empleados activos")
        print("5. 📊 Listar todos los empleados")
        print("6. ↩️ Volver al menú principal")
        print("-"*40)
        
        opcion = validar_opcion("Seleccione una opción (1-6): ", [1, 2, 3, 4, 5, 6])
        
        if opcion == 1:
            buscar_empleado_id()
        elif opcion == 2:
            buscar_empleado_nombre()
        elif opcion == 3:
            buscar_empleados_departamento()
        elif opcion == 4:
            buscar_empleados_activos_menu()
        elif opcion == 5:
            listar_todos_empleados()
        elif opcion == 6:
            break

# ===============================
# FUNCIONES DE BÚSQUEDA INTERACTIVAS
# ===============================

def buscar_producto_id():
    """Busca producto por ID (interactivo)"""
    print("\n🔍 BUSCAR PRODUCTO POR ID")
    print("-" * 30)
    id_buscado = validar_entero("Ingrese el ID del producto: ")
    producto = buscar_producto_por_id(productos, id_buscado)
    mostrar_producto(producto)
    presionar_para_continuar()

def buscar_producto_nombre():
    """Busca producto por nombre (interactivo)"""
    print("\n🔍 BUSCAR PRODUCTO POR NOMBRE")
    print("-" * 30)
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre:
        producto = buscar_producto_por_nombre(productos, nombre)
        mostrar_producto(producto)
    else:
        print("❌ Error: Debe ingresar un nombre válido.")
    presionar_para_continuar()

def buscar_productos_categoria():
    """Busca productos por categoría (interactivo)"""
    print("\n📂 BUSCAR PRODUCTOS POR CATEGORÍA")
    print("-" * 30)
    print("Categorías disponibles: Smartphone, Laptop, Tablet, Audífonos, Accesorios")
    categoria = input("Ingrese la categoría: ").strip()
    if categoria:
        resultados = buscar_productos_por_categoria(productos, categoria)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} productos en la categoría '{categoria}':")
            for producto in resultados:
                print(f"   - {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")
        else:
            print(f"❌ No se encontraron productos en la categoría '{categoria}'")
    else:
        print("❌ Error: Debe ingresar una categoría válida.")
    presionar_para_continuar()

def buscar_productos_marca():
    """Busca productos por marca (interactivo)"""
    print("\n🏭 BUSCAR PRODUCTOS POR MARCA")
    print("-" * 30)
    print("Marcas disponibles: Apple, Samsung, Dell, Sony, Logitech, HP")
    marca = input("Ingrese la marca: ").strip()
    if marca:
        resultados = buscar_productos_por_marca(productos, marca)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} productos de la marca '{marca}':")
            for producto in resultados:
                print(f"   - {producto['nombre']} (${producto['precio']}, Stock: {producto['stock']})")
        else:
            print(f"❌ No se encontraron productos de la marca '{marca}'")
    else:
        print("❌ Error: Debe ingresar una marca válida.")
    presionar_para_continuar()

def buscar_productos_disponibles_menu():
    """Muestra productos disponibles (interactivo)"""
    print("\n✅ PRODUCTOS DISPONIBLES")
    print("-" * 30)
    resultados = buscar_productos_disponibles(productos)
    if resultados:
        print(f"📊 Total de productos disponibles: {len(resultados)}")
        for producto in resultados:
            print(f"   - {producto['nombre']} (Stock: {producto['stock']}, Precio: ${producto['precio']})")
    else:
        print("❌ No hay productos disponibles en este momento.")
    presionar_para_continuar()

def buscar_productos_rango_precio():
    """Busca productos por rango de precio (interactivo)"""
    print("\n💰 BUSCAR PRODUCTOS POR RANGO DE PRECIO")
    print("-" * 30)
    try:
        precio_min = validar_flotante("Ingrese el precio mínimo: ")
        precio_max = validar_flotante("Ingrese el precio máximo: ")
        
        if precio_min <= precio_max:
            resultados = buscar_productos_por_rango_precio(productos, precio_min, precio_max)
            if resultados:
                print(f"\n✅ Se encontraron {len(resultados)} productos entre ${precio_min} y ${precio_max}:")
                for producto in resultados:
                    print(f"   - {producto['nombre']}: ${producto['precio']} (Stock: {producto['stock']})")
            else:
                print(f"❌ No se encontraron productos entre ${precio_min} y ${precio_max}")
        else:
            print("❌ Error: El precio mínimo no puede ser mayor al precio máximo.")
    except ValueError:
        print("❌ Error: Ingrese valores numéricos válidos.")
    presionar_para_continuar()

def contar_productos_categoria_menu():
    """Muestra conteo de productos por categoría (interactivo)"""
    print("\n📊 CONTEO DE PRODUCTOS POR CATEGORÍA")
    print("-" * 30)
    conteo = contar_productos_por_categoria(productos)
    total_productos = len(productos)
    print(f"📈 Distribución de {total_productos} productos:")
    for categoria, cantidad in conteo.items():
        porcentaje = (cantidad / total_productos) * 100
        print(f"   - {categoria}: {cantidad} productos ({porcentaje:.1f}%)")
    presionar_para_continuar()

def buscar_empleado_id():
    """Busca empleado por ID (interactivo)"""
    print("\n🔍 BUSCAR EMPLEADO POR ID")
    print("-" * 30)
    id_buscado = validar_entero("Ingrese el ID del empleado: ")
    empleado = buscar_empleado_por_id(empleados, id_buscado)
    mostrar_empleado(empleado)
    presionar_para_continuar()

def buscar_empleado_nombre():
    """Busca empleado por nombre (interactivo)"""
    print("\n🔍 BUSCAR EMPLEADO POR NOMBRE")
    print("-" * 30)
    nombre = input("Ingrese el nombre completo (ej: Ana García): ").strip()
    if nombre:
        empleado = buscar_empleado_por_nombre_completo(empleados, nombre)
        mostrar_empleado(empleado)
    else:
        print("❌ Error: Debe ingresar un nombre válido.")
    presionar_para_continuar()

def buscar_empleados_departamento():
    """Busca empleados por departamento (interactivo)"""
    print("\n🏢 BUSCAR EMPLEADOS POR DEPARTAMENTO")
    print("-" * 30)
    print("Departamentos disponibles: Ventas, Técnico, Inventario, Administración")
    departamento = input("Ingrese el departamento: ").strip()
    if departamento:
        resultados = buscar_empleados_por_departamento(empleados, departamento)
        if resultados:
            print(f"\n✅ Se encontraron {len(resultados)} empleados en '{departamento}':")
            for empleado in resultados:
                estado = "Activo" if empleado['activo'] else "Inactivo"
                print(f"   - {empleado['nombre']} {empleado['apellido']} (${empleado['salario']:,}) - {estado}")
        else:
            print(f"❌ No se encontraron empleados en el departamento '{departamento}'")
    else:
        print("❌ Error: Debe ingresar un departamento válido.")
    presionar_para_continuar()

def buscar_empleados_activos_menu():
    """Muestra empleados activos (interactivo)"""
    print("\n✅ EMPLEADOS ACTIVOS")
    print("-" * 30)
    resultados = buscar_empleados_activos(empleados)
    if resultados:
        print(f"📊 Total de empleados activos: {len(resultados)}")
        for empleado in resultados:
            print(f"   - {empleado['nombre']} {empleado['apellido']} ({empleado['departamento']}) - ${empleado['salario']:,}")
    else:
        print("❌ No hay empleados activos.")
    presionar_para_continuar()

def listar_todos_empleados():
    """Lista todos los empleados (interactivo)"""
    print("\n📋 LISTA COMPLETA DE EMPLEADOS")
    print("-" * 30)
    if empleados:
        print(f"📊 Total de empleados: {len(empleados)}")
        for empleado in empleados:
            estado = "✅ Activo" if empleado['activo'] else "❌ Inactivo"
            print(f"   - {empleado['nombre']} {empleado['apellido']} | {empleado['departamento']} | ${empleado['salario']:,} | {estado}")
    else:
        print("❌ No hay empleados registrados.")
    presionar_para_continuar()

def mostrar_estadisticas():
    """Muestra estadísticas del sistema"""
    print("\n📊 ESTADÍSTICAS DEL SISTEMA")
    print("-" * 30)
    
    # Estadísticas de productos
    productos_disponibles = buscar_productos_disponibles(productos)
    productos_sin_stock = [p for p in productos if p['stock'] == 0]
    valor_inventario = sum(p['precio'] * p['stock'] for p in productos)
    
    print("📦 ESTADÍSTICAS DE PRODUCTOS:")
    print(f"   • Total de productos: {len(productos)}")
    print(f"   • Productos disponibles: {len(productos_disponibles)}")
    print(f"   • Productos sin stock: {len(productos_sin_stock)}")
    print(f"   • Valor total del inventario: ${valor_inventario:,.2f}")
    
    # Conteo por categoría de productos
    conteo_categorias = contar_productos_por_categoria(productos)
    print("   • Distribución por categoría:")
    for categoria, cantidad in conteo_categorias.items():
        print(f"     - {categoria}: {cantidad}")
    
    print("\n👥 ESTADÍSTICAS DE EMPLEADOS:")
    empleados_activos = buscar_empleados_activos(empleados)
    empleados_inactivos = len(empleados) - len(empleados_activos)
    salario_promedio = sum(e['salario'] for e in empleados) / len(empleados) if empleados else 0
    
    print(f"   • Total de empleados: {len(empleados)}")
    print(f"   • Empleados activos: {len(empleados_activos)}")
    print(f"   • Empleados inactivos: {empleados_inactivos}")
    print(f"   • Salario promedio: ${salario_promedio:,.2f}")
    
    # Conteo por departamento
    departamentos = {}
    for empleado in empleados:
        depto = empleado['departamento']
        if depto in departamentos:
            departamentos[depto] += 1
        else:
            departamentos[depto] = 1
    
    print("   • Distribución por departamento:")
    for departamento, cantidad in departamentos.items():
        print(f"     - {departamento}: {cantidad}")
    
    presionar_para_continuar()

# ===============================
# INICIO DEL PROGRAMA
# ===============================

if __name__ == "__main__":
    print("🚀 Iniciando Sistema Integrado de Búsqueda...")
    menu_principal()
    
#¿Cuál es la complejidad temporal ?
# La complejidad temporal de las funciones de búsqueda y filtrado en este código es generalmente O(n), donde n es el número de productos en la lista. 
#Esto se debe a que la mayoría de las funciones recorren la lista completa de productos una vez para aplicar los criterios de búsqueda o filtrado. 
#Algunas funciones que implican ordenamiento, como obtener los productos más caros o más baratos, tienen una complejidad temporal de O(n log n) debido al proceso de ordenamiento.

# ¿En qué casos la búsqueda lineal es eficiente?
# La búsqueda lineal es eficiente cuando se trabaja con listas pequeñas o cuando los datos no están ordenados. 
#También es útil cuando se necesita realizar búsquedas simples y rápidas sin la sobrecarga de estructuras de datos más complejas.

#¿Cuándo sería mejor usar otro algoritmo de búsqueda?
# Sería mejor usar otro algoritmo de búsqueda, como la búsqueda binaria, cuando la lista de productos está ordenada y es grande. 
# La búsqueda binaria tiene una complejidad temporal de O(log n), lo que la hace mucho más eficiente para grandes conjuntos de datos en comparación con la búsqueda lineal. 
# Además, para búsquedas frecuentes, podría ser beneficioso utilizar estructuras de datos como tablas hash o árboles balanceados para mejorar la eficiencia de las búsquedas.
