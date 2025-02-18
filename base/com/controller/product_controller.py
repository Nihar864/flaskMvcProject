from flask import render_template, request, redirect, jsonify, flash, make_response

from base import app
from base.com.dto.product_dto import ProductDTO
from base.com.service.category_service import CategoryService
from base.com.service.product_service import ProductService
from base.utiles.logger import get_logger

logger = get_logger()
category_service = CategoryService()
product_service = ProductService()


@app.route('/load_product', methods=['GET', 'POST'])
def load_products():
    category_vo_lst = category_service.view_category_service()
    logger.info("Load Products")
    return render_template('Product/addproduct.html',
                           category_vo_lst=category_vo_lst)


@app.route('/ajax_subcategory_product', methods=['GET', 'POST'])
def ajax_subcategory_product():
    product_category_id = request.args.get('Product_category_id')

    subcategory_vo_lst = product_service.ajax_service(product_category_id)
    print(subcategory_vo_lst)

    return jsonify([i._as_dict() for i in subcategory_vo_lst])


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    product_name = request.form.get('Product_name')
    product_description = request.form.get('Product_description')
    product_price = request.form.get('Product_price')
    product_stock = request.form.get('Product_stock')
    product_category_id = request.form.get('Product_category_id')
    product_subcategory_id = request.form.get('Product_subcategory_id')
    product_img = request.files.get("Product_img")
    product_dto = ProductDTO(product_name, product_description,
                             product_price,
                             product_stock, product_category_id,
                             product_subcategory_id, product_img)

    try:
        dto = product_dto.validate()
        product_service.add_product_service(dto)
        return redirect('/view_product')

    except ValueError as e:
        flash(str(e), "danger")
        return redirect('/load_product')

    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        flash("An unexpected error occurred. Please try again later.",
              "danger")
        return redirect('/load_product')


@app.route('/view_product', methods=['GET', 'POST'])
def view_product():
    product_vo_lst = product_service.view_product_service()
    logger.info("view_product {}: ".format(product_vo_lst))

    return render_template('Product/viewproduct.html',
                           product_vo_lst=product_vo_lst)


@app.route('/delete_product', methods=['GET', 'POST'])
def delete_product():
    product_id = request.args.get('Product_id')
    product_service.delete_product_service(product_id)
    logger.info("Delete Product")
    return redirect('/view_product')


@app.route('/edit_product', methods=['GET', 'POST'])
def edit_product():
    product_id = request.args.get('Product_id')

    product_vo_lst, category_vo_lst = product_service.edit_product_service(
        product_id)

    return render_template(
        'Product/updateproduct.html',
        product_vo_lst=product_vo_lst,
        category_vo_lst=category_vo_lst)


@app.route("/update_product", methods=['GET', 'POST'])
def update_product():
    product_id = request.form.get('Product_id')
    product_name = request.form.get('Product_name')
    product_description = request.form.get('Product_description')
    product_price = request.form.get('Product_price')
    product_stock = request.form.get('Product_stock')
    product_category_id = request.form.get('Product_category_id')
    product_subcategory_id = request.form.get('Product_subcategory_id')
    product_img = request.files.get("Product_img")

    product_dto = ProductDTO(product_name, product_description,
                             product_price,
                             product_stock, product_category_id,
                             product_subcategory_id, product_img)

    try:
        dto = product_dto.validate()
        product_service.update_product_service(product_id, dto)
        return redirect('/view_product')


    except ValueError as e:
        flash(str(e), "danger")
        return redirect(f'/edit_product?Product_id={product_id}')

    except Exception as e:
        logger.exception(f"An unexpected error occurred during update: {e}")
        flash(
            "An unexpected error occurred during update. Please try again later.",
            "danger")
        return redirect(f'/edit_product?Product_id={product_id}')
