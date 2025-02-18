from base.com.dao.category_dao import CategoryDao
from base.com.dao.subcategory_dao import SubcategoryDao
from base.com.vo.subcategory_vo import SubcategoryVo
from base.utiles.custom_exception import DataValidationError
from base.utiles.logger import get_logger
from base.utiles.timestamp import timestamp


class SubcategoryService:

    def __init__(self):
        self.subcategory_dao = SubcategoryDao()
        self.category_dao = CategoryDao()
        self.logger = get_logger()

    def add_subcategory_service(self, subcategory_dto):
        created_on = timestamp()
        subcategory_vo = SubcategoryVo()

        try:
            subcategory_vo.Subcategory_name = subcategory_dto.subcategory_name
            subcategory_vo.Subcategory_description = subcategory_dto.subcategory_description
            subcategory_vo.Subcategory_category_id = subcategory_dto.subcategory_category_id
            subcategory_vo.created_on = created_on
            subcategory_vo.modified_on = created_on
            self.subcategory_dao.add_subcategory(subcategory_vo)
            self.logger.info(f"Add Category -> {subcategory_dto}")

        except Exception as e:
            self.logger.exception(
                f"Error in add_subcategory_service: {e}")
            raise DataValidationError(
                "Error adding subcategory. Please try again.") from e

    def view_subcategory_service(self):
        subcategory_vo_lst = self.subcategory_dao.view_subcategory()
        self.logger.info("View Subcategory")
        return subcategory_vo_lst

    def delete_subcategory_service(self, subcategory_id):
        is_deleted = True 
        modified_on = timestamp()
        subcategory_vo = SubcategoryVo()
        subcategory_vo.Subcategory_id = subcategory_id
        subcategory_vo.is_deleted = is_deleted
        subcategory_vo.modified_on = modified_on
        self.subcategory_dao.update_subcategory(subcategory_vo)
        self.logger.info(f"Soft delete Subcategory Id -> {subcategory_id}")

    def edit_subcategory_service(self, subcategory_id):
        subcategory_vo = SubcategoryVo()
        subcategory_vo.Subcategory_id = subcategory_id
        subcategory_vo_lst = self.subcategory_dao.edit_subcategory(
            subcategory_vo)
        category_vo_lst = self.category_dao.view_category()
        return subcategory_vo_lst, category_vo_lst

    def update_subcategory_service(self, subcategory_id, subcategory_dto):
        modified_on = timestamp()
        subcategory_vo = SubcategoryVo()
        try:
            subcategory_vo.Subcategory_id = subcategory_id
            subcategory_vo.Subcategory_name = subcategory_dto.subcategory_name
            subcategory_vo.Subcategory_description = (
                subcategory_dto.subcategory_description)
            subcategory_vo.Subcategory_category_id = subcategory_dto.subcategory_category_id
            subcategory_vo.modified_on = modified_on
            self.subcategory_dao.update_subcategory(subcategory_vo)
            self.logger.info(
                f"Update Subcategory Id ->{subcategory_id} ->"
                f" {subcategory_dto}")
        except Exception as e:
            self.logger.exception(
                f"Error in add_subcategory_service: {e}")
            raise DataValidationError(
                "Error adding subcategory. Please try again.") from e