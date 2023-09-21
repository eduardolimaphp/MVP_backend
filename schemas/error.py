from pydantic import BaseModel

class ErrorSchema(BaseModel):
    """Erro - Schema para erros"""
    code: int
    name: str
    message: str