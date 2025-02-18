from base.com.dao.category_dao import CategoryDao
from base.com.vo.category_vo import CategoryVo
from base.utiles.custom_exception import DataValidationError, ValidationError
from base.utiles.logger import get_logger
from base.utiles.timestamp import timestamp
from marshmallow import ValidationError as MarshmallowValidationError


class CategoryService:

    def __init__(self):
        self.category_dao = CategoryDao()
        self.logger = get_logger()

    def add_category_service(self, validated_data):
        created_on = timestamp()
        category_vo = CategoryVo()
        try:
            category_vo.Category_name = validated_data['Category_name']
            category_vo.Category_description = validated_data[
                'Category_description']
            category_vo.created_on = created_on
            category_vo.modified_on = created_on
            self.category_dao.add_category(category_vo)
            self.logger.info(f"Add Category -> {category_vo}")

        except MarshmallowValidationError as e:
            self.logger.error(f"Validation error: {e.messages}")
            raise DataValidationError(f"Validation error: {e.messages}") from e

        except Exception as e:
            self.logger.exception(f"Error in add_category_service: {e}")
            raise DataValidationError(f"Error adding category: {e}") from e

    def view_category_service(self):
        category_vo_lst = self.category_dao.view_category() 
        self.logger.info("View Category")
        return category_vo_lst

    def delete_category_service(self, category_id):
        category_vo = CategoryVo()
        is_deleted = True
        modified_on = timestamp()
        category_vo.Category_id = category_id
        category_vo.is_deleted = is_deleted
        category_vo.modified_on = modified_on
        self.category_dao.update_category(category_vo)
        self.logger.info(f"Soft Delete Category Id -> {category_id}")

    def edit_category_service(self, category_id):
        category_vo_lst = self.category_dao.edit_category(category_id)
        return category_vo_lst

    def update_category_service(self, category_id, validated_data):
        modified_on = timestamp()
        category_vo = CategoryVo()

        try:
            category_vo.Category_id = category_id
            category_vo.Category_name = validated_data['Category_name']  
            category_vo.Category_description = validated_data['Category_description']
            category_vo.modified_on = modified_on
            self.category_dao.update_category(category_vo)
            self.logger.info(
                f"Update Category Id ->{category_id} -> {validated_data}")
        except MarshmallowValidationError as e:
            self.logger.error(f"Validation error: {e.messages}")
            raise DataValidationError(f"Validation error: {e.messages}") from e
        except Exception as e:
            self.logger.exception(
                f"Error in update_category_service: {e}")
            raise DataValidationError(
                "Error updating category, please try again.") from e
