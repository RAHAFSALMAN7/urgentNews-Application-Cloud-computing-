from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host='mysql-urgentnews',
        user='root',
        password='root_password',
        database='urgentNews'
    )
    return connection

@app.route('/getUrgentNews', methods=['GET'])
def get_urgent_news():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT title, content FROM News')
    news = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(news)