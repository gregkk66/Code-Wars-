def strip_comments(strng, markers):
    lista=strng.split("\n")
    result=[]
    final_result=[]
    a=0
    for i in lista:
        if i:
            for j in i:
                a+=1
                if j in markers:
                    result.append(i[0:a-1])
                    a=0
                    break
            if a>0:
                result.append(i[0:a])
                a=0
        else:
            result.append("")
    for i in result:
            final_result.append(i.rstrip())
    return "\n".join(final_result)
