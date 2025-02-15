from models.cliente import criar_cliente, listar_clientes, atualizar_cliente, deletar_cliente,clientes_menos_compraram
from views.cliente_views import mostrar_menu_cliente, coletar_dados_cliente, coletar_dados_atualizacao_cliente, mostrar_clientes, coletar_id_cliente, mostrar_clientes_menos_compraram

def menu_cliente():
    while True:
        opcao = mostrar_menu_cliente()
        if opcao == "1":
            clientes = listar_clientes()
            mostrar_clientes(clientes)
        elif opcao == "2":
            dados = coletar_dados_cliente()
            criar_cliente(*dados)
        elif opcao == "3":
            dados = coletar_dados_atualizacao_cliente()
            atualizar_cliente(*dados)
        elif opcao == "4":
            id_cliente = coletar_id_cliente()
            deletar_cliente(id_cliente)
        elif opcao == "5":
            break
        elif opcao == "6":  # Nova opção
            clientes = clientes_menos_compraram()
            mostrar_clientes_menos_compraram(clientes)
        else:
            print("Opção inválida!")
