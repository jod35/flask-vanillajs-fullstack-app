from flask import Blueprint,render_template,url_for,redirect,request
from ..models.students import Student


ui_bp=Blueprint('ui',__name__,template_folder='templates')

@ui_bp.route('/')
def hello():
    return render_template('index.html')


@ui_bp.route('/view')
def view_records():
    student=Student.query.order_by(Student.id.desc()).all()
    context={
        'students':student
    }
    return render_template('entries.html',**context)
    