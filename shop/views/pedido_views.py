def mostrar_menu_pedido():
    print("\n--- Gerenciar Pedidos ---")
    print("1. Listar Pedidos")
    print("2. Adicionar Pedido")
    print("3. Confirmar Pedido")
    print("4. Excluir Pedido")
    print("5. Voltar")
    return input("Escolha uma opção: ")

def coletar_dados_pedido():
    cliente_id = input("ID do Cliente: ")
    vendedor_id = input("ID do Vendedor: ")
    itens = []
    while True:
        produto_id = input("ID do Produto (ou 'sair' para finalizar): ")
        if produto_id.lower() == 'sair':
            break
        quantidade = int(input("Quantidade: "))
        itens.append((produto_id, quantidade))
    return cliente_id, vendedor_id, itens

def coletar_id_pedido():
    return input("ID do Pedido: ")

def mostrar_pedidos(pedidos):
    if not pedidos:
        print("Nenhum pedido encontrado.")
        return
    
    print("\n--- Lista de Pedidos ---")
    for pedido in pedidos:
        print(f"ID: {pedido[0]} | Cliente: {pedido[1]} | Vendedor: {pedido[2]} | Total: R${pedido[3]} | Status: {pedido[4]}")