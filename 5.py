def recoverSecret(triplets):
    lista=[]
    for i in triplets:
        for j in i:
            if j not in lista:
                lista.append(j)
    for a in range(3):
        for i in triplets:
            for j in range(1,3):
                if lista.index(i[j])<lista.index(i[j-1]):
                    lista[lista.index(i[j-1])]=i[j]
                    lista[lista.index(i[j])]=i[j-1]
    return "".join(lista)
