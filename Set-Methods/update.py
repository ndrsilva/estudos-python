"""
--- Method updade ---

Atualiza os item de um set.
"""

updade_alf_01 = {'a', 'b', 'c'}
updade_alf_02 = {'a', 'b', 'c'}
updade_num = {2}

updade_alf_01.update(updade_num)
updade_alf_02 |= updade_num


print(updade_alf_01) # {1, 2, 'a', 'c', 'b'}
print(updade_alf_02) # {1, 2, 'a', 'c', 'b'} 