def next_bigger(n):
    if len(str(n))==1 or n==int("".join(sorted(str(n),reverse=True))):
        return -1
    a=0
    b=0
    flag=0
    lista1=[int(x) for x in str(n)]
    lista2=[]
    number=0
    for i in range(1,len(lista1)+1):
        a+=1
        b=0
        for j in range(i+1,len(lista1)+1):
            b+=1
            if lista1[-i]>lista1[-j]:
                if lista1[-j+1:-i]==sorted(lista1[-j+1:-i],reverse=True) or len(lista1[-j+1:-i])==0 or len(lista1[-j+1:-i])==1:
                    number=lista1[-i]
                    lista1.pop(-i)
                    flag=True
            if flag==True:
                break
        if flag==True:
            break
    lista2=lista1[0:len(lista1)-(a+b-1)]
    lista4=lista1[len(lista1)-(a+b-1):]
    lista2.append(number)
    lista4.sort()
    lista2=[str(x) for x in lista2]
    lista4=[str(x) for x in lista4]
    no1=int("".join(lista2) + "".join(lista4))
    return no1
    
    

    
      
