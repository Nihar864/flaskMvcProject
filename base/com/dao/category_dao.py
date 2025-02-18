from base import db
from base.com.vo.category_vo import CategoryVo


class CategoryDao:

    def add_category(self, category_vo):
        db.session.add(category_vo)
        db.session.commit()

    def view_category(self):
        category_vo_lst = CategoryVo.query.filter(
            CategoryVo.is_deleted == False).all()
        return category_vo_lst

    def edit_category(self, category_id):
        category_vo_lst = CategoryVo.query.filter_by(
            Category_id=category_id).first()
        return category_vo_lst

    def update_category(self, category_vo):
        db.session.merge(category_vo)
        db.session.commit()
