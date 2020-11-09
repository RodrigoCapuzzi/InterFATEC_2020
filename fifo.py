#fifo

N = 0
while (N<1 or N>100):
    N = int(input())

lista_TCs =[]
lista_Ds = []
for i in range(N):
    tempo = input()
    x = tempo.split(" ")
    for i in x:
        if int(i) <0 or int(i) >60:
            tempo = input()
            x = tempo.split(" ")
    for i in range(len(x)):
        if i % 2 ==0:
            lista_TCs.append(int(x[i]))
        else:
            lista_Ds.append(int(x[i]))

instante_inicial = 0
lista_instantes_iniciais=[]
for i in lista_Ds:
    instante_inicial = instante_inicial + i
    lista_instantes_iniciais.append(instante_inicial)

instante_inicial2 = 0
lista_instantes_iniciais2=[0]
for i in lista_Ds:
    instante_inicial2 = instante_inicial2 + i
    lista_instantes_iniciais2.append(instante_inicial2)

lista_inst_inicial_menos_TC = []
for i in range(len(lista_Ds)):
    subtracao = lista_instantes_iniciais2[i] - lista_TCs[i]
    lista_inst_inicial_menos_TC.append(subtracao)

resultado =[]
for i in range(len(lista_TCs)):
    menos = lista_instantes_iniciais[i] - lista_TCs[i]
    resultado.append(menos)

soma = sum(resultado)
TMT = soma/len(lista_instantes_iniciais)
TME = sum(lista_inst_inicial_menos_TC)/len(lista_inst_inicial_menos_TC)

print('TME: ', round(TME,1))
print('TMT: ', round(TMT,1),"\n")