from base import db


class RegisterDao():

    def insert_data(self, register_vo):
        db.session.add(register_vo)
        db.session.commit()
