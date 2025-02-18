from base import db
from base.com.vo.category_vo import CategoryVo
from base.com.vo.product_vo import ProductVo
from base.com.vo.subcategory_vo import SubcategoryVo


class ProductDao:

    def add_product(self, product_vo):
        db.session.add(product_vo)
        db.session.commit()

    def ajax_product(self, subcategory_vo):
        subcategory_vo_lst = SubcategoryVo.query.filter_by(
            Subcategory_category_id=subcategory_vo.Subcategory_category_id
        ).filter(SubcategoryVo.is_deleted == False).all()
        return subcategory_vo_lst

    def view_product(self):
        product_vo_lst = (db.session.query(ProductVo, SubcategoryVo, CategoryVo
                                           ).join(SubcategoryVo,
                                                  SubcategoryVo.Subcategory_id == ProductVo.Product_subcategory_id
                                                  )).join(
            CategoryVo, CategoryVo.Category_id ==
                        ProductVo.Product_category_id).filter(
            ProductVo.is_deleted == False).all()
        return product_vo_lst

    def edit_product(self, product_id):
        product_vo_lst = db.session.query(ProductVo).filter_by(
            Product_id=product_id).first()
        category_vo_lst = db.session.query(CategoryVo).all()
        return product_vo_lst, category_vo_lst

    def update_product(self, product_vo):
        db.session.merge(product_vo)
        db.session.commit()
