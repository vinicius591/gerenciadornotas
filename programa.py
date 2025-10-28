from funcoes import *
listaAlunos = []

while True:
    no = int(input("Digite conforme o que deseja: 1 para adicionar um aluno, 2 para exibir relatorio e 0 para sair do programa: "))
    listaNotas = []
    if no == 1: 
        nomes = input("Digite o nome do aluno: ")
        for i in range (1, 4):
            notas = float(input(f"Digite a {i}° nota do aluno: "))
            listaNotas.append(notas)
        medias= calcular_media(listaNotas)
        situ= situacao(medias)
        aluno= {
            "nome": nomes,
            "notas": listaNotas,
            "media": medias,
            "situacao": situ
        }
        
        listaAlunos.append(aluno)
        print(f"\nAluno {nomes} adicionado!")

    elif no == 2:   
        if len(listaAlunos) == 0:
            print("\nNenhum aluno cadastrado ainda.")
        else:
            print("Relatorio dos alunos:")
            for aluno in listaAlunos:
                print(f"\nNome: {aluno['nome']}")
                print(f"\nNotas: {aluno['notas']}")
                print(f"\nMédia: {aluno['media']:.2f}")
                print(f"\nSituação: {aluno['situacao']}")
    elif no == 0:
        print("\nPrograma finalizado")
        break
            
