#banco de dados que salva green e red das apostas.
import sqlite3 

def conectar_banco(aposta_banco):
    conexao = sqlite3.connect(aposta_banco)
    return conexao

def apostas(conexao, tabela, valor, odd):
    cursor = conexao.cursor()
    odd_formatado = f"{odd / 100:.2f}"

    # Inserir dados na tabela RED ou GREEN
    if tabela == 'RED':
        cursor.execute('''INSERT INTO RED (valor, odd) VALUES(?, ?)''', (valor, odd_formatado))
    elif tabela == 'GREEN':
        cursor.execute('''INSERT INTO GREEN (valor, odd) VALUES(?, ?)''', (valor, odd_formatado))

    conexao.commit()

def tabelas(conexao):
    cursor = conexao.cursor()

    # Criando as tabelas no banco
    cursor.execute('''CREATE TABLE IF NOT EXISTS RED(id INTEGER PRIMARY KEY AUTOINCREMENT,
                   valor REAL NOT NULL, odd REAL NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS GREEN(id INTEGER PRIMARY KEY AUTOINCREMENT,
                   valor REAL NOT NULL, odd REAL NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS RESULTADOS(id INTEGER PRIMARY KEY AUTOINCREMENT,
                   valor REAL NOT NULL, odd REAL NOT NULL, status TEXT NOT NULL)''')

    conexao.commit()

# Iniciar programa
if __name__ == '__main__':
    conexao = conectar_banco('apostas.db')
    tabelas(conexao)

    # Solicitar para o usuário inserir valor e odd
    tabela = input("Sua aposta deu GREEN ou RED? ").strip().upper()
    if tabela not in ['RED', 'GREEN']:
        print('Tabela inválida, aposta não feita.')
    else:
        try:
            valor = float(input("Valor da aposta: "))
            odd_formatado = float(input("Valor da odd (3 dígitos numéricos): "))
            
            # Chamar a função apostas para salvar no banco
            apostas(conexao, tabela, valor, odd_formatado)
            print('Aposta feita com sucesso!')
        except ValueError:
            print('Valor inválido para a aposta ou odd.')
    
    conexao.close()
    print("Conexão fechada")