@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = mariadb.connect(user='root', password='password', database='test')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    data = cursor.fetchone()
    if data is not None:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})
