from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "프롬프트 관리 서버가 준비되었습니다!"}