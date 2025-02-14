from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


Base = declarative_base()
class Empresa(Base):
    __tablename__ = "empresa"

    id = Column(Integer, primary_key=True,index=True)
    nome = Column(String)
    cnpj = Column(String,unique=True)
    endereco = Column(String)
    email = Column(String)
    telefone = Column(String)

class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacaoacessoria"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    periodicidade = Column(String)
    empresa_id = Column(Integer, ForeignKey("empresa.id"))