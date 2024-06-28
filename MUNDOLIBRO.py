import json
import os

#nombre:str,credito:int

""""def agregarCliente():
    with open("biblioteca.json", mode = "r") as lecturaJson:
        leerJason= json.load(lecturaJson)  

        categoria_nueva= {
            "CategoriaID": len(leerJason["Categoria"])+ 1,
            "Nombre": "nombre",
        }

        leerJason["Categoria"].append(categoria_nueva)

    with open("biblioteca.json", mode = "w") as escrituraJson:
        json.dump(leerJason, escrituraJson, indent= 4)

        print("cliente agregado correctamente")"""

#agregarCliente()

def editar_categoria():
    contador = 0
    with open("biblioteca.json", mode = "r") as lecturaJson:
        leerJason= json.load(lecturaJson)
        for i in leerJason["Categoria"]:

            if i["Nombre"] == nombreN:
                print("encontrado")
                break
            contador+= 1
        leerJason["Categoria"]["Nombre"]= nombreN= input("Ingresa un nombre: ")
        
    with open("biblioteca.json", mode = "w") as escrituraJson:
        json.dump(leerJason, escrituraJson, indent= 4)
        print("cliente editado correctamente")  

editar_categoria()
    
#def eliminar_categoria():

#def buscar_categoria():
