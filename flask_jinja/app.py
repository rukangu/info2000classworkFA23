from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title = 'Home')

@app.route('/view_students') # view all the students on file
def view():
    return render_template('view_records.html', title = 'view records')

@app.route('/add_student')
def add():
    return render_template('add_record.html', title = 'add records')


if __name__ == '__main__':
    app.run(debug=True)