from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

class SistemaGestao:
    conn = sqlite3.connect('tarefas.db')
    cur = conn.cursor()
    cur.execute('''  
                CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                prioridade INTEGER NOT NULL)
''')
    conn.commit()
    conn.close()

    def criar_tarefa(self, name, prioridade):
        conn = sqlite3.connect('tarefas.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO tarefas (name, prioridade)  VALUES (? , ?)', (name, prioridade))
        conn.commit()
        conn.close()

    def listar_tarefas(self):
        conn = sqlite3.connect('tarefas.db')
        cur = conn.cursor()
        cur.execute('SELECT id, name, prioridade FROM tarefas')
        tarefas = cur.fetchall()
        return tarefas 
    
    def limpar_banco(self):
        conn = sqlite3.connect('tarefas.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM tarefas')
        conn.commit()
        conn.close()
    
    def limpar_tarefa(self, tarefa_id):
        conn = sqlite3.connect('tarefas.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
        conn.commit()
        conn.close()

sistema = SistemaGestao()

@app.route("/", methods = ["POST", "GET"])
def index():
    if request.method == "POST":
        name = request.form['name']
        prioridade = request.form['prioridade']
        sistema.criar_tarefa(name, prioridade)
    
    tarefa = sistema.listar_tarefas()
    return render_template("index.html", tarefa = tarefa)

@app.route("/limpar-banco", methods = ["POST"])
def limpar_banco_dados():
    sistema.limpar_banco()
    tarefa = sistema.listar_tarefas()
    return render_template("index.html", tarefa = tarefa)

@app.route('/limpar-tarefa/<int:tarefa_id>', methods = ["POST"])
def limpar_id_tarefa(tarefa_id):
    sistema.limpar_tarefa(tarefa_id)
    tarefa = sistema.listar_tarefas()
    return render_template("index.html", tarefa = tarefa)

if __name__ == "__main__":
    app.run(debug = True)