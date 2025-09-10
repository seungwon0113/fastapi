from app import app

print('나는 asgi.py 야', __name__)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)