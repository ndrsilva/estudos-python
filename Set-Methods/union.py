"""
--- Method union ---

Cria um novo conjunto com os sets passados.
"""

set_alf = {'a', 'b', 'c'}
set_num = {1, 2, 3}

union_01 = set_alf.union(set_num)
union_02 = set_alf | set_num

print(union_01) # {'b', 1, 2, 3, 'c', 'a'} 
print(union_02) # {'b', 1, 2, 3, 'c', 'a'}