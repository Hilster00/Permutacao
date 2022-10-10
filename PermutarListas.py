def permutar(a=None,permut=list(range(3)),lista=list()):
    if len(permut) > 1:
        l=list()
        for i in permut:
            temp=[j for j in permut]
            t=[j for j in lista]
            temp.remove(i)
            t.append(i)
            for p in permutar(a,temp,t): 
                l.append([i]+p)
        return l
    else:
        if a != None:
            lista.append(permut[0])
            a.append(lista)
        return [permut]
