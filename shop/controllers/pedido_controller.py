from mysql.connector import Error
from models.cliente import cliente_existe  # <-- Importação corrigida
from models.usuario import usuario_existe
from models.produto import produto_existe
from models.pedido import criar_pedido, listar_pedidos, confirmar_pedido, excluir_pedido, pedido_existe
from views.pedido_views import mostrar_menu_pedido, coletar_dados_pedido, mostrar_pedidos, coletar_id_pedido
def menu_pedido():
    while True:
        try:
            opcao = mostrar_menu_pedido()
            
            # Listar Pedidos
            if opcao == "1":
                try:
                    pedidos = listar_pedidos()
                    mostrar_pedidos(pedidos)
                except Error as e:
                    print(f"Erro ao listar pedidos: {e}")
            
            # Adicionar Pedido
            elif opcao == "2":
                try:
                    cliente_id, vendedor_id, itens = coletar_dados_pedido()
                    
                    # Validação de existência
                    if not cliente_existe(cliente_id):
                        print("Erro: Cliente não encontrado!")
                        continue
                        
                    if not usuario_existe(vendedor_id):
                        print("Erro: Vendedor não encontrado!")
                        continue
                        
                    for produto_id, _ in itens:
                        if not produto_existe(produto_id):
                            print(f"Erro: Produto ID {produto_id} não existe!")
                            continue
                    
                    criar_pedido(cliente_id, vendedor_id, itens)
                    print("Pedido criado com sucesso!")
                    
                except Error as e:
                    print(f"Erro ao criar pedido: {e}")
            
            # Confirmar Pedido
            elif opcao == "3":
                try:
                    pedido_id = coletar_id_pedido()
                    if not pedido_existe(pedido_id):
                        print("Erro: Pedido não encontrado!")
                        continue
                        
                    confirmar_pedido(pedido_id)
                    print("Pedido confirmado com sucesso!")
                    
                except Error as e:
                    print(f"Erro ao confirmar pedido: {e}")
            
            # Excluir Pedido
            elif opcao == "4":
                try:
                    pedido_id = coletar_id_pedido()
                    if not pedido_existe(pedido_id):
                        print("Erro: Pedido não encontrado!")
                        continue
                        
                    excluir_pedido(pedido_id)
                    print("Pedido excluído com sucesso!")
                    
                except Error as e:
                    print(f"Erro ao excluir pedido: {e}")
            
            # Sair
            elif opcao == "5":
                break
                
            else:
                print("Opção inválida! Digite um número entre 1 e 5.")
                
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")