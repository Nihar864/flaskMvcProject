from flask import render_template, request, redirect, flash

from base import app
from base.com.dto.subcategory_dto import AddSubcategoryDTO, \
    UpdateSubcategoryDTO
from base.com.service.category_service import CategoryService
from base.com.service.subcategory_service import SubcategoryService
from base.utiles.custom_exception import DataValidationError
from base.utiles.logger import get_logger

logger = get_logger()
category_service = CategoryService()
subcategory_service = SubcategoryService()


@app.route('/load_subcategory')
def load_subcategory():
    category_vo_lst = category_service.view_category_service()
    logger.info("Load Subcategory")
    return render_template("Subcategory/addSubcategory.html",
                           category_vo_lst=category_vo_lst)


@app.route('/add_subcategory', methods=['GET', 'POST'])
def add_subcategory():
    subcategory_name = request.form.get('Subcategory_name')
    subcategory_description = request.form.get('Subcategory_description')
    subcategory_category_id = request.form.get('Subcategory_category_id')
    subcategory_dto = AddSubcategoryDTO(subcategory_name,
                                        subcategory_description,
                                        subcategory_category_id)
    try:
        dto = subcategory_dto.validate()
        subcategory_service.add_subcategory_service(dto)
        return redirect('/view_subcategory')

    except ValueError as e:
        flash(str(e), "danger")
        return redirect('/load_subcategory')
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        flash("An unexpected error occurred. Please try again later.",
              "danger")
        return redirect('/load_subcategory')


@app.route('/view_subcategory', methods=['GET', 'POST'])
def view_subcategory():
    subcategory_vo_lst = subcategory_service.view_subcategory_service()
    return render_template("Subcategory/viewsubSubcategory.html",
                           subcategory_vo_lst=subcategory_vo_lst)


@app.route('/delete_subcategory', methods=['GET', 'POST'])
def delete_subcategory():
    subcategory_id = request.args.get('subcategory_id')
    subcategory_service.delete_subcategory_service(subcategory_id)
    return redirect('/view_subcategory')


@app.route('/edit_subcategory', methods=['GET', 'POST'])
def edit_subcategory():
    subcategory_id = request.args.get('subcategory_id')
    subcategory_vo_lst, category_vo_lst = subcategory_service.edit_subcategory_service(
        subcategory_id)
    return render_template("Subcategory/updateSubcategory.html",
                           subcategory_vo_lst=subcategory_vo_lst,
                           category_vo_lst=category_vo_lst)


@app.route('/update_subcategory', methods=['GET', 'POST'])
def update_subcategory():
    subcategory_id = request.form.get('subcategory_id')
    subcategory_name = request.form.get('subcategory_name')
    subcategory_description = request.form.get('subcategory_description')
    subcategory_category_id = request.form.get('subcategory_category_id')

    subcategory_dto = UpdateSubcategoryDTO(subcategory_name,
                                           subcategory_description,
                                           subcategory_category_id)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>", subcategory_dto)

    try:
        dto = subcategory_dto.validate()
        subcategory_service.update_subcategory_service(subcategory_id, dto)
        return redirect('/view_subcategory')

    except ValueError as e:
        print(e, "<<<<<<<<<<<<<<<")
        flash(str(e), "danger")
        return redirect(f'/edit_subcategory?subcategory_id={subcategory_id}')

    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        flash("An unexpected error occurred. Please try again later.",
              "danger")
        return redirect(f'/edit_subcategory?subcategory_id={subcategory_id}')
