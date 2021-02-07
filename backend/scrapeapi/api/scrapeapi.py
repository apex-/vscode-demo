from fastapi import FastAPI, Query

from scrapeapi.business.biz_scrape import (

    biz_amazon_scrape,
)
from scrapeapi.api.apimodels import AmazonArticle

app = FastAPI(title="Scrape API", version="1.0")

@app.post('/product', tags=["Amazon"])
async def add_product(url: str):
    return biz_amazon_scrape(url)

@app.get('/product', tags=["Amazon"])
async def list_products(url: str):
    return biz_amazon_scrape(url)

@app.delete('/product', tags=["Amazon"])
async def delete_products(url: str):
    return biz_amazon_scrape(url)

@app.get('/test_scrape', tags=["Amazon"], response_model=AmazonArticle)
async def test_scrape_product(url: str):
    return biz_amazon_scrape(url)
