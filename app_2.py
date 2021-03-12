from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'school_flask'

mysql = MySQL(app)

@app.route('/')
def index():
    return "Flask running"

#READ ALL DATA
@app.route('/read_school')
def read_school():
    mycursor = mysql.connection.cursor()
    mycursor.execute('SELECT * FROM school_v')
    schools = mycursor.fetchall()
    mycursor.close()
    return render_template('read_school.html', schools = schools)

 
#INSERT FROM   
@app.route('/insert_school')
def insert_school():
    return render_template('insert_school.html')


#INSER INTO
@app.route('/insert_values_school', methods=['POST'])
def insert_values_school():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        print(name, description)
        mycursor = mysql.connection.cursor()
        mycursor.execute("INSERT INTO school (name, description) VALUES (%s, %s)", (name, description))
        mysql.connection.commit()
        print("Inserted")
        mycursor.close()
        #return "insert_values_school"
        return redirect(url_for('read_school'))
    

#READ with parameter
@app.route('/read_one_school/<id>', methods=['GET', 'POST'])
def read_one_school(id):
    print(id)
    mycursor = mysql.connection.cursor()
    mycursor.execute('SELECT * FROM school_v WHERE id = %s', (id))
    school = mycursor.fetchall()
    mycursor.close()
    print(school[0])
    #return "read_one_school"
    return render_template('read_one_school.html', school = school[0])


#UPDATE records
@app.route('/update_one_school/<id>', methods=['POST'])
def update_one_school(id):
    print(id)
    if request.method=='POST':
        name = request.form['name']
        description = request.form['description']
        print(name, description)
        mycursor = mysql.connection.cursor()
        mycursor.execute('UPDATE school SET name = %s, description = %s WHERE id = %s', (name, description, id))
        mysql.connection.commit()
        mycursor.close()
        #return "update_one_school"
        return redirect(url_for('read_school'))

if __name__ == "__main__":
    app.run(port=3000, debug=True)

