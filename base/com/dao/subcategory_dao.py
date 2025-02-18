from base import db
from base.com.vo.category_vo import CategoryVo
from base.com.vo.subcategory_vo import SubcategoryVo


class SubcategoryDao:

    def add_subcategory(self, subcategory_vo):
        db.session.add(subcategory_vo)
        db.session.commit()

    def view_subcategory(self):
        subcategory_vo_lst = db.session.query(CategoryVo, SubcategoryVo).join(
            SubcategoryVo,
            CategoryVo.Category_id == SubcategoryVo.Subcategory_category_id
        ).filter(SubcategoryVo.is_deleted == False,
                 CategoryVo.is_deleted == False).all()
        return subcategory_vo_lst

    def edit_subcategory(self, subcategory_vo):
        subcategory_vo_lst = SubcategoryVo.query.filter_by(
            Subcategory_id=subcategory_vo.Subcategory_id).first()
        return subcategory_vo_lst

    def update_subcategory(self, subcategory_vo):
        db.session.merge(subcategory_vo)
        db.session.commit()
