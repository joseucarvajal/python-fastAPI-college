from fastapi import FastAPI
from models.course import Course

app = FastAPI()

@app.post("/course")
async def create_course(course:Course):
    return course