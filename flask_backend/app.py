from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/info')
def handle_info():
    return render_template('hello_info.html', greeting = "Hi") 

if __name__ == '__main__':
    app.run(debug=True)