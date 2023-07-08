matriz_empresas = []
lista_empresas = []
lista_empresa = []
rep = 1
while rep >= 0 :
        razao = str(input("Insira a Razão Social da empresa: "))
        div = float(input("Insira a divida referente a Razão Social: "))
        rep = int(input("Digite (-1) para sair ou outro número para continuar: "))
        linha = [razao,div]
        matriz_empresas.append(linha)
        if rep == -1 :
            print(matriz_empresas)
semdiv = 0
razao = ""
for linha in matriz_empresas:
    linha[1]
    lista_empresas.append(linha[1])
    soma = 0
    for somas in lista_empresas:
        soma = soma + somas
    if linha [1] == semdiv:
        semdiv = linha [1]
        razao = linha [0]
        lista_empresa.append(razao)
media = soma/len(matriz_empresas)
print("Total de empresas que integram um distrito industrial: ",len(matriz_empresas))
print("Média aritmética das dívidas: ",media)
print("Razão social das empresas que não possuem dívidas com a prefeitura:",lista_empresa)
