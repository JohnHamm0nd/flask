from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import *
import os

app = Flask(__name__)

#DB 설정
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///todo'

# heroku 서버용 설정
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)
migrate = Migrate(app,db)

@app.route('/')
def index():
    todos = Todo.query.order_by(Todo.deadline.asc())
    return render_template('index.html', todos=todos)
    
# @app.route('/todo/new')
# def new():
#     return render_template('new.html')
    
# @app.route('/todo/create', methods=['POST'])
# def create():
#     # 사용자가 입력한 데이터 가져오기
#     todo = request.form['todo']
#     deadline = request.form.get('deadline')
#     # 가져온 데이터로 Todo 만들기
#     new_todo = Todo(todo=todo,deadline=deadline)
#     # Todo DB에 저장
#     db.session.add(new_todo)
#     db.session.commit()
#     # 페이지 이동
#     return redirect('/')
       
@app.route('/todos/create', methods=['POST', 'GET'])
def todo():
    if request.method == "POST":
        # 데이터를 저장하는 로직
        todo = Todo(request.form['todo'], request.form['deadline'])
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('new.html')
    

@app.route('/todos/<int:id>/delete')
def delete(id):
    # 몇번글을 삭제할지 알아낸다
    todo = Todo.query.get(id)
    # 글을 삭제한다
    db.session.delete(todo)
    # 상태를 저장한다.
    db.session.commit()
    # 어디로 보낼지 url 설정한다.
    return redirect('/')

# @app.route('/todos/<int:id>/edit')
# def edit(id):
#     todo = Todo.query.get(id)
#     return render_template('edit.html', todo=todo)

# @app.route('/todos/<int:id>/update', methods=["POST"])
# def update(id):
#     # 변경한 데이터를 가져와서 DB에 반영
#     todo = Todo.query.get(id)
#     todo.todo = request.form['todo']
#     todo.deadline = request.form['deadline']
#     db.session.commit()
#     return redirect('/')


@app.route('/todos/<int:id>/upgrade', methods=['POST', 'GET'] )
def upgrade(id):
    todo = Todo.query.get(id)
    if request.method == 'POST':
        # 게시물을 실제로 업데이트 하는 로직
        todo.todo = request.form['todo']
        todo.deadline = request.form['deadline']
        # DB에 반영
        db.session.commit()
        # 어디로 보낼지 결정
        return redirect('/')
    # 수정할 수 있는 폼을 리턴
    return render_template('edit.html', todo=todo)