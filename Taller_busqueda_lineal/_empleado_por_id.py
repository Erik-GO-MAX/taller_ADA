# Datos de ejemplo
empleados = [
	{'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
	{'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
	{'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
	{'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True},
	{'id': 105, 'nombre': 'Laura', 'apellido': 'Hernández', 'departamento': 'Técnico', 'salario': 45000, 'activo': True},
	{'id': 106, 'nombre': 'Pedro', 'apellido': 'Gómez', 'departamento': 'Administración', 'salario': 32000, 'activo': False}
]

from collections import Counter
from typing import List, Dict, Any, Optional


def buscar_empleado_por_id(empleados: List[Dict[str, Any]], id_buscado: int) -> Optional[Dict[str, Any]]:
	"""Busca un empleado por su ID y devuelve el diccionario o None."""
	return next((e for e in empleados if e.get('id') == id_buscado), None)


def buscar_empleado_por_nombre_completo(empleados: List[Dict[str, Any]], nombre_completo: str) -> Optional[Dict[str, Any]]:
	"""Busca por nombre completo. Coincide con exacto o con las dos primeras partes."""
	target = nombre_completo.strip().lower()
	partes = target.split()

	def nombre_empleado_lower(e: Dict[str, Any]) -> str:
		return f"{e.get('nombre','')} {e.get('apellido','') }".lower().strip()

	for e in empleados:
		ne = nombre_empleado_lower(e)
		if ne == target:
			return e
		if len(partes) >= 2:
			if e.get('nombre','').lower() == partes[0] and e.get('apellido','').lower() == partes[1]:
				return e
	return None


def buscar_empleados_por_departamento(empleados: List[Dict[str, Any]], departamento_buscado: str) -> List[Dict[str, Any]]:
	"""Devuelve empleados cuyo campo 'departamento' coincide (case-insensitive)."""
	dep = departamento_buscado.lower()
	return [e for e in empleados if (e.get('departamento') or '').lower() == dep]


def buscar_empleados_activos(empleados: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
	"""Devuelve empleados con 'activo' True."""
	return [e for e in empleados if e.get('activo')]


def buscar_empleados_por_rango_salario(empleados: List[Dict[str, Any]], salario_min: int, salario_max: int) -> List[Dict[str, Any]]:
	"""Devuelve empleados con salario entre salario_min y salario_max (inclusive)."""
	return [e for e in empleados if salario_min <= e.get('salario', 0) <= salario_max]


def buscar_empleados_por_nombre_o_apellido(empleados: List[Dict[str, Any]], texto_buscado: str) -> List[Dict[str, Any]]:
	"""Búsqueda parcial en nombre o apellido (case-insensitive)."""
	t = texto_buscado.lower()
	return [e for e in empleados if t in e.get('nombre','').lower() or t in e.get('apellido','').lower()]


def obtener_resumen_departamentos(empleados: List[Dict[str, Any]]) -> Dict[str, int]:
	"""Cuenta empleados por departamento usando Counter."""
	return dict(Counter(e.get('departamento','') for e in empleados))


def buscar_empleados_avanzado(empleados: List[Dict[str, Any]], **criterios) -> List[Dict[str, Any]]:
	"""Búsqueda avanzada con criterios: salario_min, salario_max, nombre_contiene, apellido_contiene, y comparaciones directas."""
	resultados: List[Dict[str, Any]] = []

	for e in empleados:
		ok = True
		for criterio, valor in criterios.items():
			if criterio == 'salario_min':
				if e.get('salario', 0) < valor:
					ok = False
					break
			elif criterio == 'salario_max':
				if e.get('salario', 0) > valor:
					ok = False
					break
			elif criterio == 'nombre_contiene':
				if valor.lower() not in e.get('nombre','').lower():
					ok = False
					break
			elif criterio == 'apellido_contiene':
				if valor.lower() not in e.get('apellido','').lower():
					ok = False
					break
			elif criterio in e:
				# comparación directa: si es string, ignore case
				if isinstance(valor, str) and isinstance(e.get(criterio), str):
					if e.get(criterio,'').lower() != valor.lower():
						ok = False
						break
				else:
					if e.get(criterio) != valor:
						ok = False
						break
			else:
				ok = False
				break
		if ok:
			resultados.append(e)

	return resultados


if __name__ == '__main__':
	# Pruebas de las funciones (misma salida esperada que el original)
	print('=== PRUEBAS DE BÚSQUEDA EN EMPLEADOS ===\n')

	# Prueba 1: Búsqueda por ID
	print('1. Búsqueda por ID:')
	resultado = buscar_empleado_por_id(empleados, 102)
	print(f"   Buscando ID 102: {resultado}\n")

	# Prueba 2: Búsqueda por nombre completo
	print('2. Búsqueda por nombre completo:')
	resultado = buscar_empleado_por_nombre_completo(empleados, 'Ana García')
	if resultado:
		print(f"   Buscando 'Ana García': {resultado['nombre']} {resultado['apellido']} - {resultado['departamento']}")

	resultado = buscar_empleado_por_nombre_completo(empleados, 'Carlos López')
	if resultado:
		print(f"   Buscando 'Carlos López': {resultado['nombre']} {resultado['apellido']} - {resultado['departamento']}\n")

	# Prueba 3: Búsqueda por departamento
	print('3. Búsqueda por departamento:')
	resultados = buscar_empleados_por_departamento(empleados, 'Ventas')
	print("   Empleados en departamento 'Ventas':")
	for empleado in resultados:
		estado = 'Activo' if empleado['activo'] else 'Inactivo'
		print(f"   - {empleado['nombre']} {empleado['apellido']} (${empleado['salario']}) - {estado}")

	# Prueba 4: Empleados activos
	print('\n4. Empleados activos:')
	resultados = buscar_empleados_activos(empleados)
	print('   Lista de empleados activos:')
	for empleado in resultados:
		print(f"   - {empleado['nombre']} {empleado['apellido']} ({empleado['departamento']})")

	# Prueba 5: Rango salarial
	print('\n5. Búsqueda por rango salarial:')
	resultados = buscar_empleados_por_rango_salario(empleados, 35000, 40000)
	print('   Empleados con salario entre $35,000 y $40,000:')
	for empleado in resultados:
		print(f"   - {empleado['nombre']} {empleado['apellido']}: ${empleado['salario']:,}")

	# Prueba 6: Búsqueda parcial
	print('\n6. Búsqueda parcial por nombre/apellido:')
	resultados = buscar_empleados_por_nombre_o_apellido(empleados, 'Garc')
	print("   Empleados que contienen 'Garc' en nombre o apellido:")
	for empleado in resultados:
		print(f"   - {empleado['nombre']} {empleado['apellido']}")

	resultados = buscar_empleados_por_nombre_o_apellido(empleados, 'Mar')
	print("   Empleados que contienen 'Mar' en nombre o apellido:")
	for empleado in resultados:
		print(f"   - {empleado['nombre']} {empleado['apellido']}")

	# Prueba 7: Resumen
	print('\n7. Resumen por departamento:')
	resumen = obtener_resumen_departamentos(empleados)
	for departamento, cantidad in resumen.items():
		print(f"   - {departamento}: {cantidad} empleado(s)")

	# Prueba 8: Búsquedas sin resultados
	print('\n8. Búsquedas sin resultados:')
	resultado = buscar_empleado_por_id(empleados, 999)
	print(f"   Buscando ID 999: {resultado}")

	resultado = buscar_empleado_por_nombre_completo(empleados, 'Juan Pérez')
	print(f"   Buscando 'Juan Pérez': {resultado}")

	# Prueba 9: Búsqueda avanzada
	print('\n9. Búsqueda avanzada:')
	resultados = buscar_empleados_avanzado(empleados, departamento='Técnico', activo=True)
	print('   Empleados técnicos activos:')
	for empleado in resultados:
		print(f"   - {empleado['nombre']} {empleado['apellido']} (${empleado['salario']:,})")

	resultados = buscar_empleados_avanzado(empleados, salario_min=40000, activo=True)
	print('\n   Empleados activos con salario >= $40,000:')
	for empleado in resultados:
		print(f"   - {empleado['nombre']} {empleado['apellido']} (${empleado['salario']:,})")

