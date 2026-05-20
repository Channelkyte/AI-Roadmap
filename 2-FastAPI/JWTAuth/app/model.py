from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default = None)
    title: str = Field(default = None)
    content: str = Field(default = None)
    
    class Config:
        schema_extra = {
            "post_demo" : {
                "title": "Title About Animals",
                "content": "Content About Animals"
            }
        }

class UserSchema(BaseModel):
    fullName: str = Field(default = None)
    email: EmailStr = Field(default = None)
    password: str = Field(default = None)
    
    class Config:
        the_schema = {
            "user_demo": {
                "name" : "John",
                "email" : "johndoe@john.com",
                "password" : "123"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default = None)
    password: str = Field(default = None)
    
    class Config:
        the_schema = {
            "user_demo": { 
                "email" : "johndoe@john.com",
                "password" : "123"
            }
        }