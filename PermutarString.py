def permutar(permut="abc",palavra=""):
    if len(permut)  > 1:
        for letra in permut:
            temp=permut.replace(letra,"")
            permutar(temp,palavra+letra)
    else:
        print(palavra+permut)
