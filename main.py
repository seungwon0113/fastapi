from fastapi import FastAPI

from app.routers.article_router import router as article_router

app = FastAPI()
app.include_router(article_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
