def permutar(permut=list(range(3))):
    if len(permut) > 1:
        l=list()
        for i in permut:
            temp=[j for j in permut]
            temp.remove(i)
            for p in permutar(temp): 
                l.append([i]+p)
        return l
    else:
        return [permut]
