from sqlalchemy import Table, Column, Integer, ForeignKey
from proj_extensions import db

blog_post_and_blog_tag_association_table = \
    Table('blog_post_and_blog_tag_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('blog_post.id')),
          Column('right_id', Integer, ForeignKey('blog_tag.id'))
          )

home_content_products_of_section_1_association_table = \
    Table('home_content_products_of_section_1_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product.id'))
          )

home_content_products_of_section_2_association_table = \
    Table('home_content_products_of_section_2_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product.id'))
          )

home_content_products_of_section_3_association_table = \
    Table('home_content_products_of_section_3_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product.id'))
          )

home_content_products_of_section_4_association_table = \
    Table('home_content_products_of_section_4_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product.id'))
          )

home_content_products_of_section_5_association_table = \
    Table('home_content_products_of_section_5_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product.id'))
          )

home_content_products_of_section_6_association_table = \
    Table('home_content_products_of_section_6_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product.id'))
          )

home_content_more_categories_section_category_1_association_table = \
    Table('home_content_more_categories_section_category_1_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_category.id'))
          )

home_content_more_categories_section_category_2_association_table = \
    Table('home_content_more_categories_section_category_2_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_category.id'))
          )

home_content_more_categories_section_category_3_association_table = \
    Table('home_content_more_categories_section_category_3_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_category.id'))
          )

home_content_more_categories_section_category_4_association_table = \
    Table('home_content_more_categories_section_category_4_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_category.id'))
          )

home_content_more_categories_section_category_5_association_table = \
    Table('home_content_more_categories_section_category_5_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_category.id'))
          )

home_content_more_categories_section_category_6_association_table = \
    Table('home_content_more_categories_section_category_6_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_category.id'))
          )

home_content_more_categories_section_category_1_subcategories_association_table = \
    Table('home_content_more_categories_section_cat_1_subcats_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_subcategory.id'))
          )

home_content_more_categories_section_category_2_subcategories_association_table = \
    Table('home_content_more_categories_section_cat_2_subcats_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_subcategory.id'))
          )

home_content_more_categories_section_category_3_subcategories_association_table = \
    Table('home_content_more_categories_section_cat_3_subcats_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_subcategory.id'))
          )

home_content_more_categories_section_category_4_subcategories_association_table = \
    Table('home_content_more_categories_section_cat_4_subcats_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_subcategory.id'))
          )

home_content_more_categories_section_category_5_subcategories_association_table = \
    Table('home_content_more_categories_section_cat_5_subcats_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_subcategory.id'))
          )

home_content_more_categories_section_category_6_subcategories_association_table = \
    Table('home_content_more_categories_section_cat_6_subcats_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('product_subcategory.id'))
          )

home_content_blog_section_1_post_1_association_table = \
    Table('home_content_blog_section_1_post_1_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('blog_post.id'))
          )

home_content_blog_section_1_post_2_association_table = \
    Table('home_content_blog_section_1_post_2_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('blog_post.id'))
          )

home_content_blog_section_2_post_1_association_table = \
    Table('home_content_blog_section_2_post_1_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('blog_post.id'))
          )

home_content_blog_section_2_post_2_association_table = \
    Table('home_content_blog_section_2_post_2_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('blog_post.id'))
          )

home_content_blog_section_3_post_1_association_table = \
    Table('home_content_blog_section_3_post_1_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('blog_post.id'))
          )

home_content_blog_section_3_post_2_association_table = \
    Table('home_content_blog_section_3_post_2_association',
          db.Model.metadata,
          Column('left_id', Integer, ForeignKey('home_content.id')),
          Column('right_id', Integer, ForeignKey('blog_post.id'))
          )
