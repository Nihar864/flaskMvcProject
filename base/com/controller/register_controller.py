from flask import render_template, redirect, request

from base import app
from base.com.dao.register_dao import RegisterDao
from base.com.vo.register_vo import RegisterVo


# @app.route('/')
# def home_page():
#     return render_template("login.html")


@app.route('/load_register')
def load_register():
    return render_template("Login/register.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    firt_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    user_name = request.form.get('userName')
    password = request.form.get('password')

    # print(firt_name, last_name, user_name, password)
    register_vo = RegisterVo()
    register_dao = RegisterDao()

    if firt_name and last_name and user_name and password:
        register_vo.fn = firt_name
        register_vo.ln = last_name
        register_vo.un = user_name
        register_vo.pwd = password
        register_dao.insert_data(register_vo)
    else:
        print("Error: Please fill in all required fields.")

    return redirect("/")
