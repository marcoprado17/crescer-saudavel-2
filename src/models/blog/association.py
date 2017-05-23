from sqlalchemy import Table, Column, Integer, ForeignKey
from proj_extensions import db


association_table = Table('blog_post_and_blog_tag_association', db.Model.metadata,
    Column('left_id', Integer, ForeignKey('blog_post.id')),
    Column('right_id', Integer, ForeignKey('blog_tag.id'))
)
