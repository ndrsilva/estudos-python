"""
.removesuffix()
.removepreffix()
"""

nome_completo = 'andre silva'

# Uma forma de removeprefix.
if nome_completo.startswith('andre'):
    print(nome_completo[len('andre') + 1:])

# Uma forma de removesuffix.
if nome_completo.endswith('silva'):
    print(nome_completo[:len('silva') + 1])



# Python 3.9
nome = nome_completo.removeprefix('andre ')
sobrenome = nome_completo.removesuffix(' silva')

print(nome)
print(sobrenome)
print(nome_completo)

