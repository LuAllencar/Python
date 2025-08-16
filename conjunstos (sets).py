conj1= {"Carlos", "Josiel", "Jandira", "Aline"}
conj2 = {"Aline", "Carlos", "Jaqueline", "Altair"}

repetidos = conj1.intersection(conj2) 
# 1. corresponde aos elementos que estão em ambos os conjuntos
uniao = conj1.union(conj2) 
# 2.  corresponde à união dos dois conjuntos, sem repetir os elementos
apenasUmGrupo = conj1.symmetric_difference(conj2) 
# 3. corresponde aos elementos que estão apenas em um dos conjuntos, mas não em ambos. Essa é a diferença simétrica.

print(f"Estão presentes nos dois grupos: {repetidos}") 
# 1. Elementos comuns
print(f"Estão presentes apenas em um dos grupos: {apenasUmGrupo}") 
# 3. Elementos exclusivos de cada grupo
print(f"União dos dois grupos, sem repetir indivíduos: {uniao}") 
# 2. União dos conjuntos