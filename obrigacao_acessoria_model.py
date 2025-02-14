from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from db import Base
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

class PeriodicidadeEnum(PyEnum):
    MENSAL = "mensal"
    TRIMESTRAL = "trimestral"
    ANUAL = "anual"

class ObrigacaoAcessoria(Base):
    __tablename__ = 'obrigacaoacessoria'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    periodicidade = Column(String)
    empresa_id = Column(Integer, ForeignKey('empresa.id', ondelete="CASCADE"))
    empresa = relationship("Empresa", back_populates="obrigacoes")
