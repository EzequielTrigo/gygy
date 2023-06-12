def contarLineas(archivo:str)->int:
    x=open(archivo,"r") #abre un texto
    seTermino=False
    vacio=""
    res:int = 0
    while not seTermino: #recorre las lineas de texto hasta que no hay mas(sale "")
        res+=1
        f=x.readline()
        seTermino=(f==vacio)
    x.close()
    return (res-1)

def existePalabra(archivo:str,palabra:str)->bool:
    x=open(archivo,"r")
    cantLineas=contarLineas(archivo)
    i=0
    res:bool=False
    while i<cantLineas:
        linea=x.readline()
        res= palabra in linea # devuelve tru si esta la palabra
        #for i in range(len(linea)):

            #if linea[i] == palabra[0]:
             #   f=1
              #  while f<len(palabra) and linea[f+i]==palabra[f]:
               #     f+=1
                #if f==len(palabra):
                 #   res=True
        i+=1
    x.close()
    return res

def cantidadDeApariciones(archivo:str,palabra:str)->int:
    res:int=0
    x=open(archivo,"r")
    i=0
    cantLineas=contarLineas(archivo)
    while i<cantLineas: #itera las lineas
        linea=x.readline()
        for i in range(len(linea)):#itera los caracteres, buscando palabras
            if linea[i] == palabra[0]:
                f=1
                while f<len(palabra) and linea[f+i]==palabra[f]:
                    f+=1
                if f==len(palabra) and ((i==0 and (linea[f+i]=="\n" or linea[f+i]==" ")) ):
                    res+=1
                elif f==len(palabra) and i>0:
                    if (linea[i-1]==" " and (linea[f+i]=="\n" or linea[f+i]==" ")):
                        res+=1
        i+=1
    x.close()
    return res  

def clonarSinComentarios(archivo: str):
    x=open(archivo,"r")
    z=open(archivo+"corregido","w")
    i=0
    cantLineas=contarLineas(archivo)
    while i<cantLineas:
        c=x.readline()
        if not empiezaConComentario(c):
            z.write(c)
        i+=1
    z.close()
    x.close()
    return "terminado"

def empiezaConComentario(linea:str)->bool:
    res:bool=False
    for letra in linea:
        if letra == "#":
            res=True
        elif letra != " ":
            break
    return res
    
#print(clonarSinComentarios("test"))

def fraseAlFinal(archivo:str,frase:str):
    x=open(archivo,"a")
    x.write("\n"+frase)
    x.close()

#print(fraseAlFinal("test","hola q hace"))

def textoALista(archivo:str)->list:
    res:list=[]
    texto=open(archivo,"r")
    cantLineas=contarLineas(archivo)
    i=0
    while i<cantLineas:
        c=texto.readline()
        res.append(c)
        i+=1
    texto.close()
    return res

#print(hola.textoALista("test"))

def fraseAlPrincipio(archivo:str,frase:str)->str:
    lista:list=textoALista(archivo)
    x=open(archivo,"w")
    cantLineas=len(lista)+1
    i=0
    while i<cantLineas:
        if i!=0:
            x.write(lista[i-1])
        else:
            x.write(frase+"\n")
        i+=1
    x.close()
    return "terminado"

def promedioEstudiante(lu:str)->float:
    x=open("notasAlumnos","r")
    i=0
    sumNotas:int=0
    cantNotas:int=0
    cantLineas=contarLineas("notasAlumnos")
    while i<cantLineas:
        linea=x.readline()
        if lu==luEst(linea):
            sumNotas+=sacarNota(linea) 
            cantNotas+=1
        i+=1
    return (sumNotas/cantNotas)

def sacarNota(linea:str)->int:
    notaString:str=""
    cantDigitos=len(linea)
    i=0
    comas=0
    while i<cantDigitos:
        if comas==3:
            notaString += linea[i]
        elif linea[i]==",":
            comas+=1
        i+=1
    res:int=eval(notaString)
    return res

def luEst(linea:str)->str:
    res:str=""
    i=0
    comas=0
    cantCaracter=len(linea)
    while i<cantCaracter and comas<1:
        if linea[i+1]==",":
            comas+=1
        res+=linea[i]
        i+=1
    return res

#print(h.promedioEstudiante("54/22"))
import random

