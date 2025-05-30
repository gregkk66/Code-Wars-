def solution(args):
    result=""
    a=0
    lista=[]
    args.append(1/2)
    while len(args)>1:
            if args[1]==args[0]+1 or args[1]==args[0]-1:
                lista.append(args[0])
                args.pop(0)
                a+=1
            else:
                if a>1:
                    lista.append(args[0])
                    args.pop(0)
                    result+= str(lista[0])+ "-" +str(lista[-1])+","
                    lista=[]
                    a=0
                elif a==1:
                    result+=str(lista[0]) + ","
                    result+=str(args[0]) + ","
                    args.pop(0)
                    lista=[]
                    a=0
                else:
                    result+=str(args[0])+","
                    args.pop(0)
                    a=0
    return result[0:-1]
