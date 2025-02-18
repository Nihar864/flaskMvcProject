from base import db


class ProductVo(db.Model):
    __tablename__ = 'product_table'
    Product_id = db.Column(db.Integer, primary_key=True)
    Product_name = db.Column(db.String(50), nullable=False)
    Product_description = db.Column(db.String(500), nullable=False)
    Product_price = db.Column(db.Float, nullable=False)
    Product_stock = db.Column(db.Integer, nullable=False)
    Product_image_name = db.Column(db.String(255), nullable=False)
    Product_image_path = db.Column(db.String(255), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.String(150), nullable=False)
    modified_on = db.Column(db.String(150), nullable=False)
    Product_category_id = db.Column(db.Integer,
                                    db.ForeignKey('category_table.Category_id',
                                                  ondelete='CASCADE',
                                                  onupdate='CASCADE'),
                                    nullable=False)
    Product_subcategory_id = db.Column(db.Integer,
                                       db.ForeignKey(
                                           'subcategory_table.Subcategory_id',
                                           ondelete='CASCADE',
                                           onupdate='CASCADE'),
                                       nullable=False)

    def _as_dict(self):
        return {
            'Product_name': self.Product_name,
            'Product_price': self.Product_price,
            'Product_stock': self.Product_stock,
            'Product_image': self.Product_image,
            'Product_category_id': self.Product_category_id,
            'Product_subcategory_id': self.Product_subcategory_id

        }


db.create_all()
