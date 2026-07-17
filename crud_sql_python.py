import pymysql

# Configurações de acesso
config = {
    
    'host': 'localhost',
    'user': 'vagner_user',
    'password': 'sua_senha',
    'database': 'crud_mysql',
    'cursorclass': pymysql.cursors.DictCursor # Retorna os dados como dicionários
}

try:
    # Estabelece a conexão
    connection = pymysql.connect(**config)
    print("Conectado diretamente com PyMySQL!")
  
    connection.close()
except Exception as e:
    print(f"Erro: {e}")


# Neste exemplo estou fazendo um crud.
# O banco de dados tem duas tabelas, uma 
# chamada autores e outra chamada posts.

def inserir_dados():
    print('====================================================')
    print('Opção 1 - Inserir dados')
    print('====================================================')
    
    connection = pymysql.connect(**config)   
    
    try:
        # cursor a partir da conexão
        with connection.cursor() as cursor:
            
            nome = input('Insira o nome do autor: ')    
           
            sql = "INSERT INTO autores (nome) VALUES (%s)"
            
            # O parâmetro deve ser uma tupla (nome,) ou lista [nome]
            cursor.execute(sql, (nome,))
            
        # Commit deve ser feito na conexão
        connection.commit()
        print("Dados inseridos com sucesso!")
        
    finally:
        connection.close()
        
def listar_dados():
    print('====================================================')
    print('Opção 2 - Listar Autores')
    print('====================================================')
    
    connection = pymysql.connect(**config) 
    
    try:
        # cursor a partir da conexão
        with connection.cursor() as cursor:           
                        
            sql = "SELECT * FROM autores"
            
            # O parâmetro deve ser uma tupla (nome,) ou lista [nome]
            cursor.execute(sql)            
            
            resultados = cursor.fetchall()     
            
            if not resultados:
                print("Nenhum autor encontrado.")
            else:
                for linha in resultados:
                    #print(f"ID: {linha[0]} | Nome: {linha[1]}")
                    print(f"ID: {linha['id']} | Nome: {linha['nome']}")
               
    finally:
        connection.close()
        
def atualizar_dados():
    print('====================================================')
    print('Opção 3 - Atualizar dados')
    print('====================================================')
    
    connection = pymysql.connect(**config) 
    
    try:
        with connection.cursor() as cursor:           
            
            cursor.execute("SELECT id, nome FROM autores")            
            resultados = cursor.fetchall()     
            
            if not resultados:
                print("Nenhum autor encontrado.")
                return

            for linha in resultados:
                print(f"ID: {linha['id']} | Nome: {linha['nome']}")
            
            nome_selecionado = input('\nDigite o nome para atualizar: ')            
            nome_atualizado = input('\nDigie o nome atualizado: ')
                        
            sql_atualizar = "UPDATE autores SET nome = %s WHERE nome = %s"

            linhas_afetadas = cursor.execute(sql_atualizar, (nome_atualizado, nome_selecionado))
            
            if linhas_afetadas > 0:
                connection.commit() 
                print(f'Sucesso: Autor "{nome_selecionado}" atualizado para "{nome_atualizado}"')
               
            else:
                print('Erro: Nome não encontrado no banco de dados!')
                
    except Exception as e:
        print(f"Erro na operação: {e}")
    finally:
        connection.close() 
        
def excluir_dados():
    print('====================================================')
    print('Opção 4 - Excluir dados')
    print('====================================================')
    
    connection = pymysql.connect(**config) 
    
    try:
        with connection.cursor() as cursor:           
            
            cursor.execute("SELECT id, nome FROM autores")            
            resultados = cursor.fetchall()     
            
            if not resultados:
                print("Nenhum autor encontrado.")
                return

            for linha in resultados:
                print(f"ID: {linha['id']} | Nome: {linha['nome']}")
            
            nome_selecionado = input('\nDigite o nome para excluir: ')           
                        
            sql_delete = "DELETE FROM autores WHERE nome = %s"
            linhas_afetadas = cursor.execute(sql_delete, (nome_selecionado,))
            
            if linhas_afetadas > 0:
                connection.commit() 
                print(f'Sucesso: Autor "{nome_selecionado}" removido!')
            else:
                print('Erro: Nome não encontrado no banco de dados!')
                
    except Exception as e:
        print(f"Erro na operação: {e}")
    finally:
        connection.close()    
                
def crud():
    print('====================================================')
    print('Selecione a opção desejada')              
    print('Opção 1 - Inserir dados')
    print('Opção 2 - Listar dados')
    print('Opção 3 - Atualizar dados')
    print('Opção 4 - Excluir dados')
    print('====================================================')
                  
    opcao = int(input('Digite sua opção!'))
                
    if opcao == 1: 
        inserir_dados()
    elif opcao == 2:
        listar_dados()  
    elif opcao == 3:
        atualizar_dados()
    elif opcao == 4:        
        excluir_dados()
    else:
        print('Erro! Número Inválido!')

def loop():
    resp = 's' 
    
    while resp == 's':
        crud()        
       
        resp = input('\nDeseja repetir? (s) p/ Sim, (n) para Não: ').lower()
        
        if resp == 'n':
            print("Encerrando o programa...")
        

if __name__ == "__main__":
    loop()


