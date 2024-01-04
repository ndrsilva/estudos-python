"""
--- Method difference ---

O método difference elimina todos os itens que tem no  
primeiro conjunto que seja igual aos itens do segundo conjunto.

"""

difference_01 = {1, 2, 3}
difference_02 = {3, 4}

result_01 = difference_01.difference(difference_02)
result_02 = difference_01 - difference_02

print(result_01) # {1, 2}
print(result_02) # {1, 2}