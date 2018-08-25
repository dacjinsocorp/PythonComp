import sys
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

#Pregunta donde se informa la cantidad de palabras a generar por defecto y si desea continuar
print("El numero de palabras que se generaran sera: " +
      str(get_max_num(dic))+"\nQuires proseguir?[Y/N]")
resp = input(">")
while True:
    if resp == "y":
        break
    if resp == "n":
        sys.exit()
    else:
        print("Quires proseguir?[Y/N]")
        resp = input(">")
while True:
    
    # Solicitud de ingreso de número de palabras que desea generar, esto con validación
    try:
        wordCuantity = int(input("Cuantas palabras se desea generar?: "))
        break
    except ValueError:
        print ("Por favor ingresar un numero entero")

# Solicita el 
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

    # Corte por cantidad de palabras ordenadas por el usuario
    if counter == wordCuantity:
        create_file(file_name, alltext)
        break

    # Corte por maxima cantidad de palabras posibles
    if counter == get_max_num(dic):
        create_file(file_name, alltext)
        break
