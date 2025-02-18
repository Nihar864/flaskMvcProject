# from base import db
#
#
# class LoginVo(db.Model):
#     __tablename__ = 'log_in'
#     id = db.Column("user_id", db.Integer, autoincrement=True)
#     un = db.Column("user_un", db.String(255), unique=True, nullable=False)
#     pwd = db.Column("user_pwd", db.String(255), unique=True, nullable=False)
#
#     def as_dict(self):
#         return {
#             'id': self.id,
#             'un': self.un,
#             'pwd': self.pwd
#         }
#
# db.create_all()
