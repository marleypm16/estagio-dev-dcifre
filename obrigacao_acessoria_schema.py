from pydantic import BaseModel


class ObrigacaoAcessoriaCreate(BaseModel):
    nome:str
    periodicidade:str
    empresa_id:int


class ObrigacaoAcessoria(ObrigacaoAcessoriaCreate):
    id:int

    class Config:
        from_attributes = True
