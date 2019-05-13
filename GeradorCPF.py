from random import randint

num = []
m = []

def dividir(soma):
    resto = soma % 11
    if resto < 2:
        num.append(0)
    else:
        res = 11 - resto
        num.append(res)

def somar(tam):
    soma = 0
    for i in range(tam):
        mult = num[i]*m[i]
        soma += mult
    dividir(soma)

def gerarCPF():
    for i in range(9):
        item = randint(0, 9)
        num.append(item)

    for i in range(10, 1, -1):
        m.append(i)

    somar(len(m))
    m.insert(0, 11)
    somar(len(m))

    print("{}{}{}.{}{}{}.{}{}{}-{}{}".format(num[0],num[1],num[2],num[3],num[4],num[5],num[6],num[7],num[8],num[9],num[10]))

gerarCPF()