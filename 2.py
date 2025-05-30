def format_duration(seconds):
    if seconds==0:
        return "now"
    years=seconds//(365*24*60*60)
    days = (seconds-(years*365*24*60*60))//(24*60*60)
    hours=(seconds-(days*24*60*60)-(years*365*24*60*60))//(60*60)
    minutes=(seconds-(hours*60*60)-(days*24*60*60)-(years*365*24*60*60))//(60)
    seconds2=seconds-(minutes*60)-(hours*60*60)-(days*24*60*60)-(years*365*24*60*60)
    lista=[]
    lista.append([years,"year"])
    lista.append([days,"day"])
    lista.append([hours,"hour"])
    lista.append([minutes,"minute"])
    lista.append([seconds2,"second"])
    lista=[x for x in lista if x[0]]
    for i in lista:
        if i[0]>1:
            i[1]=i[1]+"s"
    if len(lista)==1:
        return str(lista[0][0])+" "+lista[0][1]
    elif len(lista)==2:
        return str(lista[0][0])+" "+lista[0][1]+" and "+str(lista[1][0])+" "+lista[1][1]
    elif len(lista)==3:
        return str(lista[0][0])+" "+lista[0][1]+", "+str(lista[1][0])+" "+lista[1][1]+" and "+str(lista[2][0])+" "+lista[2][1]
    elif len(lista)==4:
        return str(lista[0][0])+" "+lista[0][1]+", "+str(lista[1][0])+" "+lista[1][1]+", "+str(lista[2][0])+" "+lista[2][1]+" and "+str(lista[3][0])+" "+lista[3][1]
    elif len(lista)==5:
        return str(lista[0][0])+" "+lista[0][1]+", "+str(lista[1][0])+" "+lista[1][1]+", "+str(lista[2][0])+" "+lista[2][1]+", "+str(lista[3][0])+" "+lista[3][1]+" and "+str(lista[4][0])+" "+lista[4][1]
