from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class AmazonArticle(BaseModel):
    id: int
    name: Optional[str]
    price: Optional[str]
    short_description: Optional[str]
    images: Optional[str]
    rating: Optional[str]
    number_of_reviews: Optional[int]
    variants: Optional[str]
    product_description: Optional[str]
    sales_rank: Optional[str]
    link_to_all_reviews: Optional[str]
    scraped_at: Optional[datetime]
    scrape_url: Optional[str]

    class Config:
        orm_mode = True
