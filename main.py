# uvicorn main:app --reload
# uvicorn main:app --host 0.0.0.0 --port 10000
from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos, users
from starlette.staticfiles import StaticFiles
from starlette import status
from starlette.responses import RedirectResponse
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
   
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return RedirectResponse(url="/auth", status_code=status.HTTP_302_FOUND)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app)

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)