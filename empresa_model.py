from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base
from sqlalchemy.orm import relationship


class Empresa(Base):
    __tablename__ = 'empresa'
    id = Column(Integer, primary_key=True,index=True)
    nome = Column(String)
    cnpj = Column(String,unique=True)
    email = Column(String)
    endereco = Column(String)
    telefone = Column(String)
    obrigacoes = relationship("ObrigacaoAcessoria", back_populates="empresa")





