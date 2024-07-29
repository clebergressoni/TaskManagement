from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

class ManagementSystem:
    conn = sqlite3.connect('projects.db')
    cur = conn.cursor()
    cur.execute('''  
                
                CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                start_date DATE NOT NULL,
                deadline DATE NOT NULL)
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

        