from fastapi import FastAPI

app = FastAPI(title="Student Task API")


@app.get("/")
def read_root():
    return {"message": "API is running"}


# Run with:
# uvicorn starter-code:app --reload
