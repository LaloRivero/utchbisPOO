#set FLASK_APP=main.py
#set FLASK_DEBUG=1
#set FLASK_ENV=development

from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_pymongo import pymongo
from app import create_app
from app.form import DataForm, SearchForm, UpdateForm
from bson.json_util import dumps
import db
import json

app  = create_app()


@app.route('/')
def index():
    # response = make_response(redirect('/create_student'))
    # return response
    return render_template('options.html')


@app.route('/create_student', methods=['GET','POST'])
def create_students():
    data_form = DataForm()
    context={
        'message': 'Create Student',
        'data_form': data_form,
    }
    
    if data_form.validate_on_submit():
        student_id = data_form.student_id.data
        first_name = data_form.first_name.data.upper()
        last_name = data_form.last_name.data.upper()
        student_group = data_form.group.data
        student_email = data_form.student_email.data
    
        db.db.students.insert_one({
            'student_id': student_id,
            'first_name': first_name,
            'last_name': last_name,
            'group': student_group,
            'email': student_email
        })
        flash('Student create with success!')
        return redirect(url_for('index'))
    
    return render_template('create_student.html', **context)


@app.route('/show_students', methods=['GET'])
def show_students():
    students = list(db.db.students.find({}))
    context = {
        'students' : students
    }
    return render_template('show_students.html', **context)

    
@app.route('/search_student/<type_op>', methods=['GET', 'POST'])
def search_student(type_op):
    search_form = SearchForm()
    update_form = UpdateForm()
    flag = False
    if type_op == 'delete':
        message = 'Delete Student'
    else: 
        message = 'Update Student' 
    
    context = {
        'message': message,
        'form': search_form,
        'type_op' : type_op,
        'update_form': update_form        
    }


    if search_form.validate_on_submit():
        student_id = search_form.student_id.data
        student = db.db.students.find_one({'student_id': student_id})
        if student == None:
            search_form.student_id.data = ''
            flash("ERROR, The student doesn't exist")
        else:
            context['student'] = student


    if update_form.validate_on_submit():
        student_id = update_form.student_id.data
        student = db.db.students.find_one({'student_id': student_id})
        if update_form.first_name.data :
            db.db.students.update_one({'student_id': student_id},{'$set':{ 'first_name' : update_form.first_name.data.upper()}})
            update_form.first_name.data=''
            flag = True      
        if update_form.last_name.data:
            db.db.students.update_one({'student_id': student_id},{'$set':{ 'last_name' : update_form.last_name.data.upper()}})
            update_form.last_name.data = ''
            flag = True
        if update_form.group.data:
            db.db.students.update_one({'student_id': student_id},{'$set':{ 'group' : update_form.group.data}})
            update_form.group.data = ''
            flag = True
        if update_form.student_email.data:
            db.db.students.update_one({'student_id': student_id},{'$set':{ 'email' : update_form.student_email.data}})
            update_form.student_email.data = ''
            flag = True
        
        student = db.db.students.find_one({'student_id': student_id})
        context['student'] = student
    
    
    if flag:
        flash('Student Update success!')
        search_form.student_id.data = ''
        update_form.student_id.data = ''
        flag = False
    
    return render_template('search_student.html', **context)


@app.route('/delete/<student_id>', methods=['GET','POST'])
def delete(student_id):
    db.db.students.delete_one({'student_id': student_id})
    flash('Student deleted success!')
    return redirect('/')


if __name__ == '__main__':
    app.run(port=8000)