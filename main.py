from fastapi import FastAPI


import empresa_controller
import obrigacao_acessoria_controller

app = FastAPI()

app.include_router(empresa_controller.router)
app.include_router(obrigacao_acessoria_controller.router)




