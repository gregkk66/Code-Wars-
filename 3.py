
import copy
def findsubdet(det):
    subdets=[]
    det2=copy.deepcopy(det)
    if len(det[0])>2:
        for i in range(len(det[0])):
            for j in range(len(det[0])):
                det2[0].pop(0)
            for k in range(1,len(det[0])):
                det2[k].pop(i)
            det2=[x for x in det2 if x]
            subdets.append(det2)
            det2=copy.deepcopy(det)
        return subdets

def mindet(lista):
    return (lista[0][0]*lista[1][1])-(lista[0][1]*lista[1][0])

def determinant(matrix):
    result=0
    a=0
    n=0
    if len(matrix)==1:
        return matrix[0][0]
    if not len(matrix)==2:
        for i in findsubdet(matrix):
            if len(i)==2:
                result=result+(-1)**(n)*(matrix[0][a]*mindet(i))             
            elif len(i)>2:
                result=result+(-1)**(n)*matrix[0][a]*determinant(i)
            a+=1
            n+=1
    else:
        return mindet(matrix)
    return result
