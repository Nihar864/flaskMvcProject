from base import db


class LoginDao:

    def add_user(self, login_vo):
        db.session.add(login_vo)
        db.session.commit()