def listaNumerosDesHasta(desde:int,hasta:int)->list:
    res:list=[]
    i=hasta
    while i>=desde:
        res.append(i)
        i-=1
    return res

#print(listaNumerosDesHasta(1,10))

def generarNrosAlAzar(n : int, desde : int, hasta : int)->list:
    res:list=[]
    lista:list=listaNumerosDesHasta(desde,hasta)
    i=0
    while i<n:
        res.append(random.randint(desde,hasta))
        i+=1
    return res

numAlAzar=generarNrosAlAzar(10,0,10)

from queue import LifoQueue as Pila

def pilaIntAlAzar(n : int, desde : int, hasta : int)->Pila:
    p=Pila()
    i=0
    listaNumeros:list=generarNrosAlAzar(n,desde,hasta)
    while i<n:
        p.put(listaNumeros[i])
        i+=1
    return p

#p=pilaIntAlAzar(10,0,10)

#print(p.qsize())

def cantidadElementos(p : Pila) -> int:
    res:int=p.qsize()
    return res

def buscarElMaximo2( p : Pila) -> int:
    cantidadElem:int=cantidadElementos(p)
    i=0
    res:int=0
    while i<cantidadElem:
        x=p.get()
        if x>res:
            res=x
        i+=1
    return res

#print(buscarElMaximo2(p))

def estaBienBalanceada( s : str) -> bool:
    cantAbre:int=0
    cantCierra:int=0
    i=0
    cantCaracteres:int=len(s)
    while i<cantCaracteres:
        if s[i]=="(":
            cantAbre+=1
        elif s[i]==")":
            cantCierra+=1
        i+=1        
    res:bool=(cantAbre==cantCierra)
    return res

#print(estaBienBalanceada("(2+3(*5))"))
#print(estaBienBalanceada(""))
#print(estaBienBalanceada("(2+3(*5)"))

from queue import Queue as Cola

def colaConNumAlAzar()->Cola:
    cola:Cola=Cola()
    x=numAlAzar
    i=0
    while i<len(x):
        cola.put(x[i])
        i+=1
    return cola

c=colaConNumAlAzar()

def cantidadElementos2(c : Cola) -> int:
    i:int=0
    x=c
    while not x.empty():
        x.get()
        i+=1
    res=i
    return res

#print(cantidadElementos2(c))

def buscarElMaximo( c : Cola) -> int:
    res:int=c.get()
    i=0
    cantElem=cantidadElementos2(c)
    while i<cantElem:
        a=c.get()
        if a>res:
            res=a
        i+=1
    return res

def armarSecuenciaDeBingo()->Cola[int]:
    res:Cola=Cola()
    x=listaNumerosDesHasta(0,99)
    i=0
    c=random.sample(x,12)
    while i<12:
        res.put(c[i])
        i+=1
    return res

def colaALista(cola)->list:
    c=cola
    res:list=[]
    while not c.empty():
        x=c.get()
        res.append(x)
    return res

#print(colaALista())

def bolillero()->Cola[int]:
    x=listaNumerosDesHasta(0,99)
    lista:list=random.sample(x,100)
    c:Cola=Cola()
    i=0
    while i<len(lista):
        c.put(lista[i])
        i+=1
    return c

def jugarCartonDeBingo( carton : list[int], bolillero : Cola[int])->int:
    i=0
    c=bolillero.qsize()
    fed=[]
    while i<c and len(carton)>0:
        x=bolillero.get()
        fed.append(x)
        if pertenece(carton,x):
            carton.remove(x)
        i+=1
    res:int=i
    return res

def pertenece(lista:list,elem:int)->bool:
    res:bool=False
    i=0
    while i<len(lista):
        if lista[i]==elem:
            res=True
        i+=1
    return res
''''
carton=colaALista(armarSecuenciaDeBingo())
print(carton)
bolille=bolillero()
p=Cola()

#print(colaALista(p))
print(jugarCartonDeBingo(carton,bolille))
'''

def listaEstudiantes():
    res=[]
    while True:
        x=input("ingrese estudiantes, para terminar ingrese listo:")
        if x== "listo":
            break
        res.append(x)
    return res

#print(listaEstudiantes())

