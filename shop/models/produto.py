from mysql.connector import Error
from models.db import conectar

def criar_produto(nome, descricao, preco, estoque):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                sql = "INSERT INTO produtos (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s)"
                valores = (nome, descricao, preco, estoque)
                cursor.execute(sql, valores)
                conexao.commit()
                print("Produto criado com sucesso!")
        except Error as e:
            print(f"Erro ao criar produto: {e}")
        finally:
            conexao.close()

def listar_produtos():
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT id, nome, descricao, preco, estoque FROM produtos")
                produtos = cursor.fetchall()
                return produtos
        except Error as e:
            print(f"Erro ao listar produtos: {e}")
        finally:
            conexao.close()
    return []

def atualizar_produto(id_produto, novo_nome, novo_preco, novo_estoque):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                sql = "UPDATE produtos SET nome = %s, preco = %s, estoque = %s, editado = NOW() WHERE id = %s"
                valores = (novo_nome, novo_preco, novo_estoque, id_produto)
                cursor.execute(sql, valores)
                conexao.commit()
                print("Produto atualizado com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar produto: {e}")
        finally:
            conexao.close()

def deletar_produto(id_produto):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                sql = "DELETE FROM produtos WHERE id = %s"
                cursor.execute(sql, (id_produto,))
                conexao.commit()
                print("Produto deletado com sucesso!")
        except Error as e:
            print(f"Erro ao deletar produto: {e}")
        finally:
            conexao.close()


def produto_existe(id_produto):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT id FROM produtos WHERE id = %s", (id_produto,))
                return cursor.fetchone() is not None
        except Error as e:
            print(f"Erro ao verificar produto: {e}")
            return False
        finally:
            conexao.close()
    return False


def produto_mais_vendido():
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                cursor.execute("""
                    SELECT p.id, p.nome, SUM(ip.quantidade) as total_vendido
                    FROM itens_pedido ip
                    JOIN pedidos pd ON ip.pedido_id = pd.id
                    JOIN produtos p ON ip.produto_id = p.id
                    WHERE pd.status = 'Pago'
                    GROUP BY p.id
                    ORDER BY total_vendido DESC
                    LIMIT 1
                """)
                resultado = cursor.fetchone()
                return resultado if resultado else None
        except Error as e:
            print(f"Erro ao buscar produto mais vendido: {e}")
            return None
        finally:
            conexao.close()
    return None