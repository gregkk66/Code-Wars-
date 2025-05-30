from itertools import permutations
def gta(limit, *args): 
    result=0
    lista=[]
    a=0
    while len(lista)<limit:
        for i in range(len(args)):
            if len(lista)<limit:
                if a<len(str(args[i])):
                    if int(str(args[i])[a]) not in lista:
                        lista.append(int(str(args[i])[a]))
        a+=1
    for i in range(1,limit+1):
        for j in permutations(lista,i):
            for k in j:
                result+=k
    return result
