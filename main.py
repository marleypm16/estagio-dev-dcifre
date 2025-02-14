from fastapi import FastAPI


import empresa_controller
import obrigacao_acessoria_controller

app = FastAPI(
    title="Api Desafio Dcifre",
    description="Api permite gerenciar empresas e obrigações Acessórias",
    contact={
        "Nome" : "Marley Pinheiro Martins",
        "email": "marleypm16@gmail.com"
    }
)

app.include_router(empresa_controller.router)
app.include_router(obrigacao_acessoria_controller.router)




