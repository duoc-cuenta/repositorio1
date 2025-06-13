opcion = 0
productos = []
prod=[]
description=[]


diccionario = {
    "codigo": 1,
    "descripcion": "",
    "precio": 200000,
    "cantidad": 10,
}
while opcion != 5:
    print("1. Agregar producto")
    print("2. Modificar producto")
    print("3. Eliminar producto")
    print("4. Listar productos")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        diccionario["codigo"] = int(input("Ingrese el código del producto: "))
        diccionario["descripcion"] = input("Ingrese la descripción del producto: ")
        diccionario["precio"] = float(input("Ingrese el precio del producto: "))
        diccionario["cantidad"] = int(input("Ingrese la cantidad del producto: "))
        productos.append(diccionario.copy())
    
    elif opcion == 2:
        codigo_modificar = int(input("Ingrese el código del producto a modificar: "))
        for prod in productos:
            if prod["codigo"] == codigo_modificar:
                prod["descripcion"] = input("Ingrese la nueva descripción: ")
                prod["precio"] = float(input("Ingrese el nuevo precio: "))
                prod["cantidad"] = int(input("Ingrese la nueva cantidad: "))
                break
    
    elif opcion == 3:
        codigo_eliminar = int(input("Ingrese el código del producto a eliminar: "))
        print("seguro que desea eliminar el producto con código", codigo_eliminar, "? (si/no)")
        confirmacion = input().strip().lower()
        if confirmacion == "si":
            print("producto eliminado con éxito.")
        else:
            print("Operación cancelada.")
            continue

        productos = [prod for prod in productos if prod["codigo"] != codigo_eliminar]
    
    elif opcion == 4:
        for prod in productos:
            print(prod)
            if not productos:
                print("No hay productos registrados.")
    
    
    elif opcion == 5:
        print("Saliendo del programa.")
        import time
        import sys
        tiempo_espera = 2
        time.sleep(tiempo_espera)
        print("gracias por usar el programa.")
        sys.exit()

        
    
    else:
        print("Opción no válida, por favor intente de nuevo.")

    if opcion < 1 or opcion > 5:
        print("Opción no válida, por favor intente de nuevo.")
    print("")


