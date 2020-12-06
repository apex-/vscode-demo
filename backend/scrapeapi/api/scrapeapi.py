from fastapi import FastAPI

from scrapeapi.business.biz_scrape import scrape

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/amazon')
async def scrape_price(url: str):
    return scrape(url)


print('Initialized')