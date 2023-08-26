import sqlite3

class aluno_model():
    
    def __init__(self):
        self.conexao = sqlite3.connect("SERPRO")
        self.cursor = self.conexao.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS tb_alunos"
                            '('
                            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'nome TEXT NOT NULL,'
                            'idade INTEGER NOT NULL,'
                            'pese REAL NOT NULL'
                            ' )'
            )
        self.conexao.commit()
        self.cursor.close()
        
    
    
    