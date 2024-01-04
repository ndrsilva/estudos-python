"""
--- Method intersection ---

Apenas retorna um novo conjunto, se todos os conjuntos usado no 
método 'intersection' tenha um ou mais elemento em comum.

"""

intersection_01 = {1, 2, 4} 
intersection_02 = {2, 4, 6}
intersection_03 = {3, 4, 8}

conjunto_01 = intersection_01.intersection(intersection_02)
conjunto_02 = intersection_01.intersection(intersection_02, intersection_03)

# OU

conj_01 = intersection_01 & intersection_02
conj_02 = intersection_01 & intersection_02 & intersection_03

print(conjunto_01)
print(conjunto_02)

print(conj_01)
print(conj_02)