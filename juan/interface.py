from classes import Arvore, ArvoreFrutiferas

print("Olá bem vindo ao site de arvores, aqui nos catalogamos")
print("        sua arvore e armazenamos no sistema:")


def menu():
    folhas_cor = ["verde", "marron", "sem folhas", "vermelho", "laranja"]
    tronco_cor = ["branco", "marron", "cinza", "arco-iris", "vermelho"]
    inverno = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho"]
    verao = ["agosto", "setembro", "outubro", "novembro", "dezembro"]
    s = ["sim", "Sim", "SIM"]

    n = input("Digite o nome da arvore: ")

    while True:
        p = input("A arvore é frutifera? ")
        if p in s:
            fu = input("Qual o nome da fruta? ")
            break
        else:
            fu = "não frutifera"
            break

    while True:
        f = input("A arvore tem folhas? ")
        if f in s:
            fo = input("Qual a cor das folhas? ")
            if fo in folhas_cor:
                break
            else:
                print("resposta invalida!")
                continue
        elif f not in s:
            fo = "sem folhas"
            break

    while True:
        t = input("Qual a cor do tronco? ")
        if t in tronco_cor:
            break
        else:
            print("Essa resposta não é válida.")
            continue

    while True:
        c = input("Em que mês estamos? ")
        if c in inverno:
            estacao = "inverno"
            break
        elif c in verao:
            estacao = "verão"
            break
        else:
            print("Essa resposta não é válida.")
            continue

    arvore = Arvore(n, fo, t, estacao)
    frutifera = ArvoreFrutiferas(fu)
    print("------------| Status |------------")
    print(f"nome: {arvore.nome}")
    print(f"folhas: {arvore.folhas}")
    print(f"fruta: {frutifera.frutas}")
    print(f"tronco: {arvore.tronco}")
    print(f"estação: {arvore.calendario_climatico}")
menu()