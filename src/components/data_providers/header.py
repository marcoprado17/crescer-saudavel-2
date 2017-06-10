from flask_login import current_user
from sqlalchemy import desc

from models.content.header import HeaderContent
from models.product.product_category import ProductCategory


class HeaderDataProvider(object):
    # noinspection PyMethodMayBeStatic
    def get_data(self):
        product_categories = ProductCategory.query.filter_by(active=True).order_by(desc(ProductCategory.priority)).all()
        product_categories_by_4_grouped = []
        for i in [x for x in range(0, len(product_categories)) if x % 4 == 0]:
            product_categories_row = [product_categories[i]]
            if i+1 < len(product_categories):
                product_categories_row.append(product_categories[i+1])
            if i+2 < len(product_categories):
                product_categories_row.append(product_categories[i+2])
            if i+3 < len(product_categories):
                product_categories_row.append(product_categories[i+3])
            product_categories_by_4_grouped.append(product_categories_row)

        return dict(
            header_content=HeaderContent.get(),
            user=current_user,
            product_categories=product_categories,
            product_categories_by_4_grouped=product_categories_by_4_grouped
        )

header_data_provider = HeaderDataProvider()
