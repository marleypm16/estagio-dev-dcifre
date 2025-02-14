from db import engine , Base
from empresa_model import Empresa
from obrigacao_acessoria_model import ObrigacaoAcessoria

Base.metadata.create_all(bind=engine)
