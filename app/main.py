from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="🚀 AI Chat Assistant with LangChain + VectorDB + Google Calendar")

# Include routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "AI Chat Assistant is running with LangChain + VectorDB!"}
