from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def main():
    return "work"


#uvicorn main:app --reload - start server

