from pydantic import BaseModel

class EmpresaCreate(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str


class Empresa(EmpresaCreate):
    id: int

    class Config:
        from_attributes = True
