class ProductDTO:

    def __init__(self, product_name: str, product_description: str,
                 product_price: int,
                 product_stock: int, product_category_id: int,
                 product_subcategory_id, product_img: str):
        self.product_name: [str] = product_name
        self.product_description: [str] = product_description
        self.product_price: [int] = product_price
        self.product_stock: [int] = product_stock
        self.product_category_id: [int] = product_category_id
        self.product_subcategory_id: [int] = product_subcategory_id
        self.product_img: [str] = product_img

    def validate(self):
        if not self.product_category_id:
            raise ValueError("Product category Name cannot be empty")
        elif not self.product_subcategory_id:
            raise ValueError("Product subcategory Name cannot be empty")
        elif not self.product_name:
            raise ValueError("Product name cannot be empty")
        elif not self.product_description:
            raise ValueError("Product description cannot be empty")
        elif not self.product_price:
            raise ValueError("Product price cannot be empty")
        elif not self.product_stock:
            raise ValueError("Product stock cannot be empty")
        return self
