#GENETICA.PY
#Salvem os machos

C = 0
while (C<1 or C>255):
    C = int(input())

sequencia_genetica = ''
while (len(sequencia_genetica)<1 or len(sequencia_genetica)>1000):
    sequencia_genetica = input()

lista_sequencia =[]
for i in range(0, (len(sequencia_genetica)-(C-1))):
    quebrado = sequencia_genetica[i:i+C]
    lista_sequencia.append(quebrado)

existe = 0
palindromo = ''

for j in lista_sequencia:
    palindromo = j[::-1]
    if (j == palindromo):
        existe += 1
    else:
        existe += 0

if (existe >0):
    resposta = 'S\n'
else:
    resposta = 'N\n'

print(resposta)