"""
'|' -> Permitir atribuir o valor de n dicts em uma nova variável, "c = a | b".
'|=' -> Seria o update utilizado no python3.8; "a |= b"
"""

a = {'al': 'andre luis'}
b = {'ls': 'leo silva'}

## Python 3.8
print('\nPython3.8:')

print('Usando o ** para juntar os dicts em uma nova variável.')
c = {**a, **b} # {'al': 'andre luis', 'ls': 'leo silva'}
print(c, '\n')

print('Usando os métodos "copy" e "update" para juntar os dicts em uma nova variável.')
d = a.copy() # {'al': 'andre luis'}
d.update(b) # {'al': 'andre luis', 'ls': 'leo silva'}
print(d, '\n')



## Python 3.9
print('\nPython3.9:')

print('Usando o operador "|" para juntar os dicts em uma nova variável.')
c = a | b # {'al': 'andre luis', 'ls': 'leo silva'}
print(c, '\n')

print('Usando o método "copy" e o operador "|=" para juntar os dicts em uma nova variável.')
d = a.copy() # {'al': 'andre luis'}
d |= b # {'al': 'andre luis', 'ls': 'leo silva'}
print(d, '\n')
