def mostrar_menu_usuario():
    print("\n--- Gerenciar Usuários ---")
    print("1. Listar Usuários")
    print("2. Adicionar Usuário")
    print("3. Atualizar Usuário")
    print("4. Deletar Usuário")
    print("5. Voltar")
    return input("Escolha uma opção: ")

def coletar_dados_usuario():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    login = input("Login: ")
    password = input("Password: ")
    tipo_usuario = input("Tipo de Usuário (Gerente, Vendedor, ADMIN): ")
    return nome, cpf, login, password, tipo_usuario

def coletar_dados_atualizacao_usuario():
    id_usuario = input("ID do Usuário: ")
    novo_nome = input("Novo Nome: ")
    novo_cpf = input("Novo CPF: ")
    novo_login = input("Novo Login: ")
    novo_password = input("Novo Password: ")
    novo_tipo_usuario = input("Novo Tipo de Usuário (Gerente, Vendedor, ADMIN): ")
    return id_usuario, novo_nome, novo_cpf, novo_login, novo_password, novo_tipo_usuario

def mostrar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário encontrado.")
        return
    
    print("\n--- Lista de Usuários ---")
    for usuario in usuarios:
        print(f"""ID: {usuario[0]} | Nome: {usuario[1]} 
CPF: {usuario[2]} | Login: {usuario[3]}
Tipo: {usuario[4]}
----------------------------------------------------------------------------------""")
        
def coletar_id_usuario():
    return input("ID do Usuário: ")