from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from obrigacao_acessoria_model import PeriodicidadeEnum
from obrigacao_acessoria_service import ObrigacaoAcessoriaService
from obrigacao_acessoria_schema import ObrigacaoAcessoriaCreate, ObrigacaoAcessoria
from db import connect_db

router = APIRouter(
    prefix="/obrigacao-acessoria"
)

@router.post("/", response_model=ObrigacaoAcessoria, status_code=201,
             summary="Criar uma nova obrigação acessória",
             description="Adiciona uma nova obrigação acessória ao banco de dados.")
def create_obrigacao(obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(connect_db)):
    if obrigacao.periodicidade.lower() not in [item.value for item in PeriodicidadeEnum]:
        raise HTTPException(status_code=422, detail="A periodicidade deve ser 'mensal', 'trimestral' ou 'anual'.")

    service = ObrigacaoAcessoriaService(db)
    return service.create_obrigacao(obrigacao)

@router.get("/", response_model=List[ObrigacaoAcessoria], status_code=200,
            summary="Listar todas as obrigações acessórias",
            description="Retorna uma lista de todas as obrigações acessórias cadastradas no banco de dados.")
def get_obrigacoes(db: Session = Depends(connect_db)):

    service = ObrigacaoAcessoriaService(db)
    return service.get_obrigacao()

@router.get("/{obrigacao_id}", response_model=ObrigacaoAcessoria, status_code=200,
            summary="Obter detalhes de uma obrigação acessória",
            description="Busca os detalhes de uma obrigação acessória pelo seu ID.")
def get_obrigacao_by_id(obrigacao_id: int, db: Session = Depends(connect_db)):

    service = ObrigacaoAcessoriaService(db)
    db_obrigacao = service.get_obrigacao_by_id(obrigacao_id)
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    return db_obrigacao

@router.put("/{obrigacao_id}", response_model=ObrigacaoAcessoria, status_code=200,
            summary="Atualizar uma obrigação acessória",
            description="Atualiza os dados de uma obrigação acessória existente pelo ID.")
def update_obrigacao(obrigacao_id: int, obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(connect_db)):
    service = ObrigacaoAcessoriaService(db)
    db_obrigacao = service.get_obrigacao_by_id(obrigacao_id)
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigação não encontrada")
    if obrigacao.periodicidade.lower() not in [item.value for item in PeriodicidadeEnum]:
        raise HTTPException(status_code=422, detail="A periodicidade deve ser 'mensal', 'trimestral' ou 'anual'.")
    return service.update_obrigacao(obrigacao_id, obrigacao)

@router.delete("/{obrigacao_id}", status_code=204,
               summary="Deletar uma obrigação acessória",
               description="Remove uma obrigação acessória do banco de dados pelo seu ID.")
def delete_obrigacao(obrigacao_id: int, db: Session = Depends(connect_db)):
    service = ObrigacaoAcessoriaService(db)
    service.delete_obrigacao(obrigacao_id)
    return {"message": "Obrigação deletada com sucesso"}
