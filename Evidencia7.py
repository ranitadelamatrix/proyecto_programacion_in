#Crear cuatro listas:
#1. Con los nombres de su familia.
#2. Con los valores de la temperatura de un mes entero (mes a elección, pero definirlo).
#3. Con los nombres de ciudades que hayan visitado.
#4. Con las fechas y nombres de eventos importantes de su vida.

nombres_familiares =["Flor", "Esteban", "Julia", "Cecilia", "Uma"]


mes_mayo_temp = [20, 26.5, 24.8, 22.1, 21.7, 20.5, 19.9, 23.4, 24.7, 26.0, 27.2, 28.6, 25.9, 22.8, 20.2, 21.5, 23.7, 24.6, 25.8, 26.3, 25.1, 23.9, 22.6, 21.0, 20.3, 19.5, 18.7, 22.0, 24.3, 26.8, 27.9]


ciudades_visitadas = ["Cordoba", "Bs As", "Salta", "Jujuy", "San Luis"]


fechas_importantes = ["10/07/1989 nacimiento", 
"20/04/2000 campeones con mi club", 
"13/09/2008 graduacion", "16/05/2013 inicio banda de rock",
 "28/12/2019 casamiento"]

#Ordenar alfabéticamente la lista de los nombres de familia.
nombres_familiares.sort()

#Ordenar ascendentemente la lista de temperaturas.
mes_mayo_temp.sort()

#Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente.
mes_julio_temp = [7, 10, 10, 6, 4, 8, 12, 14, 18, 20, 5, 2, 1, 4, 0]
mes_julio_temp.extend(mes_mayo_temp)

#Quitar de la lista de los nombres de familia, a tus abuelos.
elim_abuelos = nombres_familiares
elim_abuelos.remove ("Flor")
elim_abuelos.remove ("Cecilia")

#Quitar de la lista de ciudades la ciudad menos linda que hayas visitado.
ciudades_menos_lindas = ciudades_visitadas
del ciudades_menos_lindas [4] 


#Mostrar todas las listas.
print("Nombres de mis Familiares sin mis abuelos",nombres_familiares)
print("Temperatura del mes de Mayo y 15 dias posteriores", mes_mayo_temp)
print("Ciudades mas lindas que visitamos", ciudades_visitadas)
print("Eventos importantes", fechas_importantes)

#Crear tres tuplas con datos random.
tup_1 = ("guitarra", "bajo", "bateria", "teclado")
tup_2 = (2,12,13,5)
tup_3 = ("rojo", "azul", "verde", "plateado")

#Crear una lista que las contenga y mostrarla.
lista_tup = [tup_1, tup_2, tup_3]
print(lista_tup)

#Crear el siguiente diccionario:
#Las claves serán los dni de su núcleo familiar, y el valor será SOLO el nombre de la persona.
#Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)
dic_familiar = {
    "35485956" : "Cecilia",
    "45874596" : "Flor",
    "12456789" : "Esteban",
    "25456951" : "Uma",
    "15975345" : "Julia"
}
#Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)
dic_familiar ["35485956"] = "Abuela Paterna"
dic_familiar ["45874596"] = "Abuela Materna"
dic_familiar ["12456789"] = "Hermano"
dic_familiar ["25456951"] = "Prima"
dic_familiar ["15975345"] = "Hermana"

#Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono.
#Ambos deben ser mostrados.
