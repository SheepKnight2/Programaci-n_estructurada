"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print("\033c")

# set1={"Python", "SQL", "Estructurado"}
# print(set1)

# for i in set1:
#     print(i)

# set2={"hola", True, 33, 3.1416}
# print(set2)

# set_respaldo=set2.copy()
# set2.clear()
# print(set2)


# set3={""}
# print(set3)

# set3.add("Hola")
# set3.add(3)
# set3.add(10.0)
# set3.add("3")
# print(set3)



# set3.pop()
# set3.pop()
# print(set3)
# set3.clear
# print(set3)
# set3.add("33")
# print(set3)

# lista=[10,9.5,8.5,3.5]
#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
# emails=[]

# resp="SI"
# while resp=="SI":
#    emails.append(input("email: ").strip())
#     #set_emails.add(input("Ingresa un email: ").lower().strip())
# resp=input("¿Deseas ingresar otro email (S/N)? ").upper().strip()
# print(emails)


#Solucion 2
# #Solucion 2
emails=[]

resp=True
while resp:
    emails.insert(0,input("Email: ").strip())
    resp=input("¿Deseas capturar otro email (Si/No)? ").upper().strip()
    if resp=="NO":
        resp=False

emails_set=set(emails)
emails=list(emails_set)
print(emails)


  



