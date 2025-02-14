from pydantic import BaseModel


class EmpresaModel(BaseModel):
    nome:str
    cnpj:str
    endereco:str
    email:str
    telefone:str

class ObrigacaoAcessoModel(BaseModel):
    nome:str
    periodicidade:str
    empresa_id:int

