import sys
def get_max_num(word):
        maxi = 1
        for x in range(len(word)):
                maxi *= len(word)

        return maxi

dic = sys.argv[1]
print ("El numero de palabras que se generaran sera: "+str(get_max_num(dic))+"\nQuires proseguir?[Y/N]")
resp = input(">")
if resp != "y":
        sys.exit(0)

lista = [0] * int(len(dic))
palabra = ""
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

                print (palabra)
                a += 1
                if a == get_max_num(dic):
                        break
