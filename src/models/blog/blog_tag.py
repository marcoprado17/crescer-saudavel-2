from markupsafe import Markup
from sqlalchemy.orm import relationship
from models.associations import blog_post_and_blog_tag_association_table
from models.base import BaseModel
from models.blog.blog_post import BlogPost
from proj_extensions import db
from r import R


class BlogTag(BaseModel):
    __tablename__ = "blog_tag"

    active = db.Column(db.Boolean, default=False, nullable=False)
    name = db.Column(db.String(R.dimen.blog_tag_max_length), nullable=False)
    blog_posts = \
        relationship("BlogPost",
                     order_by=BlogPost.date,
                     secondary=blog_post_and_blog_tag_association_table,
                     back_populates="tags")

    def __repr__(self):
        return Markup("<b><searchable>#%s</searchable></b> | <searchable>%s</searchable>" % (self.id, self.name))
