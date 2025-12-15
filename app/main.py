from fastapi import FastAPI
from app.database import Base, engine
from routers import questions, quiz_sessions, statistics

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quiz API")

app.include_router(questions.router)
app.include_router(quiz_sessions.router)
app.include_router(statistics.router)
