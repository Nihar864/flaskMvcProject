import os

from base.com.dao.product_dao import ProductDao
from base.com.vo.product_vo import ProductVo
from base.com.vo.subcategory_vo import SubcategoryVo
from base.utiles.logger import get_logger
from base.utiles.timestamp import timestamp


class ProductService:

    def __init__(self):
        self.product_dao = ProductDao()
        self.logger = get_logger()
        self.image_directory = os.path.join("base", "static", "product_images")

    def ajax_service(self, product_category_id):
        subcategory_vo = SubcategoryVo()
        subcategory_vo.Subcategory_category_id = product_category_id
        subcategory_vo_lst = self.product_dao.ajax_product(subcategory_vo)
        return subcategory_vo_lst

    def add_product_service(self, dto):
        created_on = timestamp()
        product_vo = ProductVo()
        image_name = dto.product_img.filename

        image_path = os.path.join(self.image_directory, image_name)
        dto.product_img.save(image_path)

        product_vo.Product_name = dto.product_name
        product_vo.Product_description = dto.product_description
        product_vo.Product_price = dto.product_price
        product_vo.Product_stock = dto.product_stock
        product_vo.Product_image_name = image_name
        product_vo.Product_image_path = image_path
        product_vo.Product_category_id = dto.product_category_id
        product_vo.Product_subcategory_id = dto.product_subcategory_id
        product_vo.created_on = created_on
        product_vo.modified_on = created_on
        self.product_dao.add_product(product_vo)
        self.logger.info("Add Product")

    def view_product_service(self):
        product_vo_lst = self.product_dao.view_product()
        return product_vo_lst

    def delete_product_service(self, product_id):
        product_vo = ProductVo()
        is_deleted = True
        modified_on = timestamp()
        product_vo.Product_id = product_id
        product_vo.is_deleted = is_deleted
        product_vo.modified_on = modified_on
        self.product_dao.update_product(product_vo)

    def edit_product_service(self, product_id):
        product_vo_lst, category_vo_lst = self.product_dao.edit_product(
            product_id)
        return product_vo_lst, category_vo_lst

    def update_product_service(self, product_id, product_dto):
        modified_on = timestamp()
        product_vo = ProductVo()

        image_name = product_dto.product_img.filename
        if image_name == '':
            print("")
        else:
            image_name = product_dto.product_img.filename
            image_path = os.path.join(self.image_directory, image_name)
            product_dto.product_img.save(image_path)
            product_vo.Product_image_name = image_name
            product_vo.Product_image_path = image_path

        product_vo.Product_id = product_id
        product_vo.Product_name = product_dto.product_name
        product_vo.Product_description = product_dto.product_description
        product_vo.Product_price = product_dto.product_price
        product_vo.Product_stock = product_dto.product_stock
        product_vo.Product_category_id = product_dto.product_category_id
        product_vo.Product_subcategory_id = product_dto.product_subcategory_id
        product_vo.modified_on = modified_on

        self.product_dao.update_product(product_vo)
        self.logger.info(f"Updated Product with ID: {product_id}")