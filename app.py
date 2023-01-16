from flask import Flask,request, jsonify
from flaskext.mysql import MySQL
from flask_cors import CORS

mysql = MySQL()
app = Flask(__name__)
CORS(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1111'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = '10.0.0.13' 
app.secret_key = "ABCDEFG"
mysql.init_app(app)

@app.route('/login', methods=['POST'])
def login():
    Json_data = request.get_json()
    
    username = Json_data['username']
    password = Json_data['password']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    data = cursor.fetchone()
    if data is not None:
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)