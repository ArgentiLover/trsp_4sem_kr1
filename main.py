from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from models import User, Feedback

app = FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float

user = User(name="Данил Гроцкий", id=1, age=19)
feedbacks = []

@app.get("/")
async def get_index():
    return FileResponse("index.html")

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

@app.get("/users")
async def get_user():
    return user

@app.post("/user")
async def check_user_age(user_data: User):
    is_adult = user_data.age >= 18
    return {
        "name": user_data.name,
        "age": user_data.age,
        "is_adult": is_adult
    }


@app.post("/feedback")
async def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Feedback received. Thank you, {feedback.name}."}

@app.get("/feedbacks")
async def get_all_feedbacks():
    return {"feedbacks": feedbacks, "count": len(feedbacks)}
