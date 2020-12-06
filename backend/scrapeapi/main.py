import uvicorn

print("Launching FastAPI ASGI Server Uvicorn...")
if __name__ == "__main__":
    uvicorn.run("scrapeapi.api.scrapeapi:app", host="127.0.0.1", port=8000, log_level="info")
