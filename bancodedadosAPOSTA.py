import sqlite3 

def conectar_banco(aposta_banco):
    conexao = sqlite3.connect(aposta_banco)
    return conexao

#def apostas():
    #valor = 100
    #odd  = 1.85

    #valor_formatado = f"{odd:.2f}"


def tabelas(conexao):
    cursor = conexao.cursor()

    #criando tres tabelas.
    cursor.execute('''CREATE TABLE IF NOT EXISTS RED(id INTEGER PRIMARY KEY AUTOINCREMENT,
                   valor REAL NOT NULL, odd REAL NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS GREEN(id INTEGER PRIMARY KEY AUTOINCREMENT,
                   valor REAL NOT NULL, odd REAL NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS RESULTADOS(id INTEGER PRIMARY KEY AUTOINCREMENT,valor REAL NOT NULL,
                   odd REAL NOT NULL, status TEXT NOT NULL
                   )''')
    conexao.commit() 
#iniciar programa
if __name__ == '__main__':
    conexao = conectar_banco('apostas.db')
    tabelas(conexao)
    conexao.close()
    print ("tabela atualizada")       