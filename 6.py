def top_3_words(text):
    for i in text:
        if i.isalpha()==False and i!="'":
            text=text.replace(i," ")
    text="".join(c for c in text if c.isalpha() or c=="'" or c==" ")
    text=text.lower()
    lista=text.split()
    lista2=[]
    for i in list(set(lista)):
        if set(i)!={"'"}:
            lista2.append([i,lista.count(i)])
    lista2.sort(key=lambda x: x[1],reverse=True)
    return [x[0] for x in lista2[0:3]]
