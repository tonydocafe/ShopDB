from controllers.usuario_controller import menu_usuario
from controllers.produto_controller import menu_produto
from controllers.cliente_controller import menu_cliente
from controllers.pedido_controller import menu_pedido

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Produtos")
        print("3. Gerenciar Clientes")
        print("4. Gerenciar Pedidos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_usuario()
        elif opcao == "2":
            menu_produto()
        elif opcao == "3":
            menu_cliente()
        elif opcao == "4":
            menu_pedido()
        elif opcao == "5":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()