from base import db


class SubcategoryVo(db.Model):
    __tablename__ = 'subcategory_table'
    Subcategory_id = db.Column(db.Integer, primary_key=True)
    Subcategory_name = db.Column(db.String(80), unique=True, nullable=False)
    Subcategory_description = db.Column(db.String(150), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.String(150), nullable=False)
    modified_on = db.Column(db.String(150), nullable=False)
    Subcategory_category_id = db.Column(db.Integer, db.ForeignKey(
        'category_table.Category_id', ondelete='CASCADE', onupdate='CASCADE'),
                                        nullable=False)

    def _as_dict(self):
        return {
            'Subcategory_id': self.Subcategory_id,
            'Subcategory_name': self.Subcategory_name,
            'Subcategory_description': self.Subcategory_description,
            'Subcategory_category_id': self.Subcategory_category_id
        }


db.create_all()
