# Diccionario inicial

videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 10
    },

    "VG002": {
        "nombre": "Zelda: Breath of the Wild",
        "plataforma": "Nintendo Switch",
        "precio": 220000,
        "cantidad": 5
    },

    "VG003": {
        "nombre": "Forza Horizon 5",
        "plataforma": "Xbox Series X",
        "precio": 210000,
        "cantidad": 8
    }
}


# Función para mostrar inventario

def mostrar_inventario(videojuegos):

    print("\n===== INVENTARIO =====")

    for codigo, datos in videojuegos.items():

        print(f"\nCódigo: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Plataforma: {datos['plataforma']}")
        print(f"Precio: ${datos['precio']}")
        print(f"Cantidad: {datos['cantidad']}")


# Función para buscar videojuego

def buscar_videojuego(videojuegos):

    codigo = input("\nIngrese el código a buscar: ")

    if codigo in videojuegos:

        print("\nVideojuego encontrado")
        print("Nombre:", videojuegos[codigo]["nombre"])
        print("Plataforma:", videojuegos[codigo]["plataforma"])
        print("Precio:", videojuegos[codigo]["precio"])
        print("Cantidad:", videojuegos[codigo]["cantidad"])

    else:

        print("El videojuego no existe")

def agregar_videojuego(videojuegos):

    codigo = input("\nIngrese el código: ")

    if codigo in videojuegos:
        print("Ese código ya existe")
        return

    nombre = input("Ingrese el nombre: ")

    plataforma = input("Ingrese la plataforma: ")

    precio = int(input("Ingrese el precio: "))

    cantidad = int(input("Ingrese la cantidad: "))

    if precio <= 0 or cantidad <= 0:
        print("Precio y cantidad deben ser mayores a cero")
        return

    videojuegos[codigo] = {
        "nombre": nombre,
        "plataforma": plataforma,
        "precio": precio,
        "cantidad": cantidad
    }

    print("Videojuego agregado correctamente")
# Función para actualizar precio

def actualizar_precio(videojuegos):

    codigo = input("\nIngrese el código del videojuego: ")

    if codigo in videojuegos:

        nuevo_precio = int(input("Ingrese el nuevo precio: "))

        if nuevo_precio > 0:

            videojuegos[codigo]["precio"] = nuevo_precio

            print("Precio actualizado correctamente")

        else:

            print("El precio debe ser mayor que cero")

    else:

        print("El videojuego no existe")

# Función para registrar venta
def registrar_venta(videojuegos):

    codigo = input("\nIngrese el código del videojuego: ")

    if codigo in videojuegos:

        cantidad_vender = int(input("Ingrese cantidad a vender: "))

        if cantidad_vender <= videojuegos[codigo]["cantidad"]:

            total = cantidad_vender * videojuegos[codigo]["precio"]

            videojuegos[codigo]["cantidad"] -= cantidad_vender

            print("\nFactura")
            print("-------")
            print("Juego:", videojuegos[codigo]["nombre"])
            print("Precio unitario:", videojuegos[codigo]["precio"])
            print("Cantidad:", cantidad_vender)
            print("Total:", total)

        else:
            print("No hay inventario suficiente")

    else:
        print("El videojuego no existe")


# Función para mostrar estadísticas
def mostrar_estadisticas(videojuegos):

    total_videojuegos = len(videojuegos)

    valor_total = 0

    juego_mas_costoso = ""
    precio_mayor = 0

    juego_mayor_cantidad = ""
    cantidad_mayor = 0

    suma_precios = 0

    for codigo, datos in videojuegos.items():

        valor_total += datos["precio"] * datos["cantidad"]

        suma_precios += datos["precio"]

        if datos["precio"] > precio_mayor:
            precio_mayor = datos["precio"]
            juego_mas_costoso = datos["nombre"]

        if datos["cantidad"] > cantidad_mayor:
            cantidad_mayor = datos["cantidad"]
            juego_mayor_cantidad = datos["nombre"]

    promedio = suma_precios / total_videojuegos

    print("\n===== ESTADISTICAS =====")
    print("Total videojuegos:", total_videojuegos)
    print("Valor total inventario:", valor_total)
    print("Juego mas costoso:", juego_mas_costoso)
    print("Mayor cantidad disponible:", juego_mayor_cantidad)
    print("Promedio precios:", promedio)


# Función para eliminar videojuego
def eliminar_videojuego(videojuegos):

    codigo = input("\nIngrese el código a eliminar: ")

    if codigo in videojuegos:

        del videojuegos[codigo]

        print("Videojuego eliminado correctamente")

    else:

        print("El videojuego no existe")

def menu():

    print("\n===== TIENDA DE VIDEOJUEGOS =====")
    print("1. Agregar videojuego")
    print("2. Mostrar inventario")
    print("3. Buscar videojuego")
    print("4. Actualizar precio")
    print("5. Registrar venta")
    print("6. Mostrar estadísticas")
    print("7. Eliminar videojuego")
    print("8. Salir")
    
# Pruebas

mostrar_inventario(videojuegos)

buscar_videojuego(videojuegos)

agregar_videojuego(videojuegos)

mostrar_inventario(videojuegos)

actualizar_precio(videojuegos)

mostrar_inventario(videojuegos)

registrar_venta(videojuegos)

mostrar_inventario(videojuegos)

mostrar_estadisticas(videojuegos)

eliminar_videojuego(videojuegos)

mostrar_inventario(videojuegos)