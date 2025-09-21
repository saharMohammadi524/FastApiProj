from pydantic import BaseModel
from uuid import UUID

class RegisterOutput(BaseModel):
    username:str
    id:UUID

class LoginOutput(BaseModel):
    access_token: str
    token_type: str