import random

# Datos predefinidos
nombres = ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro', 'Lucía', 'Jorge', 'Sofía', 'Pablo', 'Julia']
departamentos = ['Ventas', 'TI', 'Recursos Humanos', 'Marketing']

# Función para generar empleados aleatorios
def generar_empleados(num_empleados):
    empleados = []
    ids_empleados = set()  # ID únicos
    while len(empleados) < num_empleados:
        id_empleado = random.randint(1000, 9999)
        if id_empleado not in ids_empleados:
            ids_empleados.add(id_empleado)
            nombre = random.choice(nombres)
            edad = random.randint(18, 65)
            departamento = random.choice(departamentos)
            salario = random.randint(30000, 100000)
            empleado = (id_empleado, nombre, edad, departamento, salario)
            empleados.append(empleado)
    return empleados

# Funciones CRUD
def crear_empleado(lista_empleados, dicc_departamentos, empleado):
    lista_empleados.append(empleado)
    id_empleado, _, _, departamento, _ = empleado
    if departamento in dicc_departamentos:
        dicc_departamentos[departamento].add(id_empleado)
    else:
        dicc_departamentos[departamento] = {id_empleado}

def leer_empleado(lista_empleados, id_empleado):
    for empleado in lista_empleados:
        if empleado[0] == id_empleado:
            return empleado
    return None

def actualizar_empleado(lista_empleados, dicc_departamentos, id_empleado, campo, valor):
    for i, empleado in enumerate(lista_empleados):
        if empleado[0] == id_empleado:
            empleado = list(empleado)
            if campo == 'nombre':
                empleado[1] = valor
            elif campo == 'edad':
                empleado[2] = valor
            elif campo == 'departamento':
                # Actualizar diccionario de departamentos si se cambia el departamento
                dicc_departamentos[empleado[3]].remove(id_empleado)
                empleado[3] = valor
                if valor in dicc_departamentos:
                    dicc_departamentos[valor].add(id_empleado)
                else:
                    dicc_departamentos[valor] = {id_empleado}
            elif campo == 'salario':
                empleado[4] = valor
            lista_empleados[i] = tuple(empleado)
            break

def eliminar_empleado(lista_empleados, dicc_departamentos, id_empleado):
    for empleado in lista_empleados:
        if empleado[0] == id_empleado:
            lista_empleados.remove(empleado)
            dicc_departamentos[empleado[3]].remove(id_empleado)
            break

# Estadísticas de salarios mayores a 80,000
def ids_salarios_altos(lista_empleados):
    return frozenset([empleado[0] for empleado in lista_empleados if empleado[4] > 80000])

# Generación de datos aleatorios
empleados = generar_empleados(20)

# Diccionario para departamentos y set de IDs de empleados por departamento
dicc_departamentos = {}
for empleado in empleados:
    id_empleado, _, _, departamento, _ = empleado
    if departamento not in dicc_departamentos:
        dicc_departamentos[departamento] = {id_empleado}
    else:
        dicc_departamentos[departamento].add(id_empleado)

# Frozenset de empleados con salarios superiores a 80,000
salarios_altos = ids_salarios_altos(empleados)

# Mostrar resultados en la terminal
print("Lista de empleados generados:")
for empleado in empleados:
    print(empleado)

print("\nDiccionario de departamentos y IDs de empleados:")
for departamento, ids in dicc_departamentos.items():
    print(f"{departamento}: {ids}")

print("\nFrozenset de empleados con salarios superiores a 80,000:")
print(salarios_altos)

# CRUD Implementación

# 1. Crear un nuevo empleado
nuevo_empleado = (1234, 'María', 30, 'TI', 45000)
crear_empleado(empleados, dicc_departamentos, nuevo_empleado)
print("\nDespués de crear un nuevo empleado:")
for empleado in empleados:
    print(empleado)

# 2. Leer los datos del empleado creado
empleado = leer_empleado(empleados, 1234)
print(f"\nDatos del empleado leído: {empleado}")

# 3. Actualizar el salario del empleado
actualizar_empleado(empleados, dicc_departamentos, 1234, 'salario', 50000)
print(f"\nDespués de actualizar el salario: {leer_empleado(empleados, 1234)}")

# 4. Eliminar al empleado
eliminar_empleado(empleados, dicc_departamentos, 1234)
print(f"\nDespués de eliminar el empleado:")
for empleado in empleados:
    print(empleado)

print("\nDiccionario de departamentos y IDs de empleados actualizado:")
for departamento, ids in dicc_departamentos.items():
    print(f"{departamento}: {ids}")