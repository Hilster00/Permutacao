def permutar(permut="abc"):
    if len(permut)  > 1:
        palavras=list()
        for letra in permut:
            temp=permut.replace(letra,"")
            for i in permutar(temp):
                palavras.append(letra+i)
        return palavras
    else:
        return permut
