from perfis import Perfil
from recomendador import Recomendador
# você ainda pode usar armazenador_de_competencias se quiser, mas aqui não é obrigatório
# from competencia import armazenador_de_competencias

def menu():
    print("\n=== Future Skills Career Advisor ===")
    print("1. Criar perfil")
    print("2. Ver recomendações de carreira")
    print("3. Sair")
    return input("Escolha: ")

perfil_atual = None
recomendador = Recomendador()

while True:
    opcao = menu()

    if opcao == "1":
        nome = input("Seu nome: ")
        perfil_atual = Perfil(nome)

        print("\nAdicione suas competências (ex: lógica, criatividade, comunicação)")
        print("Quando terminar, aperte ENTER em branco.\n")

        competencias_usuario = []

        while True:
            comp = input("Digite uma competência (ou ENTER para finalizar): ").strip().lower()

            if comp == "":
                if not competencias_usuario:
                    print("Você precisa informar pelo menos uma competência.")
                    continue
                break

            if comp in competencias_usuario:
                print("Você já adicionou essa competência.")
                continue

            competencias_usuario.append(comp)

        print("\nAgora, informe o nível (0 a 10) em cada competência:\n")

        for comp in competencias_usuario:
            while True:
                try:
                    nivel = int(input(f"Nível em '{comp}' (0 a 10): "))
                    if 0 <= nivel <= 10:
                        break
                    else:
                        print("Digite um número entre 0 e 10.")
                except ValueError:
                    print("Digite um número inteiro.")

            perfil_atual.adicionar_competencia(comp, nivel)

        print("\nPerfil criado com sucesso!")

    elif opcao == "2":
        if perfil_atual is None:
            print("\nCrie um perfil primeiro!")
        else:
            print("\n=== Suas carreiras recomendadas ===")
            recs = recomendador.recomendar(perfil_atual)
            for carreira, score in recs:
                print(f"- {carreira} (score: {score})")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
