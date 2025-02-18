from typing import Optional


class AddSubcategoryDTO:
    def __init__(self, name: str, description: str, category_id: int):
        self.subcategory_name: [str] = name
        self.subcategory_description: [str] = description
        self.subcategory_category_id: [int] = category_id

    def validate(self):
        if not self.subcategory_name:
            raise ValueError('Subcategory name is required')
        elif not self.subcategory_name.replace(" ", "").isalpha():
            raise ValueError(
                "Subcategory name must contain only alphabetic characters ("
                "a-z).")

        if not self.subcategory_description:
            raise ValueError('Subcategory description is required')

        if not self.subcategory_category_id:
            raise ValueError('Category is required')

        return self


class UpdateSubcategoryDTO:
    def __init__(self, name: Optional[str], description: Optional[str],
                 category_id: int):
        self.subcategory_name: Optional[str] = name
        self.subcategory_description: Optional[str] = description
        self.subcategory_category_id = int(category_id)

    def validate(self):
        if not self.subcategory_name:
            raise ValueError('Subcategory name is required')
        elif not self.subcategory_name.replace(" ", "").isalpha():
            raise ValueError(
                "Subcategory name must contain only alphabetic characters ("
                "a-z).")

        if not self.subcategory_description:
            raise ValueError('Subcategory description is required')

        if not self.subcategory_category_id:
            raise ValueError('Category is required')

        return self
