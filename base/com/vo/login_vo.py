from base import db


class LoginVo(db.Model):
    __tablename__ = 'login_table'
    login_id = db.Column(db.Integer, primary_key=True,
                         autoincrement=True)

    user_username = db.Column(db.String(255), unique=True, nullable=False)
    user_password = db.Column(db.String(255), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.String(150), nullable=False)
    modified_on = db.Column(db.String(150), nullable=False)

    def as_dict(self):
        return {
            'login_id': self.login_id,
            'user_username': self.user_username,
            'user_password': self.user_password
        }


db.create_all()
