from flask import render_template, request, redirect, flash
from base import app
from base.utiles.logger import get_logger

logger = get_logger()


@app.route('/register', methods=['GET', 'POST'])
def load_register():
    logger.info('Loading register page')
    return render_template('Login/register.html')


# @app.route('/register', methods=['GET', 'POST'])