def mostrar_menu_cliente():
    print("\n--- Gerenciar Clientes ---")
    print("1. Listar Clientes")
    print("2. Adicionar Cliente")
    print("3. Atualizar Cliente")
    print("4. Deletar Cliente")
    print("5. Voltar")
    print("6. Clientes que Menos Compraram")  # Nova opção
    return input("Escolha uma opção: ")


def coletar_dados_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    return nome, cpf, telefone, email

def coletar_dados_atualizacao_cliente():
    id_cliente = input("ID do Cliente: ")
    novo_nome = input("Novo Nome: ")
    novo_telefone = input("Novo Telefone: ")
    return id_cliente, novo_nome, novo_telefone

def mostrar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente encontrado.")
        return
    
    print("\n--- Lista de Clientes ---")
    for cliente in clientes:
        print(f"""ID: {cliente[0]} | Nome: {cliente[1]}
CPF: {cliente[2]} | Telefone: {cliente[3]}
Email: {cliente[4]}...
----------------------------------------------------------------------------------""")
def coletar_id_cliente():
    return input("ID do Cliente: ")

def mostrar_clientes_menos_compraram(clientes):
    if not clientes:
        print("\nNenhum dado de compras disponível.")
        return
    
    print("\n--- Clientes com Menor Volume de Compras ---")
    for cliente in clientes:
        print(f"""ID: {cliente[0]}
Nome: {cliente[1]}
Total de Pedidos: {cliente[2]}
Valor Total Gasto: R${cliente[3] or 0:.2f}""")
