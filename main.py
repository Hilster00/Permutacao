import PermutarStrings
import PermutarListas

strings=PermutarStrings.permutar("abc")
listas=PermutarListas.permutar("abc")

print("Permutacao strings pelo permutador de strings")
for p in strings:
    print(p)
    
print("Permutacao strings pelo permutador de listas")    
for p in listas:
    print(p)
print("comparacao:",end="")    
print(strings==listas)

print("conveter sub_listas para string")
#conveter sub_listas para string
listas=[''.join(p) for p in listas] 


print("Permutacao strings pelo permutador de strings")
for p in strings:
    print(p)
    
print("Permutacao strings pelo permutador de listas e converitido para strings")    
for p in listas:
    print(p)
    
print("comparacao:",end="")    
print(strings==listas)

