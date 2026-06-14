# Un módulo es simplemente un archivo con extensión .py que contiene código de Python (funciones, clases, variables, etc.).
print ("\033c")
def borrarpantalla():
      print("\033c")
def funcion1():
      nombre=input("nombre: ").strip().upper()
      apellido=input("apellido: ").strip().upper()
      print(f"El nombre del alumno es: {nombre} {apellido}")

 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):
      nombre=nom
      apellido=ape
      print(f"El nombre del alumno es: {nombre} {apellido}")
      return nombre,apellido
 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
      nombre=input("nombre: ").strip().upper()
      apellido=input("apellido: ").strip().upper()
      return nombre,apellido
 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
      nombre=nom
      apellido=ape
      return nombre,apellido
nom,ape=funcion4("juan","perez")
print(f"El nombre del alumno es: {nom} {ape}")
