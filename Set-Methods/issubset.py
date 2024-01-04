"""
--- Method issubset ---

Verificar se um conjunto é um subconjunto de outro conjunto.
"""

conjunto_01 = {1, 2, 3}
conjunto_02 = {1, 2, 3, 4, 5} 


result_01 = conjunto_01.issubset(conjunto_02)
result_02 = conjunto_01 <= conjunto_02

print(result_01) # True
print(result_02) # True