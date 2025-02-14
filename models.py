from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import  declarative_base

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'
    id = Column(Integer, primary_key=True,index=True)
    nome = Column(String)
    cnpj = Column(String,unique=True)
    email = Column(String)
    endereco = Column(String)
    telefone = Column(String)

class ObrigacaoAcessoria(Base):
    __tablename__ = 'obrigacaoacessoria'
    id = Column(Integer, primary_key=True,index=True)
    nome = Column(String)
    periodicidade = Column(String)
    empresa_id= Column(Integer, ForeignKey('empresa.id'))


class EmpresaCreate(BaseModel):
        nome: str
        cnpj: str
        endereco: str
        email: str
        telefone: str

class EmpresaModel(EmpresaCreate):
    id:int

    class Config:
        from_attributes = True


class ObrigacaoAcessoriaCreate(BaseModel):
    nome:str
    periodicidade:str
    empresa_id:int


class ObrigacaoAcessoriaModel(ObrigacaoAcessoriaCreate):
    id:int

    class Config:
        from_attributes = True
