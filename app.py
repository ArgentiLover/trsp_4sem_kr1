from fastapi import FastAPI

# Создаем экземпляр приложения
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Автоперезагрузка действительно работает"}