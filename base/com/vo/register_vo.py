from base import db


class RegisterVo(db.Model):
    __tablename__ = 'register_table'
    user_id = db.Column(db.Integer, primary_key=True,
                        autoincrement=True)
    user_login_id = db.Column(db.Integer, db.ForeignKey(
        'login_table.login_id', ondelete='CASCADE', onupdate='CASCADE'),
                              nullable=False)
    user_firstname = db.Column(db.String(255), nullable=False)
    user_lastname = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    user_gender = db.Column(db.String(255), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.String(150), nullable=False)
    modified_on = db.Column(db.String(150), nullable=False)

    def as_dict(self):
        return {
            'user_id': self.user_id,
            'user_firstname': self.user_firstname,
            'user_lastname': self.user_lastname,
            'user_email': self.user_email,
            'user_gender': self.user_gender
        }


db.create_all()
