#abbreviating.py

nome = ''
lista_inicial =[]
while True:
    try:
        nome = input();
        lista_inicial.append(nome)
    except EOFError:
        break;

lista_abreviacoes=[]
for j in lista_inicial:
    lista_nomes = j.split()
    nome_abreviado = []
    nome_abreviado.append(lista_nomes[0])
    for i in range(1, len(lista_nomes)-1):
        abreviacao = lista_nomes[i][0] +"."
        nome_abreviado.append(abreviacao)
    if (len(lista_nomes)>1):
        nome_abreviado.append(lista_nomes[-1])
    nome_abreviado_str = ''
    nome_abreviado_str = ' '.join(nome_abreviado)
    lista_abreviacoes.append(nome_abreviado_str)

lista_abreviacoes.sort()
for i in lista_abreviacoes:
    print(i)