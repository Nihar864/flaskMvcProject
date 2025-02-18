from flask import render_template, request, redirect, flash
from marshmallow import ValidationError as MarshmallowValidationError

from base import app
from base.com.dto.register_dto import RegisterDTO
from base.com.service.register_service import RegisterService
from base.utiles.custom_exception import DataValidationError
from base.utiles.logger import get_logger

logger = get_logger()
register_service = RegisterService()


@app.route('/load_register', methods=['GET', 'POST'])
def load_register():
    logger.info('Loading register page')
    return render_template('Login/register.html')


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    data = {
        'user_firstname': request.form.get('user_firstname').strip() or None,
        'user_lastname': request.form.get('user_lastname').strip() or None,
        'user_email': request.form.get('user_email').strip() or None,
        'user_gender': request.form.get('user_gender').strip() or None,
        'user_password': request.form.get('user_password').strip() or None,
        'user_username': request.form.get('user_username').strip() or None
    }
    user_schema = RegisterDTO()
    try:
        validated_data = user_schema.load(data)
        register_service.add_user_service(validated_data)
        return redirect('/')

    except MarshmallowValidationError as e:
        logger.exception(e.messages)
        flash("Field can Not be empty", 'danger')
        return render_template('Login/register.html')

    except DataValidationError as e:
        print(e)
        flash("Field can Not be empty", "danger")
        return render_template('Login/register.html')

    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        flash("An unexpected error occurred. Please try again later.",
              "danger")
        return render_template('Login/register.html')
