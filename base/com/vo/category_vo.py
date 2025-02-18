from base import db


class CategoryVo(db.Model):
    __tablename__ = 'category_table'
    Category_id = db.Column(db.Integer, primary_key=True,
                            unique=True)
    Category_name = db.Column(db.String(80), unique=True, nullable=False)
    Category_description = db.Column(db.String(150), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.String(150), nullable=False)
    modified_on = db.Column(db.String(150), nullable=False)

    def _as_dict(self):
        return {    
            "Category_name": self.Category_name,
            "Category_description": self.Category_description
        }


db.create_all()
