from flask import Flask, render_template, request, redirect, url_for
from info2000_package import info_logger
from info2000_package import student_details

DB_FILE = "student_db.txt"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title = 'Home')

@app.route('/view_students') # view all the students on file
def view():
    title = request.args.get('title')
    if title == None:
        title = 'View Student'
    
    with open (DB_FILE,'r') as f:
        lines = f.readlines()
        lines = [line.strip('\n') for line in lines] # strip the new line
        students = []
        for line in lines:
            _,student_details = line.split(',')
            student_details = student_details.strip(" ")
            print(student_details)
            first_name, last_name, level, color = student_details.split()
            students.append({"first_name":first_name, "last_name":last_name, "level":level, "color":color})
    
    context = {
        "title":title,
        "students":students
    }
    # return render_template('view_students.html', title = title, students = students) #works too
    return render_template('view_records.html', **context)

@app.route('/add_student/')
def add():
    return render_template('add_record.html', title = 'add records')

@app.route('/student_form/', methods = ['POST'])
def HandleStudent():
    # add student to database
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    color = request.form.get('Favorite Color')
    level = request.form.get('level')

    my_logger = info_logger.Logger(DB_FILE)
    my_logger.LogRow(f"{first_name} {last_name} {level} {color}")

    return redirect(url_for('view',title = f'{first_name}_{last_name}')) # the title of the view page will be the name of the newly added student


if __name__ == '__main__':
    app.run(debug=True)