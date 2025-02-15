from models.usuario import criar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario
from views.usuario_views import mostrar_menu_usuario, coletar_dados_usuario, coletar_dados_atualizacao_usuario, mostrar_usuarios, coletar_id_usuario

def menu_usuario():
    while True:
        opcao = mostrar_menu_usuario()
        if opcao == "1":
            usuarios = listar_usuarios()
            mostrar_usuarios(usuarios)
        elif opcao == "2":
            dados = coletar_dados_usuario()
            criar_usuario(*dados)
        elif opcao == "3":
            dados = coletar_dados_atualizacao_usuario()
            atualizar_usuario(*dados)
        elif opcao == "4":
            id_usuario = coletar_id_usuario()
            deletar_usuario(id_usuario)
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")