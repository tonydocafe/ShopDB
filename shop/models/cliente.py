from mysql.connector import Error
from models.db import conectar

def criar_cliente(nome, cpf, telefone=None, email=None):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                sql = "INSERT INTO clientes (nome, cpf, telefone, email) VALUES (%s, %s, %s, %s)"
                valores = (nome, cpf, telefone, email)
                cursor.execute(sql, valores)
                conexao.commit()
                print("Cliente criado com sucesso!")
        except Error as e:
            print(f"Erro ao criar cliente: {e}")
        finally:
            conexao.close()

def listar_clientes():
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT id, nome, cpf, telefone, email FROM clientes")
                clientes = cursor.fetchall()
                return clientes
        except Error as e:
            print(f"Erro ao listar clientes: {e}")
        finally:
            conexao.close()
    return []

def atualizar_cliente(id_cliente, novo_nome, novo_telefone=None):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                sql = "UPDATE clientes SET nome = %s, telefone = %s, editado = NOW() WHERE id = %s"
                valores = (novo_nome, novo_telefone, id_cliente)
                cursor.execute(sql, valores)
                conexao.commit()
                print("Cliente atualizado com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar cliente: {e}")
        finally:
            conexao.close()

def deletar_cliente(id_cliente):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                sql = "DELETE FROM clientes WHERE id = %s"
                cursor.execute(sql, (id_cliente,))
                conexao.commit()
                print("Cliente deletado com sucesso!")
        except Error as e:
            print(f"Erro ao deletar cliente: {e}")
        finally:
            conexao.close()

def cliente_existe(id_cliente):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT id FROM clientes WHERE id = %s", (id_cliente,))
                return cursor.fetchone() is not None
        except Error as e:
            print(f"Erro ao verificar cliente: {e}")
            return False
        finally:
            conexao.close()
    return False


def clientes_menos_compraram(limite=1):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                cursor.execute("""
                    SELECT c.id, c.nome, COUNT(p.id) as total_pedidos, SUM(p.total) as total_gasto
                    FROM clientes c
                    LEFT JOIN pedidos p ON c.id = p.cliente_id AND p.status = 'Pago'
                    GROUP BY c.id
                    ORDER BY total_gasto ASC
                    LIMIT %s
                """, (limite,))
                return cursor.fetchall()
        except Error as e:
            print(f"Erro ao buscar clientes: {e}")
            return []
        finally:
            conexao.close()
    return []