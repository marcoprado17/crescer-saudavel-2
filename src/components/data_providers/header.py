from flask_login import current_user
from sqlalchemy import desc

from models.content.header import HeaderContent
from models.product.product_category import ProductCategory


class HeaderDataProvider(object):
    # noinspection PyMethodMayBeStatic
    def get_data(self):
        product_categories = ProductCategory.query.filter_by(active=True).order_by(desc(ProductCategory.priority)).all()

        return dict(
            header_content=HeaderContent.get(),
            user=current_user,
            product_categories=product_categories
        )

header_data_provider = HeaderDataProvider()
