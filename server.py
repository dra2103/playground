from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return ("LEts PLay a GaMe")

@app.route('/play')
def play():
    return render_template("index.html")


@app.route('/play/<int:num>')
def play_color(num):
    num = num
    return render_template('number.html', num = num)

@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    num = num
    return render_template('color.html', num=num, color = color)


if __name__ == "__main__":
    app.run(debug=True)
