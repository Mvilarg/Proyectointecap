# Declarar variables para almacenar productos, precios, descuentos y cantidades
productos = {
    "1": {"nombre": "Camisa", "precio": 90.0, "cantidad": 10},
    "2": {"nombre": "Pantalon", "precio": 200.0, "cantidad": 15},
    "3": {"nombre": "Zapato", "precio": 350.0, "cantidad": 20}
}

descuentos = {
    "10%": 0.1,
    "20%": 0.2
}

# Función para mostrar los productos disponibles
def mostrar_productos():
    print("Productos disponibles:")
    for key, value in productos.items():
        print(f"{key}. {value['nombre']} - Q{value['precio']}")

# Función para agregar productos al carrito
def agregar_producto(carrito):
    mostrar_productos()
    producto = input("Ingrese el número del producto que desea agregar: ")
    if producto in productos:
        cantidad = int(input("Ingrese la cantidad que desea agregar: "))
        if cantidad <= productos[producto]["cantidad"]:
            carrito.append({"producto": producto, "cantidad": cantidad})
            productos[producto]["cantidad"] -= cantidad
            print("Producto agregado al carrito con éxito.")
        else:
            print("No hay suficiente stock para agregar la cantidad deseada.")
    else:
        print("Producto no encontrado.")

# Función para mostrar el carrito
def mostrar_carrito(carrito):
    print("Carrito:")
    total = 0
    for producto in carrito:
        nombre = productos[producto["producto"]]["nombre"]
        precio = productos[producto["producto"]]["precio"]
        cantidad = producto["cantidad"]
        subtotal = precio * cantidad
        total += subtotal
        print(f"{nombre} x {cantidad} = ${subtotal:.2f}")
    print(f"Total: Q{total:.2f}")

# Función para aplicar descuentos
def aplicar_descuento(carrito):
    total = 0
    for producto in carrito:
        precio = productos[producto["producto"]]["precio"]
        cantidad = producto["cantidad"]
        subtotal = precio * cantidad
        total += subtotal
    print("Descuentos disponibles:")
    for key, value in descuentos.items():
        print(f"{key} - {value*100}%")
    descuento = input("Ingrese el descuento que desea aplicar: ")
    if descuento in descuentos:
        total *= (1 - descuentos[descuento])
        print(f"Descuento aplicado con éxito. Total: Q{total:.2f}")
    else:
        print("Descuento no encontrado.")

# Función para procesar el pago
def procesar_pago(carrito, descuento_aplicado=0):
    total = 0
    for producto in carrito:
        precio = productos[producto["producto"]]["precio"]
        cantidad = producto["cantidad"]
        subtotal = precio * cantidad
        total += subtotal
    total_con_descuento = total * (1 - descuento_aplicado)
    print(f"Total a pagar con descuento: Q{total_con_descuento:.2f}")
    pago = float(input("Ingrese el monto del pago: "))
    if pago >= total_con_descuento:
        print("Pago procesado con éxito.")
        # Save the discount and total paid to a file
        with open("ventas.txt", "a") as f:
            f.write(f"Venta: {', '.join([productos[producto['producto']]['nombre'] for producto in carrito])}\n")
            f.write(f"Total pagado: Q{total_con_descuento:.2f}\n")
            f.write(f"Descuento aplicado: {descuento_aplicado*100}%\n\n")
    else:
        print("Monto insuficiente para pagar.")

# Función para aplicar descuentos
def aplicar_descuento(carrito):
    total = 0
    for producto in carrito:
        precio = productos[producto["producto"]]["precio"]
        cantidad = producto["cantidad"]
        subtotal = precio * cantidad
        total += subtotal
    print("Descuentos disponibles:")
    for key, value in descuentos.items():
        print(f"{key} - {value*100}%")
    descuento = input("Ingrese el descuento que desea aplicar: ")
    if descuento in descuentos:
        descuento_aplicado = descuentos[descuento]
        print(f"Descuento aplicado con éxito. Total con descuento: Q{(total * (1 - descuento_aplicado)):.2f}")
        return descuento_aplicado
    else:
        print("Descuento no encontrado.")
        return 0

# Función para generar el reporte
def generar_reporte(carrito, cliente):
    with open("reporte.txt", "w") as f:
        f.write("Resumen de compras:\n")
        total = 0
        for producto in carrito:
            nombre = productos[producto["producto"]]["nombre"]
            precio = productos[producto["producto"]]["precio"]
            cantidad = producto["cantidad"]
            subtotal = precio * cantidad
            total += subtotal
            f.write(f"{nombre} x {cantidad} = Q{subtotal:.2f}\n")
        f.write(f"Total pagado: Q{total:.2f}\n")
        f.write(f"Cliente: {cliente}\n")
        f.write("Inventario:\n")
        for key, value in productos.items():
            f.write(f"{value['nombre']} - {value['cantidad']} unidades\n")

# Programa principal
def main():
    carrito = []
    cliente = input("Ingrese su nombre: ")
    while True:
        print("1. Agregar producto al carrito")
        print("2. Mostrar carrito")
        print("3. Aplicar descuento")
        print("4. Procesar pago")
        print("5. Salir")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            agregar_producto(carrito)
        elif opcion == "2":
            mostrar_carrito(carrito)
        elif opcion == "3":
            descuento_aplicado = aplicar_descuento(carrito)
        elif opcion == "4":
            procesar_pago(carrito, descuento_aplicado)
        elif opcion == "5":
            generar_reporte(carrito, cliente)
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()