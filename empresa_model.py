from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresa'
    id = Column(Integer, primary_key=True,index=True)
    nome = Column(String)
    cnpj = Column(String,unique=True)
    email = Column(String)
    endereco = Column(String)
    telefone = Column(String)




