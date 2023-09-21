import mysql.connector

def conectar_ao_mysql():
    try:
        # Crie uma conexão com o MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            #password="sua_senha_mysql",
            database="vdc"
        )
        
        if conn.is_connected():
            print("Conexão bem-sucedida ao MySQL!")
            return conn
    except Exception as e:
        print(f"Erro ao conectar ao MySQL: {str(e)}")
        return None
