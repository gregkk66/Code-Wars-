def snail(snail_map):
    lista=[]
    lista2=[]
    b=snail_map.copy()
    b.reverse()
    for i in snail_map:
        for j in i:
            lista.append(j)

    while len(lista2)<len(lista):
        lista2.extend(snail_map[0][0:len(snail_map[0])-1])
        for i in snail_map:
            lista2.append(i[-1])
        a=snail_map[-1]
        a=a[0:len(a)-1]
        a.reverse()
        lista2.extend(a)
        for j in range(len(snail_map)-2):
            lista2.append(b[j+1][0])
        if len(snail_map)>1:
            for i in snail_map:
                i.pop(-1)
            for i in snail_map:
                i.pop(0)
            snail_map.pop(0)
            snail_map.pop(-1)
            b=snail_map.copy()
            b.reverse()
            
    return lista2
