from pydantic import BaseModel,ConfigDict

class EmpresaCreate(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: str
    telefone: str


class Empresa(EmpresaCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
