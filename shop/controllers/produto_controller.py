from models.produto import criar_produto, listar_produtos, atualizar_produto, deletar_produto, produto_mais_vendido
from views.produto_views import mostrar_menu_produto, coletar_dados_produto, coletar_dados_atualizacao_produto, mostrar_produtos, coletar_id_produto, mostrar_produto_mais_vendido


def menu_produto():
    while True:
        opcao = mostrar_menu_produto()
        if opcao == "1":
            produtos = listar_produtos()
            mostrar_produtos(produtos)
        elif opcao == "2":
            dados = coletar_dados_produto()
            criar_produto(*dados)
        elif opcao == "3":
            dados = coletar_dados_atualizacao_produto()
            atualizar_produto(*dados)
        elif opcao == "4":
            id_produto = coletar_id_produto()
            deletar_produto(id_produto)
        elif opcao == "5":
            break
        elif opcao == "6":  # Nova opção
            mais_vendido = produto_mais_vendido()
            mostrar_produto_mais_vendido(mais_vendido)
        else:
            print("Opção inválida!")