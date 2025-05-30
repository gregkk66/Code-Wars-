def mix(s1, s2):
    s1 = ''.join(ch for ch in s1 if ch.isalpha())
    s2 = ''.join(ch for ch in s2 if ch.isalpha())
    s1 = ''.join(ch for ch in s1 if ch.islower())
    s2 = ''.join(ch for ch in s2 if ch.islower())
    lista=[]
    for i in sorted(set(s1)):
        if s1.count(i)>1 and s1.count(i)>s2.count(i):
            lista.append("1:"+str(i*s1.count(i)))
    for i in sorted(set(s2)):
        if s2.count(i)>1 and s2.count(i)>s1.count(i):
            lista.append("2:"+str(i*s2.count(i)))
    for i in sorted(set(s1)):
        if s1.count(i)>1 and s1.count(i)==s2.count(i):
            lista.append("=:"+str(i*s1.count(i)))
    lista.sort(key=len,reverse=True)
    return "/".join(lista)
