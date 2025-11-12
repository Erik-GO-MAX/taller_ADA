from typing import List, Dict, Any, Optional

# Datos de ejemplo (lista de diccionarios)
productos: List[Dict[str, Any]] = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]


# --- Helpers ---

def _normalize(s: Optional[str]) -> str:
    """Devuelve cadena en minúsculas o cadena vacía si None."""
    return (s or "").lower()


def _find(iterable, predicate):
    """Next con fallback None."""
    return next((x for x in iterable if predicate(x)), None)


# --- Búsquedas básicas (versión funcional) ---

def buscar_producto_por_nombre(productos: List[Dict[str, Any]], nombre_buscado: str) -> Optional[Dict[str, Any]]:
    """Búsqueda exacta por nombre (case-insensitive)."""
    nb = _normalize(nombre_buscado)
    return _find(productos, lambda p: _normalize(p.get('nombre')) == nb)


def buscar_producto_por_id(productos: List[Dict[str, Any]], id_buscado: int) -> Optional[Dict[str, Any]]:
    """Búsqueda por ID usando next."""
    return _find(productos, lambda p: p.get('id') == id_buscado)


def buscar_productos_por_categoria(productos: List[Dict[str, Any]], categoria_buscada: str) -> List[Dict[str, Any]]:
    """Devuelve todos los productos cuya categoría coincide (case-insensitive)."""
    cb = _normalize(categoria_buscada)
    return list(filter(lambda p: _normalize(p.get('categoria')) == cb, productos))


def buscar_productos_por_marca(productos: List[Dict[str, Any]], marca_buscada: str) -> List[Dict[str, Any]]:
    """Devuelve todos los productos de una marca (case-insensitive)."""
    mb = _normalize(marca_buscada)
    return [p for p in productos if _normalize(p.get('marca')) == mb]


def buscar_productos_disponibles(productos: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Productos con stock>0 y disponible == True."""
    return [p for p in productos if p.get('disponible') and p.get('stock', 0) > 0]


def buscar_productos_con_filtros(productos: List[Dict[str, Any]], **filtros) -> List[Dict[str, Any]]:
    """Aplica múltiples filtros; los strings se comparan case-insensitive.

    Ejemplo: buscar_productos_con_filtros(productos, marca='Apple', categoria='Smartphone')
    """

    def cumple(p: Dict[str, Any]) -> bool:
        for clave, valor in filtros.items():
            if clave not in p:
                return False
            v_producto = p[clave]
            if isinstance(valor, str) and isinstance(v_producto, str):
                if _normalize(v_producto) != _normalize(valor):
                    return False
            else:
                if v_producto != valor:
                    return False
        return True

    return [p for p in productos if cumple(p)]


def resumen_por_categoria(productos: List[Dict[str, Any]]) -> Dict[str, int]:
    """Cuenta productos por categoría."""
    resumen: Dict[str, int] = {}
    for p in productos:
        cat = p.get('categoria', '')
        resumen[cat] = resumen.get(cat, 0) + 1
    return resumen


# --- Pruebas / Ejecución (separadas con guardia) ---
if __name__ == "__main__":
    print("=== PRUEBAS DE BÚSQUEDA LINEAL EN PRODUCTOS ===\n")

    print("1. Búsqueda por nombre:")
    r = buscar_producto_por_nombre(productos, "MacBook Air M3")
    print(f"   Buscando 'MacBook Air M3': {r}\n")

    print("2. Búsqueda por ID:")
    r = buscar_producto_por_id(productos, 2)
    print(f"   Buscando ID 2: {r}\n")

    print("3. Búsqueda por categoría:")
    res = buscar_productos_por_categoria(productos, "Laptop")
    print("   Productos en categoría 'Laptop':")
    for prod in res:
        print(f"   - {prod['nombre']} (${prod['precio']})")

    print("\n4. Búsqueda por marca:")
    res = buscar_productos_por_marca(productos, "Apple")
    print("   Productos de marca 'Apple':")
    for prod in res:
        print(f"   - {prod['nombre']} (${prod['precio']})")

    print("\n5. Productos disponibles:")
    res = buscar_productos_disponibles(productos)
    print("   Productos con stock disponible:")
    for prod in res:
        print(f"   - {prod['nombre']} (Stock: {prod['stock']})")

    print("\n6. Búsquedas sin resultados:")
    r = buscar_producto_por_nombre(productos, "Producto Inexistente")
    print(f"   Buscando 'Producto Inexistente': {r}")

    r = buscar_producto_por_id(productos, 99)
    print(f"   Buscando ID 99: {r}")

    print("\n7. Búsqueda con filtros múltiples:")
    res = buscar_productos_con_filtros(productos, marca='Apple', categoria='Smartphone')
    print("   Productos Apple en categoría Smartphone:")
    for prod in res:
        print(f"   - {prod['nombre']}")

    print("\nResumen por categoría:")
    for cat, cnt in resumen_por_categoria(productos).items():
        print(f"   - {cat}: {cnt} producto(s)")
