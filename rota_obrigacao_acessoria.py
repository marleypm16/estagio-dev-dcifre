import db
from fastapi import HTTPException, APIRouter
from models import  ObrigacaoAcessoriaCreate,ObrigacaoAcessoriaModel
from models import  ObrigacaoAcessoria
from typing import List

router = APIRouter(prefix="/obrigacao-acessoria")
db = db.Session()

@router.get("/",response_model=List[ObrigacaoAcessoriaModel],status_code=200)
def listar_obrigacao():
    return db.query(ObrigacaoAcessoria).all()

@router.get("/{obrigacao_acessoria_id}",response_model=ObrigacaoAcessoriaModel,status_code=200)
def listar_obrigacao_id(obrigacao_acessoria_id: int):
    obrigacao =  db.query(ObrigacaoAcessoria).get(obrigacao_acessoria_id)
    if not obrigacao:
        raise HTTPException(status_code=404,detail="Obrigação não encontrada")

    return obrigacao

@router.post("/", response_model=ObrigacaoAcessoriaCreate,status_code=201)
def criar_obrigacao(obrigacao: ObrigacaoAcessoriaCreate):
    nova_obrigacao = ObrigacaoAcessoria(
        nome=obrigacao.nome,
        periodicidade=obrigacao.periodicidade,
        empresa_id=obrigacao.empresa_id,
    )
    db.add(nova_obrigacao)
    db.commit()
    db.refresh(nova_obrigacao)
    return nova_obrigacao

@router.put("/{obrigacao_acessoria_id}", response_model=ObrigacaoAcessoriaCreate,status_code=201)
def atualizar_obrigacao(obrigacao_acessoria_id: int, obrigacao_update: ObrigacaoAcessoriaCreate):
    obrigacao = db.query(ObrigacaoAcessoria).get(obrigacao_acessoria_id)
    if not obrigacao:
        raise HTTPException(status_code=404,detail="obrigação não encontrada")
    obrigacao.nome = obrigacao_update.nome
    obrigacao.periodicidade = obrigacao_update.periodicidade
    obrigacao.empresa_id = obrigacao_update.empresa_id
    db.commit()
    db.refresh(obrigacao)

    return obrigacao


@router.delete("/{obrigacao_acessoria_id}",status_code=200)
def delete_obrigacao_id(obrigacao_acessoria_id: int):
    obrigacao = db.query(ObrigacaoAcessoria).get(obrigacao_acessoria_id)
    if not obrigacao:
        raise HTTPException(status_code=404,detail="Obrigação não encontrada")

    db.delete(obrigacao)
    db.commit()

    return {"Message" : "Obrigacao deletada com sucesso"}