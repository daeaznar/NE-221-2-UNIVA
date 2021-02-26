from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Running Python with Flask - UNIVA NE. Student: David Hernández"


@app.route('/home/<user_name>')
def home(user_name):
    # return "Welcome HOME " + user_name
    return """
        Welcome HOME Student {}
    """.format(user_name)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hello/<user_name>')
def hello(user_name):
    return render_template('hello.html', user=user_name)


@app.route('/w3schools')
def w3schools():
    return redirect("https://www.w3schools.com/python/")


@app.route('/python')
def python():
    return redirect(url_for('w3schools'))


if __name__ == "__main__":
    app.run(port=3000, debug=True)
