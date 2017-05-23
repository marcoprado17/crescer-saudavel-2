from sqlalchemy.orm import relationship
from models.base import BaseModel
from models.blog.association import association_table
from models.blog.blog_post import BlogPost
from proj_extensions import db
from r import R


class BlogTag(BaseModel):
    __tablename__ = "blog_tag"

    name = db.Column(db.String(R.dimen.blog_tag_max_length), nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    blog_posts = relationship("BlogPost", order_by=BlogPost.date, secondary=association_table, back_populates="tags")

    def __repr__(self):
        return self.name
