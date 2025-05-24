from fastapi import FastAPI
import uvicorn
import os

app = FastAPI(title="Stock Analysis API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Stock Analysis API is running!", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
