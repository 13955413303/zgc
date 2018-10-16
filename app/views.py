from flask import render_template, Blueprint, request

from app.models import books, db

blue =Blueprint('blue',__name__)

@blue.route('/')
def get():
    return render_template('base.html')



@blue.route('/index/',methods=['POST','GET','DELETE'])
def index():
    print(request.method)
    if request.method == 'get':
        pass
    if request.method == 'POST':

        flag = request.form.get('flag')
        print(flag)
        if flag == '1':
            name=request.form.get('name')
            print(name)
            auth=request.form.get('auth')
            print(auth)
            book=books(name=name,auth=auth)
            print(book)
            db.session.add(book)
            db.session.commit()
        elif flag=='2':
            id = request.form.get('id')
            book = books.query.get(id)
            if book:
                db.session.delete(book)
                db.session.commit()
            else:
                return '编号不存在'
        elif flag == '3':
            id = request.form.get('id')
            book = books.query.get(id)
            name=request.form.get('name')
            book.name=name
            auth=request.form.get('auth')
            book.auth=auth

            db.session.add(book)
            db.session.commit()
        else :
            id = request.form.get('id')
            book = books.query.get(id)
            return render_template('find.html',contents=book)

    page = request.args.get('page', 1)

    pagination = books.query.paginate(int(page), 5, False)

    return render_template('index.html', paginations=pagination)


@blue.route('/add/')
def add():
    return render_template('add.html')

@blue.route('/delete/')
def delete():
    return render_template('delete.html')

@blue.route('/change/')
def change():
    return render_template('change.html')

@blue.route('/find/')
def find():
    return render_template('find.html')
