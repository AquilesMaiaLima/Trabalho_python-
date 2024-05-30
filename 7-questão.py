nome_aluno = input("digite o nome do estudante: ")
materia = input("nome da materia: ")
n1 = int(input("digite nota parcial: "))
n2 = int(input("digite nota bimestral: "))
m = (n1 + n2)/2
if 10> m >= 0:
    if 10> m >= 6:
       M = ("passou de bimestre")
    else:
        M = ("Esta reprovado")
    print(f"na materia de {materia} o aluno(a) {nome_aluno} ficou com media final de {m} e ele(a) {M}")
else:
    print('augo esta errado cofira os valores das medias novamente')