"""
--- Method isdisjoint ---

Verificar se dois conjuntos são disjuntos, ou seja, se eles não têm elementos em comum
"""

conjunto_01 = {1, 2, 3}
conjunto_02 = {4, 5, 6} 
conjunto_03 = {3, 4, 5}

# Verificar se conjunto_01 e conjunto_02 são conjuntos disjuntos.
resultado = conjunto_01.isdisjoint(conjunto_02)
print(resultado)  # Saída: True (porque não têm elementos em comum).

# Verificar se conjunto_01 e conjunto_03 são conjuntos disjuntos
resultado = conjunto_01.isdisjoint(conjunto_03)
print(resultado) # Saída: False (porque têm o elemento 3 em comum).
