global1 = 34

def cambiar_global(glo1):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1
    global1 = glo1
    pass
print(cambiar_global(98))



def anio_bisiesto(year):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''

    if(year % 4 ==0):
      if(year % 100 == 0):
        if(year % 400 == 0):
          return True
        else:
          return False
      else:
        return True
    else:
      return False
print(anio_bisiesto(2020))   



def contar_valles(arg):
    r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    cont = 0
    for a in range(len(arg)):
      if arg[a] == -1:
        i = a+1
        while i < len(arg):
          if arg[i] == -1:
            break
          elif arg[i] == 1:
            cont =  cont + 1
            break            
          i += 1
    return cont
arg = [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1]
print("valles: "  + str(contar_valles(arg)))

def saltando_rocas(rocas):
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    cont  = 0
    salto = 0
    while cont < len(rocas):
      if (cont + 2) <  len(rocas):
        if rocas[cont + 2] != 1:
          cont +=2
        elif rocas[cont + 1] != 1:
          cont +=1
      else: 
        break
      salto +=1
    return salto
    
rocas = [1,0,0,0]
print("cont: " + str(saltando_rocas(rocas)))

def pares_medias(lisPar):
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''
    diccionario ={}
    valor = []
    for aa in lisPar:
      diccionario.setdefault(aa,0)
    for ae in lisPar:
      diccionario[ae] += 1
    for ai in diccionario:
      diccionario[ai] = diccionario[ai]//2
      if diccionario[ai] == 0:
        valor.append(ai)
    for ao in valor:
      diccionario.pop(ao)
    return diccionario
lisPar = [1,2,3,4,4,3,6,7,3,2,9,7,1,5]
print(pares_medias(lisPar))
# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'
lis = [1,2,3,4]
class ListaComa:
  def __init__(self, lista):
    self.lista = lista
    self.res = ""
  def __str__(self):
    self.res =(str(self.lista).replace("[","")).replace("]","").replace(" ","")
    return self.res

prueba = ListaComa(lis)
prueba.__str__()
print(prueba.res)

# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'

nomb = ["jhon", "eduar"]
apell = ["cuellar", "Ballen"]
class Persona:
  nom = list()
  ape = list()
  def __init__(self, nombre, apellido):
    for a in range(len(nombre)):
      if(nombre[a].isalpha()):
        nombre[a] = nombre[a].capitalize()
      else:
        break
    for b in range(len(apellido)):
      if(apellido[b].isalpha()):
        apellido[b] = apellido[b].capitalize()
    self.nombres = nombre
    self.apellidos = apellido

  def nombre_completo(self):
    self.nombre = " ".join(self.nombres) + " " +" ".join(self.apellidos)
    return self.nombre

nomPersona = Persona(nomb,apell)
nomPersona.nombre_completo()
print(nomPersona.nombre)



# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.
import datetime
class Persona1(Persona):
  def __init__(self,nombre,apellido,fechaNacimiento):
    Persona.__init__(self,nombre,apellido)
    self.fecha_nacimiento = fechaNacimiento

  def edad(self):
    actual = datetime.datetime.now()
    diferencia = 0
    if actual.year > self.fecha_nacimiento.year:
      diferencia =  actual.year - self.fecha_nacimiento.year
      if actual.month < self.fecha_nacimiento.month:
        diferencia -=1
      elif actual.month == self.fecha_nacimiento.month and  actual.days <= self.fecha_nacimiento.days:
        diferencia -=1
    return diferencia
fecha = datetime.datetime.strptime("2021-04-05","%Y-%m-%d")
prueba = Persona1(nomb,apell,fecha)
edad = prueba.edad()
print(edad)
