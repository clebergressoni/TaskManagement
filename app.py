from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

class ManagementSystem:
    conn = sqlite3.connect('tarefas.db')
    cur = conn.cursor()
    cur.execute('''  
                CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL FOREIGN KEY,
                prioridade INTEGER NOT NULL)
''')
    cur.commit()
    cur.close()

    @app.route('/')
    def criar_tarefa(self, nome, prioridade):
        conn = sqlite3.connect('tarefas.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO tarefas (nome, prioridade)  VALUES (? , ?)', (nome, prioridade))
        cur.commit()
        cur.close()

    @app.route('/listar-tarefas')
    def listar_tarefas(self):
        conn = sqlite3.connect('projects.db')
        cur = conn.cursor()
        cur.execute('SELECT nome, prioridade FROM projects')
        projetos = cur.fetchall()
        return projetos 
        
    
        