"""One To Many.

...is used to mark that an instance of a class can be associated with
many instances of another class. For example, on a blog engine, an
instance of the Article class could be associated with many instances
of the Comment class. In this case, we would map the mentioned classes
and its relation as follows:
"""


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    comments = relationship("Comment")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"))
