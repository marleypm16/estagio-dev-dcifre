import db
from fastapi import FastAPI

import rota_empresa
import rota_obrigacao_acessoria

app = FastAPI()

app.include_router(rota_empresa.router)
app.include_router(rota_obrigacao_acessoria.router)




