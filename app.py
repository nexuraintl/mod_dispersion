import os
import mysql.connector
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/conexion', methods=['POST'])
def insert_dispersion():
    try:
        data = request.get_json()

        host = data.get('host')
        user = data.get('user')
        password = data.get('password')
        database = data.get('database')


        MYSQL_CONFIG = {
        'host': os.getenv('DB_HOST', host),
        'user': os.getenv('DB_USER', user),
        'password': os.getenv('DB_PASSWORD', password),
        'database': os.getenv('DB_NAME', database),
        }



        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()

        query = "SELECT * FROM `tn_sx_cliente_comu`"
        cursor.execute(query)
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({'message': 'Registro: '.query}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'status': 'API OK'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)


