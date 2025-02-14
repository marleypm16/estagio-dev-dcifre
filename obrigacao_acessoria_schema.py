from pydantic import BaseModel,ConfigDict


class ObrigacaoAcessoriaCreate(BaseModel):
    nome:str
    periodicidade:str
    empresa_id:int


class ObrigacaoAcessoria(ObrigacaoAcessoriaCreate):
    id:int
    model_config = ConfigDict(from_attributes=True)
