from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class Article(BaseModel):
    id: int
    name: Optional[str]
    price = Optional[Decimal]
    short_description: Optional[str]
    images: Optional[str]
    rating: Optional[str]
    number_of_reviews: Optional[int]
    variants: Optional[str]
    product_description: Optional[str]
    sales_rank: Optional[str]
    link_to_all_reviews: Optional[str]
    scrape_timestamp: Optional[datetime]
    url: Optional[str]

    class Config:
        orm_mode = True