def nPacientesUrgentes(c : Cola) -> int:
    i=0
    while not c.empty():
        paciente=c.get()
        if paciente[0]<4:
            i+=1
    return i

def listaACola(lista:list)->Cola:
    i=0
    cola:Cola=Cola()
    while i<len(lista):
        cola.put(lista[i])
        i+=1
    return cola

pacientes=listaACola([(1,"d","d"),(3,"f","f"),(4,"g","g"),(2,"d","d"),(2,"f","f"),(8,"d","d"),(9,"f","f"),(3,"g","g"),(2,"d","d"),(2,"f","f")])

#print(nPacientesUrgentes(pacientes))

def palabrasALista(linea:str)->list:
    res:list=[]
    x=""
    for letra in linea:
       if letra ==" " or letra=="\n":
           res.append(x)
           x=""
       elif letra!=" ":
           x+=letra
    return res

#print(palabrasALista("dsdss dsdss dssdsd sdsdds sddss"))  

def agruparPorLongitud(archivo : str) -> dict:
    texto=open(archivo,"r")
    res:dict={}
    i=0
    cantLineas=contarLineas(archivo)
    while i<cantLineas:
        linea=texto.readline()
        palabras=palabrasALista(linea)
        j=0
        x=len(palabras)
        while j<len(palabras):
            c=palabras[j]
            if not len(palabras[j]) in res:
                res[len(palabras[j])]=0
            res[len(palabras[j])]+=1
            j+=1
        i+=1
    return res

#print(agruparPorLongitud("notasAlumnos"))
#print(palabrasALista('25/ 22/7 ,10\ n'))

def luEstudiantes(texto)-> list:
    res:list=[]
    cantLineas=contarLineas(texto)
    texto=open(texto,"r")
    i=0
    while i<cantLineas:
        x=texto.readline()
        lu=luEnLaLinea(x)
        if not perteneceStr(res,lu):
            res.append(lu)
        i+=1
    return res

def luEnLaLinea(linea:str)->str:
    res:str=""
    estaLaComa=False
    i=0
    while not estaLaComa:
        res+=linea[i]
        if linea[i+1]==",":
            estaLaComa=True
        i+=1
    return res

def perteneceStr(lista:list,elem:str)->bool:
    res:bool=False
    i=0
    while i<len(lista):
        if lista[i]==elem:
            res=True
        i+=1
    return res

#print(luEstudiantes("notasAlumnos"))

def promedioDic(texto:str)->dict:
    res:dict={}
    luEstu=luEstudiantes(texto)
    for lu in luEstu:
        res[lu]=promedioEstudiante(lu)
    return res

#print(promedioDic("notasAlumnos"))

def sacarPalabrasDict():
    x={1:23,2:4,3:567}
    c=iter(x)
    res=[]
    for key in c:
        res.append(key)
    return res

#print(sacarPalabrasDict())

def sacarPalabrasDeLinea(linea:str)->list:
    res:list=[]
    i=0
    palabra=""
    while i<len(linea):
        letra:str=linea[i]
        if letra == " " or letra == "\n":
            res.append(palabra)
            palabra=""
        elif letra !=" ":
            palabra+=letra
        i+=1
    return res

#print(sacarPalabrasDeLinea("as sasa sdsdsd asaa asassa\n"))

def cantDePalabras(archivo)->dict:
    res:dict={}
    texto=open(archivo,"r")
    cantLineas=contarLineas(archivo)
    i=0
    while i<cantLineas:
        linea=texto.readline()
        palabras=sacarPalabrasDeLinea(linea)
        for palabra in palabras:
            if not palabra in res:
                res[palabra]=1
            else:
                res[palabra]+=1
        i+=1
    return res

##print (cantDePalabras("testcorregido"))

def laPalabraMasFrecuente(archivo: str) -> str:
    res:str=""
    recuentoDePalabras:dict=cantDePalabras(archivo)
    for key in recuentoDePalabras:
        if valorMayorDelDic(key,recuentoDePalabras):
            res=key
            break
    return res


def valorMayorDelDic(keyp:str,dicc:dict)->bool:
    res:bool=True
    for key in dicc:
        if dicc[keyp]<dicc[key]:
            res=False
            break
    return res

#print(valorMayorDelDic(1,{1:2,2:2})) 

print (laPalabraMasFrecuente("testcorregido"))
