from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base
from sqlalchemy.orm import relationship


class ObrigacaoAcessoria(Base):
    __tablename__ = 'obrigacaoacessoria'
    id = Column(Integer, primary_key=True,index=True)
    nome = Column(String)
    periodicidade = Column(String)
    empresa_id= Column(Integer, ForeignKey('empresa.id'))
    empresa = relationship("Empresa", back_populates="obrigacoes")

