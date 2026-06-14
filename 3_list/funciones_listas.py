"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""
print("\033c")

#Funciones más comunes en las listas
paises=["mexico", "canada", "america","españa","francia"]

# numeros=[23,45,8,24]

# varios=["hola",3.1416,True]

# vacia=[]
# #Imprimir el contenido de una lista
# print(paises)
# print(numeros)
# print(varios)
# print(vacia)
# print(type(paises))

# #Recorrer la lista 
# #1er forma 
# for i  in paises:
#     print(i)

# # #2do forma 
# for i in range(0,len(paises)): 
#     print(paises[i])


# #ordenar elementos de una lista
# paises=["mexico", "canada", "america","españa","francia"]
# paises.sort()
# print(paises)

# #dar la vuelta a una lista
# paises.reverse()
# print(paises)




# #Agregar, insertar, Añadir un elemento a una lista
# #1er forma 
# paises.append("francia")
# print(paises)

# #2da forma
# paises.insert(3,"italia")
# print(paises)
# paises.insert(4,"alemania")
# print(paises)
# #Eliminar, borrar, suprimir, un elemento de una lista
# #1er forma
# paises.pop(4)
# print(paises) 


# #2da forma 
# paises.remove("italia")
# print(paises)
# paises.pop(4)
# print(paises) 

# #Buscar un elemento dentro de la lista
# if "italia" in paises:
#  print(f"la respuesta es true")
# else:
#  print("la respuesta es false")

#Contar el numeros de veces que aparece un elemento dentro de una lista
numeros=[23,45,8,24,23,45,8,24,100,200,0,-1,10,23,24,8,23,50]
# print(numeros)
# num=int(input("ingresa un numero a buscar: "))
# cuantos= numeros.count(num)
# print(f"el numero de veces que aparece el {num} es: {cuantos}")




#Conocer la posicion o indice en el que se encuentra un elemento de la lista
posicion=paises.index("españa" )
print(f"la posicion del elemento es: {posicion}")



#Unir el contenido de una lista dentro de otra lista
numero=[23,45,8,24]
print(numero)
numeros2=[100,200,0,-1,10,23,24,8]
print(numeros2)
numero.extend(numeros2)
print(numeros)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenid ordenado descendentemente
numeros.sort()
numeros.reverse()
print(numeros)