from flask import render_template, request, redirect, flash
from marshmallow import ValidationError as MarshmallowValidationError
from base import app
from base.com.dto.category_dto import CategoryDTO
from base.com.service.category_service import CategoryService
from base.utiles.custom_exception import DataValidationError
from base.utiles.logger import get_logger

logger = get_logger()
category_service = CategoryService()


@app.route('/')
def home_page():
    return render_template("homePage.html")


@app.route('/load_category')
def load_category():
    logger.info("Load Category")
    return render_template("Category/addCategory.html")


@app.route('/add_category', methods=['GET', 'POST'])
def add_category():
    data = {
        'Category_name': request.form.get('category_name').strip() or None,
        'Category_description': request.form.get('category_description').strip() or None
    }
    category_schema = CategoryDTO()
    try:

        validated_data = category_schema.load(data)
        print(validated_data)
        category_service.add_category_service(validated_data)
        return redirect("/view_category")

    except MarshmallowValidationError as err:
        logger.exception(err.messages)
        flash("Field can Not be empty", "danger")
        return render_template("Category/addCategory.html")

    except DataValidationError as e:
        print(e)
        flash("Field can Not be empty", "danger")
        return render_template("Category/addCategory.html")

    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        flash("An unexpected error occurred. Please try again later.", "danger")
        return render_template("Category/addCategory.html")


@app.route('/view_category', methods=['GET', 'POST'])
def view_category():
    category_vo_lst = category_service.view_category_service()
    return render_template("Category/viewCategory.html",
                           category_vo_lst=category_vo_lst)


@app.route('/delete_category', methods=['GET', 'POST'])
def delete_category():
    category_id = request.args.get('category_id')
    category_service.delete_category_service(category_id)
    return redirect("/view_category")


@app.route('/edit_category', methods=['GET', 'POST'])
def edit_category():
    category_id = request.args.get('category_id')
    category_vo_lst = category_service.edit_category_service(category_id)
    return render_template("Category/updateCategory.html",
                           category_vo=category_vo_lst)


@app.route('/update_category', methods=['GET', 'POST'])
def update_category():
    category_id = request.form.get('category_id')
    data = {
        'Category_name': request.form.get('category_name').strip() or None,
        'Category_description': request.form.get('category_description').strip() or None
    }

    category_schema = CategoryDTO() 

    try:
        validated_data = category_schema.load(data)
        category_service.update_category_service(category_id, validated_data)
        return redirect("/view_category")

    except MarshmallowValidationError as err:
        logger.exception(err.messages)
        flash("Field can Not be empty", "danger")
        return redirect(f"/edit_category?category_id={category_id}")

    except DataValidationError as e:
        flash(str(e), "danger")
        return redirect(f"/edit_category?category_id={category_id}")

    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        flash("An unexpected error occurred. Please try again later.", "danger")
        return redirect(f"/edit_category?category_id={category_id}")
