from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "The application is running"
