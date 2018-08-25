import sys
import csv
import os


# Metodo para obtener la cantidad de palabras que se generan a partir de una
def get_max_num(word):
    maxi = 1
    for x in range(len(word)):
        maxi *= len(word)
    return maxi


# Metodo que crea el archivo de texto y lo escribe
def create_file(name, content):
    file = open("archivos/" + name + ".txt", "a")
    file.write(content)
    file.close()


# Inicio del programa
dic = sys.argv[1]

print("El numero de palabras que se generaran sera: " +
      str(get_max_num(dic))+"\nQuires proseguir?[Y/N]")
resp = input(">")
if resp != "y":
    sys.exit(0)
print("Cuantas palabras se desea generar?: ")
wordCuantity = int(input(">"))
file_name = input("Ingrese el nombre del archivo a crear: ")


# Declaración de variables generales
lista = [0] * int(len(dic))
word = ""
alltext = ""
counter = 0

while True:
    word = ""
    for w in range(len(lista)):
        if lista[w] == len(dic):
            lista[w] = 0
            try:
                lista[w+1] += 1
            except:
                pass

    for x in lista:
        word += dic[x]
        lista[0] += 1
        print(word)

    counter += 1      
    alltext += word + ","
    if counter == wordCuantity:
        create_file(file_name, alltext)
        break

    if counter == get_max_num(dic):
        create_file(file_name, alltext)
        break
