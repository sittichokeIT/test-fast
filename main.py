from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
app = FastAPI()


origins = [
    "http://127.0.0.2:8000",
    "http://127.0.0.2"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def test():
    return {
        "message": "hello world"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.2", port=8000, log_level="info",reload =True)