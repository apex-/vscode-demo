from sqlalchemy import (
    Column,
    ForeignKey,
    Boolean,
    Integer,
    String,
    Numeric,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

from scrapeapi.persistence.database import Base, engine

class AmazonArticle(Base):
    __tablename__ = 'amazon_article'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Numeric)
    short_description=Column(String)
    images=Column(String)
    rating=Column(String)
    number_of_reviews=Column(Integer)
    variants=Column(String)
    product_description=Column(String)
    sales_rank=Column(Integer)
    link_to_all_reviews=Column(String)
    scraped_at=Column(DateTime)
    scrape_url=Column(String)

Base.metadata.create_all(bind=engine)
 