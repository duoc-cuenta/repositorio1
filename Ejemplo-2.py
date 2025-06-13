"""
Construir un menu interactivo que permita gestionar productos de un listado.
Un producto tiene las siguientes caracteristicas:
 - Codigo: 1
 - Descripccion: 'Mesa de centro'
 - "Precio": 45999
 - Cantidad: 50

 Operaciones del menu:
 1. Registrar producto 
 2. Buscar producto por codigo
 3. Imprimir productos
 4. Editar productos (Descripcion|Precio|Cantidad)
 5. Eliminar producto por codigo
"""
import os
lista_de_productos = []



while True :

    print("Operaciones del menu.")
    print("1. Registrar producto.") 
    print("2. Buscar producto por codigo.")
    print("3. Imprimir productos.")
    print("4. Editar productos.") 
    print("5. Eliminar producto por codigo.")

    opcion = int(input("Ingrese una opcion: "))
    os.system("cls")

    if opcion == 1:
        print("-" * 85)
        print("\t\t\t""Registrar un producto")
        print("-" * 85)
        codigo = int(input("ingrese codigo del producto: "))
        descripcion = input("Ingrese una descripccion: ")
        precio = input("Ingrese precio del producto: ")
        cantidad = input("Ingrese cantidad de producto: ")
    
        os.system("cls")

        diccionario = {"codigo": codigo,
                       "Descripccion": descripcion,
                       "Precio": precio,
                       "Cantidad": cantidad}
        
        lista_de_productos.append(diccionario)
        for productos in diccionario:
            print(f"{productos}: {diccionario[productos]}")

    elif opcion == 2:
        print("-" * 85)
        print("\t\t\t"" Buscar producto por codigo")
        print("-" * 85)
        codigo_buscado = int(input("Ingrese el numero del codigo que busca: "))
        os.system("cls")
        for productos in lista_de_productos:
            print(f"{productos["codigo"]}")
            if productos["codigo"] == lista_de_productos:
                print("producto encontrado ")
            
           # if codigo_buscado == codigo in lista_de_productos:
            #    print("Esta el producto")