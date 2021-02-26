from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 
app.config['MYSQL_DB'] = 'school_flask'


@app.route('/')
def index():
    return "Flask running"


@app.route('/read_school')
def read_school():
    mycursor = mysql.connection.cursor()
    mycursor.execute('SELECT * FROM school_v')
    data = mycursor.fetchall()
    mycursor.close()
    return render_template('read_school.html', data= data)
    

if __name__ == "__main__":
    app.run(port=3000, debug=True)

