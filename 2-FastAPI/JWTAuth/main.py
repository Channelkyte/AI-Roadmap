import uvicorn
from fastapi import FastAPI, Body, Depends
from app.model import PostSchema
from app.model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer


posts = [
    {
        "id": 1,
        "title": "penguins",
        "text": "hi, i'm a penguin"
    },
    {
        "id": 2,
        "title": "tigers",
        "text": "hi, i'm a tiger"
    },
    {
        "id": 3,
        "title": "koalas",
        "text": "hi, i'm a koala"
    }
]

users = []

app = FastAPI()

# get posts
@app.get("/post", tags=["posts"])
def get_posts():
    return {"data": posts}


@app.get("/post/{id}", tags=["posts"])
def get_one_post(id: int):
    for post in posts:
        if post["id"] == id:
            return {"data": post}

    return {"error": "Post not found"}


@app.post(
    "/post",
    tags=["posts"],
    dependencies=[Depends(jwtBearer())]
)
def add_post(post: PostSchema):
    new_post = post.dict()
    new_post["id"] = len(posts) + 1
    posts.append(new_post)

    return {"info": "Post Added", "data": new_post}


@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(...)):
    users.append(user.dict())
    return signJWT(user.email)


def check_user(data: UserLoginSchema):
    for user in users:
        if user["email"] == data.email and user["password"] == data.password:
            return True
    return False


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {"Error": "Invalid Login Details"}


@app.get(
    "/user/me",
    tags=["user"],
    dependencies=[Depends(jwtBearer())]
)
def user_me():
    return {
        "data": "This is a protected route"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)