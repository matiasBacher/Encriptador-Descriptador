
nombreArchivo= "hola.txt" #input("¿Cuál es archivo que desea encriptar? \n")
archivo=open(nombreArchivo, "r") # abre el archivo en solo lectura("r")

listContenidoArchivo=list(archivo.read())
clave=list("asrwjkmop0") #se pone al principio de los texto encriptado y se usa para saber si el mismo lo esta

def encripDescrip(texto,modo=False): # modo falso encripta y modo verdadero descripta
    principio=32 # los valores imprimibles de ascii empiezan en 32
    tope=255 # y terminan 255
    incremento=1
    if modo: # es para invertir los valores segun se quiera encriptar o descriptar
        tope=32
        principio=255
        incremento=-1
    for i in range(len(texto)):
        if ord(texto[i])==tope: 
            texto[i]=chr(principio)
        else:
            texto[i]=chr(ord(texto[i])+incremento)
    return texto

if listContenidoArchivo[0:10]==clave:
    listContenidoArchivo=encripDescrip (listContenidoArchivo[10:], True) #descripta el archivo

else:
    listContenidoArchivo=clave+encripDescrip (listContenidoArchivo) #encripta el archivo

archivo.close() #cierra el archivo
archivo= open (nombreArchivo, "w") #abre el archivo en modo escritura(borra el texto del archivo)

archivo.write ("".join(listContenidoArchivo))



""" 
.join() convierte una lista en un string
chr() convierte un valor ascii en un caracter
ord convierte un caracter en un valor ascii 
list() convierte un strin u otro objeto en en una lista
"""



    

