from sys import stdin
def sumar1(lista,index,carry):
        if carry==0:
            return lista
        if lista[index] == 0:
            lista[index] = 1
            carry=0
        elif lista[index] == 1:
            lista[index] = 0
            sumar1(lista,index-1,1)
        return lista    
def sumaComplementoa1(lista1,lista2):
    carry = 0
    lista3 = []
    for i in range(len(lista1)-1,-1,-1):
        if lista1[i] == 0 and lista2[i] ==0:
            if carry == 1:
                lista3.insert(0,1)
                carry=0
            else:
                lista3.insert(0,0)
                
        elif (lista1[i] ==1 and lista2[i] ==0) or (lista1[i] == 0 and lista2[i] ==1):
            if carry == 1:
                lista3.insert(0,0)
                carry = 1
            else:
                lista3.insert(0,1)    
        elif lista1[i] == 1 and lista2[i] == 1:
            if carry == 1:
                lista3.insert(0,1)
                carry = 1
            else:
                lista3.insert(0,0)
                carry = 1
    if carry==1:
        return sumar1(lista3,15,1)
    else:
        return lista3

def checksum(listabits):
    
    listabits = [listabits[i:i+16] for i in range(0, len(listabits), 16)]
    respuesta = listabits[0]
    for i in range(1,len(listabits)):
        respuesta = sumaComplementoa1(respuesta,listabits[i])
    for i in range(len(respuesta)):
        if respuesta[i] == 0:
            respuesta[i] =1
        else:
            respuesta[i] =0
    return respuesta
def main():
    a = stdin.readline().strip()
    a = a.replace(' ','')
    lista = [int(x) for x in a]
    print(*checksum(lista),sep="")
    
main()
