from base import db


class RegisterVo(db.Model):
    __tablename__ = 'register'
    id = db.Column("user_id", db.Integer, primary_key=True, autoincrement=True)
    fn = db.Column("user_fn", db.String(255), nullable=False)
    ln = db.Column("user_ln", db.String(255), nullable=False)
    un = db.Column("user_un", db.String(255), unique=True, nullable=False)
    pwd = db.Column("user_pwd", db.String(255), unique=True, nullable=False)

    def as_dict(self):
        return {
            'id': self.id,
            'fn': self.fn,
            'ln': self.ln,
            'un': self.un,
            'pwd': self.pwd
        }


db.create_all()
