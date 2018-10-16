from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class books(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(16))
    auth = db.Column(db.String(16))

    def __str__(self) -> str:
        return 'name:%s,auth:%s'%(self.name,self.auth)


