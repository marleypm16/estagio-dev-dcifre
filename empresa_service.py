from sqlalchemy.orm import Session
from empresa_schema import EmpresaCreate
from empresa_model import Empresa

class EmpresaService:
    def __init__(self, db:Session):
        self.db = db

    def get_empresas(self):
        return self.db.query(Empresa).all()

    def get_empresa_id(self,empresa_id: int):
        return self.db.get(Empresa,empresa_id)

    def create_empresa(self,empresa: EmpresaCreate):


        nova_empresa = Empresa(
            nome=empresa.nome,
            cnpj=empresa.cnpj,
            endereco=empresa.endereco,
            email=empresa.email,
            telefone=empresa.telefone
        )

        self.db.add(nova_empresa)
        self.db.commit()
        self.db.refresh(nova_empresa)

        return nova_empresa


    def update_empresa(self,empresa_id: int, empresa_update: EmpresaCreate):
        empresa = self.db.get(Empresa,empresa_id)


        empresa.nome = empresa_update.nome
        empresa.cnpj = empresa_update.cnpj
        empresa.endereco = empresa_update.endereco
        empresa.email = empresa_update.email
        empresa.telefone = empresa_update.telefone
        self.db.commit()
        self.db.refresh(empresa)
        return empresa


    def delete_empresa(self,empresa_id: int):
        empresa = self.db.get(Empresa,empresa_id)
        self.db.delete(empresa)
        self.db.commit()
        return {"Message": "Empresa deletada com sucesso"}