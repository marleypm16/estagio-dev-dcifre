from fastapi import APIRouter, Depends, HTTPException
from typing import List
from obrigacao_acessoria_service import ObrigacaoAcessoriaService
from obrigacao_acessoria_schema import ObrigacaoAcessoriaCreate,ObrigacaoAcessoria
from db import connect_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/obrigacao-acessoria")

@router.post("/", response_model=ObrigacaoAcessoriaCreate)
def create_obrigacao(obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(connect_db)):
    service = ObrigacaoAcessoriaService(db)
    return service.criar_obrigacao(obrigacao)

@router.get("/", response_model=List[ObrigacaoAcessoria])
def list_obrigacoes(db: Session = Depends(connect_db)):
    service = ObrigacaoAcessoriaService(db)
    return service.listar_obrigacao()

@router.get("/{obrigacao_id}", response_model=ObrigacaoAcessoria)
def read_obrigacao(obrigacao_id: int, db: Session = Depends(connect_db)):
    service = ObrigacaoAcessoriaService(db)
    db_obrigacao = service.listar_obrigacao_id(obrigacao_id)
    if db_obrigacao is None:
        raise HTTPException(status_code=404, detail="Obrigacao not found")
    return db_obrigacao

@router.put("/{obrigacao_id}", response_model=ObrigacaoAcessoriaCreate)
def update_obrigacao(obrigacao_id: int, obrigacao: ObrigacaoAcessoriaCreate, db: Session = Depends(connect_db)):
    service = ObrigacaoAcessoriaService(db)
    return service.atualizar_obrigacao(obrigacao_id, obrigacao)

@router.delete("/{obrigacao_id}")
def delete_obrigacao(obrigacao_id: int, db: Session = Depends(connect_db)):
    service = ObrigacaoAcessoriaService(db)
    service.delete_obrigacao(obrigacao_id)
    return {"message": "Obrigacao deleted"}