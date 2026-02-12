from fastapi import FastAPI
from test_simple_validator import User

app = FastAPI()

@app.post("/users")
def create_user(user: User):
    pass

@app.get("/users/{username}")
def get_user(username: str):
    pass

@app.put("/users/{username}")
def update_user(username: str, user: User):
    pass

@app.delete("/users/{username}")
def delete_user(username: str):
    pass


@app.get("/")
async def root():
    return {"message": "Hello World"}