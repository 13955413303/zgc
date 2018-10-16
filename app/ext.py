from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_restful import Api
from flask_session import Session

from app.views import  blue
from app.models import db


def init_ext(app):
    app.register_blueprint(blueprint=blue)

    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/zgc'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app=app)

    migrate = Migrate()
    migrate.init_app(app = app,db = db)

    app.config['SECRET_KEY']='100'
    app.config['SESSION_TYPE']='redis'
    Session(app=app)

    Bootstrap(app=app)
    # api = Api()
    # api.add_resource(Base,'/')
    #
    # api.init_app(app=app)




