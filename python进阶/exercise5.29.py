from pydantic import BaseModel, Field, field_validator
from datetime import datetime


# ========== 请求体 ==========
class CreateUserRequest(BaseModel):
    username: str = Field(min_length=1, max_length=20)
    email: str = Field(pattern=r"^\S+@\S+\.\S+$")
    age: int = Field(ge=0, le=150)

    @field_validator("username")
    @classmethod
    def check_username(cls, v):
        if " " in v:
            raise ValueError("用户名不能包含空格")
        return v


# ========== 响应体 ==========
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime


# ========== 使用 ==========
data = {"username": "张三", "email": "zs@example.com", "age": 25}
user = CreateUserRequest(**data)  # 自动校验
print(user.model_dump())
