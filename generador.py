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


dic = sys.argv[1]
file_name = input("Ingrese el nombre del archivo a crear: ")


print("El numero de palabras que se generaran sera: " +
      str(get_max_num(dic))+"\nQuires proseguir?[Y/N]")
resp = input(">")
if resp != "y":
    sys.exit(0)
print("Cuantas palabras se desea generar?: ")
resp2 = int(input(">"))

lista = [0] * int(len(dic))
palabra = ""

alltext = ""
a = 0


while True:
    palabra = ""
    for w in range(len(lista)):
        if lista[w] == len(dic):
            lista[w] = 0
            try:
                lista[w+1] += 1
            except:
                pass

    for x in lista:
        palabra += dic[x]
        lista[0] += 1
        print(palabra)
        # alltext += palabra + ","
        a += 1

                
    alltext += palabra + ","
    if a == resp2:
        create_file(file_name, alltext)
        break

    if a == get_max_num(dic):
        create_file(file_name, alltext)
        break
