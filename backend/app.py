from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")

# Função para inicializar o banco de dados
def init_db():
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS quartos
                 (id INTEGER PRIMARY KEY,
                  estado TEXT,
                  cliente TEXT,
                  email TEXT,
                  checkin TEXT,
                  checkout TEXT,
                  valor REAL)''')
    conn.commit()
    conn.close()

# Rota para listar todos os quartos
@app.route('/api/quartos', methods=['GET'])
def get_quartos():
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute('SELECT * FROM quartos')
    quartos = c.fetchall()
    conn.close()
    return jsonify(quartos)

# Rota para criar um novo quarto
@app.route('/api/quartos', methods=['POST'])
def create_quarto():
    data = request.get_json()
    estado = data.get('estado')
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute("INSERT INTO quartos (estado) VALUES (?)", (estado,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Quarto criado com sucesso!'})

# Rota para atualizar o estado de um quarto
@app.route('/api/quartos/<int:quarto_id>', methods=['PUT'])
def update_quarto(quarto_id):
    data = request.get_json()
    estado = data.get('estado')
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute("UPDATE quartos SET estado=? WHERE id=?", (estado, quarto_id))
    conn.commit()
    conn.close()
    return jsonify({'message': f'Estado do quarto {quarto_id} atualizado com sucesso!'})

# Rota para deletar um quarto
@app.route('/api/quartos/<int:quarto_id>', methods=['DELETE'])
def delete_quarto(quarto_id):
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute("DELETE FROM quartos WHERE id=?", (quarto_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': f'Quarto {quarto_id} deletado com sucesso!'})

# Rota para realizar o check-in de um cliente
@app.route('/api/checkin/<int:quarto_id>', methods=['POST'])
def checkin(quarto_id):
    data = request.get_json()
    cliente = data.get('cliente')
    email = data.get('email')
    checkin_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute("UPDATE quartos SET estado=?, cliente=?, email=?, checkin=? WHERE id=?", ('ocupado', cliente, email, checkin_time, quarto_id))
    conn.commit()
    conn.close()
    return jsonify({'message': f'Check-in realizado com sucesso no quarto {quarto_id}!'})

# Rota para realizar o check-out de um cliente
@app.route('/api/checkout/<int:quarto_id>', methods=['POST'])
def checkout(quarto_id):
    checkout_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('hotel.db')
    c = conn.cursor()
    c.execute("SELECT cliente, email, checkin FROM quartos WHERE id=?", (quarto_id,))
    result = c.fetchone()
    if result:
        cliente, email, checkin_time = result
        checkin_time = datetime.strptime(checkin_time, '%Y-%m-%d %H:%M:%S')
        tempo_hospedagem = (datetime.now() - checkin_time).total_seconds() / 3600.0
        valor = calcular_valor(tempo_hospedagem)  # Função para calcular o valor da hospedagem
        c.execute("UPDATE quartos SET estado=?, checkout=?, valor=? WHERE id=?", ('aberto', checkout_time, valor, quarto_id))
        conn.commit()
        conn.close()
        return jsonify({'message': f'Check-out realizado com sucesso no quarto {quarto_id}! Valor a pagar: R$ {valor:.2f}'})
    else:
        conn.close()
        return jsonify({'message': f'Quarto {quarto_id} não está ocupado!'})

# Função para calcular o valor da hospedagem (pode ser personalizada de acordo com as regras do hotel)
def calcular_valor(tempo_hospedagem):
    valor_por_hora = 50  # Exemplo de valor por hora
    return tempo_hospedagem * valor_por_hora

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
