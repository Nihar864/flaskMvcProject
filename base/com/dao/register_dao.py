from base import db
from base.com.vo.login_vo import LoginVo


class RegisterDao:

    def add_user(self, register_vo):
        db.session.add(register_vo)
        db.session.commit()

    def view_user(self, user_username):
        login_lst = LoginVo.query.filter_by(
            user_username=user_username).first()
        return login_lst