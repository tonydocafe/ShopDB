def mostrar_menu_produto():
    print("\n--- Gerenciar Produtos ---")
    print("1. Listar Produtos")
    print("2. Adicionar Produto")
    print("3. Atualizar Produto")
    print("4. Deletar Produto")
    print("5. Voltar")
    print("6. Produto Mais Vendido")  # Nova opção
    return input("Escolha uma opção: ")

def coletar_dados_produto():
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    return nome, descricao, preco, estoque

def coletar_dados_atualizacao_produto():
    id_produto = input("ID do Produto: ")
    novo_nome = input("Novo Nome: ")
    novo_preco = float(input("Novo Preço: "))
    novo_estoque = int(input("Novo Estoque: "))
    return id_produto, novo_nome, novo_preco, novo_estoque

def mostrar_produtos(produtos):
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    
    print("\n--- Lista de Produtos ---")
    for produto in produtos:
        print(f"""ID: {produto[0]} | Nome: {produto[1]}
Descrição: {produto[2][:30]}... | Preço: R${produto[3]:.2f}
Estoque: {produto[4]} unidades
----------------------------------------------------------------------------------""")
        
    
def coletar_id_produto():
    return input("ID do Produto: ")


def mostrar_produto_mais_vendido(produto):
    if not produto:
        print("\nNenhum produto vendido ainda ou nenhum pedido confirmado.")
        return
    
    print("\n--- Produto Mais Vendido ---")
    print(f"""ID: {produto[0]}
Nome: {produto[1]}
Total de Unidades Vendidas: {produto[2]}
Status: Pedidos Confirmados""")