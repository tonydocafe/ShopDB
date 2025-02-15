from models.db import conectar
from mysql.connector import Error

def criar_usuario(nome, cpf, login, password, tipo_usuario):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                sql = """
                INSERT INTO usuarios (nome, cpf, login, password, tipo_usuario, cadastrado) 
                VALUES (%s, %s, %s, %s, %s, NOW())
                """
                valores = (nome, cpf, login, password, tipo_usuario)
                cursor.execute(sql, valores)
                conexao.commit()
                print("Usuário criado com sucesso!")
        except Error as e:
            print(f"Erro ao criar usuário: {e}")
        finally:
            conexao.close()

def listar_usuarios():
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT id, nome, cpf, login, tipo_usuario FROM usuarios")
                usuarios = cursor.fetchall()
                return usuarios
        except Error as e:
            print(f"Erro ao listar usuários: {e}")
        finally:
            conexao.close()
    return []

def atualizar_usuario(id_usuario, novo_nome, novo_cpf, novo_login, novo_password, novo_tipo_usuario):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                sql = """
                UPDATE usuarios 
                SET nome = %s, cpf = %s, login = %s, password = %s, tipo_usuario = %s, editado = NOW() 
                WHERE id = %s
                """
                valores = (novo_nome, novo_cpf, novo_login, novo_password, novo_tipo_usuario, id_usuario)
                cursor.execute(sql, valores)
                conexao.commit()
                print("Usuário atualizado com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar usuário: {e}")
        finally:
            conexao.close()

def deletar_usuario(id_usuario):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                sql = "DELETE FROM usuarios WHERE id = %s"
                cursor.execute(sql, (id_usuario,))
                conexao.commit()
                print("Usuário deletado com sucesso!")
        except Error as e:
            print(f"Erro ao deletar usuário: {e}")
        finally:
            conexao.close()

def usuario_existe(id_usuario):
    conexao = conectar()
    if conexao:
        try:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT id FROM usuarios WHERE id = %s", (id_usuario,))
                return cursor.fetchone() is not None
        except Error as e:
            print(f"Erro ao verificar usuário: {e}")
            return False
        finally:
            conexao.close()
    return False