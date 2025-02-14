from db import Session
from obrigacao_acessoria_schema import  ObrigacaoAcessoriaCreate
from obrigacao_acessoria_model import  ObrigacaoAcessoria

class ObrigacaoAcessoriaService:
    def __init__(self, db:Session):
        self.db = db

    def get_obrigacao(self):
        return self.db.query(ObrigacaoAcessoria).all()


    def get_obrigacao_by_id(self,obrigacao_acessoria_id: int):
        obrigacao = self.db.get(ObrigacaoAcessoria,obrigacao_acessoria_id)

        return obrigacao


    def create_obrigacao(self,obrigacao: ObrigacaoAcessoriaCreate):
        nova_obrigacao = ObrigacaoAcessoria(
            nome=obrigacao.nome,
            periodicidade=obrigacao.periodicidade,
            empresa_id=obrigacao.empresa_id,
        )
        self.db.add(nova_obrigacao)
        self.db.commit()
        self.db.refresh(nova_obrigacao)
        return nova_obrigacao


    def update_obrigacao(self,obrigacao_acessoria_id: int, obrigacao_update: ObrigacaoAcessoriaCreate):
        obrigacao =self.db.get(ObrigacaoAcessoria,obrigacao_acessoria_id)

        obrigacao.nome = obrigacao_update.nome
        obrigacao.periodicidade = obrigacao_update.periodicidade.lower()
        obrigacao.empresa_id = obrigacao_update.empresa_id
        self.db.commit()
        self.db.refresh(obrigacao)

        return obrigacao


    def delete_obrigacao(self,obrigacao_acessoria_id: int):
        obrigacao = self.db.get(ObrigacaoAcessoria,obrigacao_acessoria_id)


        self.db.delete(obrigacao)
        self.db.commit()

        return {"Message": "Obrigacao deletada com sucesso"}
