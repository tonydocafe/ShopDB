from mysql.connector import Error  # Adicionar no início do arquivo
from models.db import conectar

# Restante do código permanece igual...
def criar_pedido(cliente_id, vendedor_id, itens):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                # Inserir o pedido
                sql_pedido = "INSERT INTO pedidos (cliente_id, vendedor_id) VALUES (%s, %s)"
                cursor.execute(sql_pedido, (cliente_id, vendedor_id))
                pedido_id = cursor.lastrowid

                # Inserir itens do pedido
                total_pedido = 0
                for item in itens:
                    produto_id, quantidade = item
                    cursor.execute("SELECT preco FROM produtos WHERE id = %s", (produto_id,))
                    preco_unitario = cursor.fetchone()[0]
                    subtotal = preco_unitario * quantidade
                    total_pedido += subtotal

                    sql_item = "INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario, subtotal) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql_item, (pedido_id, produto_id, quantidade, preco_unitario, subtotal))

                # Atualizar total do pedido
                sql_update_total = "UPDATE pedidos SET total = %s WHERE id = %s"
                cursor.execute(sql_update_total, (total_pedido, pedido_id))

                conexao.commit()
                print("Pedido criado com sucesso!")
        except Error as e:
            print(f"Erro ao criar pedido: {e}")
        finally:
            conexao.close()

def listar_pedidos():
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                cursor.execute("""
                    SELECT pedidos.id, clientes.nome AS cliente, usuarios.nome AS vendedor, pedidos.total, pedidos.status 
                    FROM pedidos 
                    JOIN clientes ON pedidos.cliente_id = clientes.id 
                    JOIN usuarios ON pedidos.vendedor_id = usuarios.id
                """)
                pedidos = cursor.fetchall()
                return pedidos
        except Error as e:
            print(f"Erro ao listar pedidos: {e}")
        finally:
            conexao.close()
    return []



def atualizar_pedido(pedido_id, novo_status):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                # Verificar status atual do pedido
                cursor.execute("SELECT status FROM pedidos WHERE id = %s", (pedido_id,))
                status_atual = cursor.fetchone()[0]

                # Verificar se o novo status é válido
                if novo_status not in ['Pendente', 'Confirmado', 'Cancelado']:
                    print("Status inválido. Escolha entre 'Pendente', 'Confirmado' ou 'Cancelado'.")
                    return

                # Se o pedido já foi confirmado ou cancelado, não permite alteração
                if status_atual in ['Confirmado', 'Cancelado']:
                    print(f"Não é possível alterar o status de um pedido {status_atual}.")
                    return

                # Atualizar o status do pedido
                cursor.execute(
                    "UPDATE pedidos SET status = %s, editado = NOW() WHERE id = %s",
                    (novo_status, pedido_id)
                )

                # Se o status for 'Confirmado', verificar estoque e atualizar
                if novo_status == 'Confirmado':
                    cursor.execute("SELECT produto_id, quantidade FROM itens_pedido WHERE pedido_id = %s", (pedido_id,))
                    itens = cursor.fetchall()

                    for produto_id, quantidade in itens:
                        # Verificar estoque
                        cursor.execute("SELECT estoque FROM produtos WHERE id = %s", (produto_id,))
                        estoque_atual = cursor.fetchone()[0]

                        if estoque_atual < quantidade:
                            raise Error("Estoque insuficiente para o produto ID: {}".format(produto_id))

                        # Atualizar estoque
                        cursor.execute(
                            "UPDATE produtos SET estoque = estoque - %s WHERE id = %s",
                            (quantidade, produto_id)
                        )

                conexao.commit()
                print(f"Pedido {pedido_id} atualizado para status '{novo_status}' com sucesso!")

        except Error as e:
            conexao.rollback()
            print(f"Erro ao atualizar pedido: {e}")
        finally:
            conexao.close()


def excluir_pedido(pedido_id):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                # Verificar status do pedido para restauração de estoque
                cursor.execute("SELECT status FROM pedidos WHERE id = %s", (pedido_id,))
                status = cursor.fetchone()[0]

                # Restaurar estoque se o pedido estava confirmado
                if status == 'Pago':
                    cursor.execute("SELECT produto_id, quantidade FROM itens_pedido WHERE pedido_id = %s", (pedido_id,))
                    itens = cursor.fetchall()
                    for produto_id, quantidade in itens:
                        cursor.execute(
                            "UPDATE produtos SET estoque = estoque + %s WHERE id = %s",
                            (quantidade, produto_id)
                        )

                # Deletar itens do pedido e o próprio pedido
                cursor.execute("DELETE FROM itens_pedido WHERE pedido_id = %s", (pedido_id,))
                cursor.execute("DELETE FROM pedidos WHERE id = %s", (pedido_id,))
                conexao.commit()
                print("Pedido excluído com sucesso!")

        except Error as e:
            conexao.rollback()
            print(f"Erro ao excluir pedido: {e}")
        finally:
            conexao.close()

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
    return cliente_id, vendedor_id, itens  # Retorna uma tupla com 3 elementos

def coletar_id_pedido():  # Função faltando
    return input("ID do Pedido: ")


def pedido_existe(pedido_id):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT id FROM pedidos WHERE id = %s", (pedido_id,))
                return cursor.fetchone() is not None
        except Error as e:
            print(f"Erro ao verificar pedido: {e}")
            return False
        finally:
            conexao.close()
    return False