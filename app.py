from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

class ManagementSystem:
    conn = sqlite3.connect('projects.db')
    cur = conn.cursor()
    cur.execute('''  
                CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL FOREIGN KEY,
                description TEXT NOT NULL)
''')

    cur.execute(''' 
                CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY,
                project_id INTEGER NOT NULL,
                tarefa TEXT NOT NULL,
                dead_line DATE NOT NULL,
                FOREIGN KEY (project_id) REFERENCES projects(id))
''')

    cur.commit()
    cur.close()

    @app.route('/')
    def criar_projeto(self, nome, descricao, data_inicio, data_fim):
        conn = sqlite3.connect('projects.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO projects (nome, descricao, data_inicio, data_fim)  VALUES (? , ? , ? , ?)', (nome, descricao, data_inicio, data_fim))
        cur.commit()
        cur.close()

    @app.route('/listar-projetos')
    def listar_projetos(self):
        conn = sqlite3.connect('projects.db')
        cur = conn.cursor()
        cur.execute('SELECT nome, deadline FROM projects')
        projetos = cur.fetchall()
        return projetos 
        
    
        