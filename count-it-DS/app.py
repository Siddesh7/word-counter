from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/counter', methods=['POST'])
def count():
    para = request.form['main']
    c = para.split()
    return render_template('counter.html', count=len(c))


if __name__ == "__main__":
    app.debug = True
    app.run()
