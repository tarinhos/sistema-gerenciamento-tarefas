def mostrar_menu():
    print("\n=== Sistema de Gerenciamento de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")


def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ")
    tarefas.append({"descricao": descricao, "concluida": False})
    print("Tarefa adicionada com sucesso!")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else "✘"
        print(f"{i} - {tarefa['descricao']} [{status}]")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa concluída: "))
        tarefas[indice]["concluida"] = True
        print("Tarefa marcada como concluída!")
    except (ValueError, IndexError):
        print("Entrada inválida.")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a remover: "))
        tarefas.pop(indice)
        print("Tarefa removida com sucesso!")
    except (ValueError, IndexError):
        print("Entrada inválida.")


def main():
    tarefas = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
