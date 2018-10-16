from flask import render_template, Blueprint, request, redirect, url_for

from app.models import books, db, user

blue =Blueprint('blue',__name__)

@blue.route('/')
def get():
    name = request.cookies.get('name','登录')
    return render_template('base.html',name=name)



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
            return render_template('find.html',contents=book,name=request.cookies.get('name','登录'))

    page = request.args.get('page', 1)

    pagination = books.query.paginate(int(page), 5, False)

    return render_template('index.html', paginations=pagination,name=request.cookies.get('name','登录'))


@blue.route('/add/')
def add():
    return render_template('add.html',name=request.cookies.get('name','登录'))

@blue.route('/delete/')
def delete():
    return render_template('delete.html',name=request.cookies.get('name','登录'))

@blue.route('/change/')
def change():
    return render_template('change.html',name=request.cookies.get('name','登录'))

@blue.route('/find/')
def find():
    return render_template('find.html',name=request.cookies.get('name','登录'))


@blue.route('/tologin/')
def tologin():
    return render_template('tologin.html',)


@blue.route('/login/' ,methods=['POST'])
def login():
    name = request.form.get('name')
    phone = request.form.get('phone')
    check1 = user.query.filter_by(phone=phone).first()
    print(check1)
    if check1:
        check2 = check1.name
        if name ==check2:
            response =redirect(url_for('blue.get'))
            response.set_cookie('name',name)
            return response
        else:
            return '信息输入有误'
    else:
        return '用户不存在'

@blue.route('/toregister/')
def toregister():
    return render_template('toregister.html',name=request.cookies.get('name','登录'))


@blue.route('/register/' ,methods=['POST'])
def register():
    name = request.form.get('name')
    phone = request.form.get('phone')
    check1 = user.query.filter_by(phone=phone).first()
    print(check1)
    if check1:
        return '已经注册过了'
    else:
        u = user(name=name,phone=phone)
        db.session.add(u)
        db.session.commit()
        return '注册成功'