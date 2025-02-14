from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ObrigacaoAcessoria(Base):
    __tablename__ = 'obrigacaoacessoria'
    id = Column(Integer, primary_key=True,index=True)
    nome = Column(String)
    periodicidade = Column(String)
    empresa_id= Column(Integer, ForeignKey('empresa.id'))

