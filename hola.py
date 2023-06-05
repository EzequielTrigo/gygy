def contarLineas(archivo:str)->int:
    x=open(archivo,"r")
    seTermino=False
    vacio=""
    res:int = 0
    while not seTermino:
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
        res= palabra in linea
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
    while i<cantLineas:
        linea=x.readline()
        for i in range(len(linea)):
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

print(cantidadDeApariciones("test","a"))