from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from empresa_service import EmpresaService
from empresa_schema import EmpresaCreate, Empresa
from db import connect_db

router = APIRouter(
    prefix="/empresas"
)

@router.post("/", response_model=Empresa, status_code=201, summary="Criar uma nova empresa",
             description="Adiciona uma nova empresa ao banco de dados.")
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(connect_db)):

    service = EmpresaService(db)
    return service.create_empresa(empresa)

@router.get("/", response_model=List[Empresa], status_code=200, summary="Listar todas as empresas",
            description="Retorna uma lista de todas as empresas cadastradas no banco de dados.")
def list_empresas(db: Session = Depends(connect_db)):
    service = EmpresaService(db)
    return service.get_empresas()

@router.get("/{empresa_id}", response_model=Empresa, status_code=200, summary="Obter detalhes de uma empresa",
            description="Busca os detalhes de uma empresa pelo seu ID.")
def list_obrigacao_by_id(empresa_id: int, db: Session = Depends(connect_db)):

    service = EmpresaService(db)
    db_empresa = service.get_empresa_by_id(empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@router.put("/{empresa_id}", response_model=Empresa, status_code=200, summary="Atualizar uma empresa",
            description="Atualiza os dados de uma empresa existente pelo ID.")
def update_empresa(empresa_id: int, empresa: EmpresaCreate, db: Session = Depends(connect_db)):

    service = EmpresaService(db)
    return service.update_empresa(empresa_id, empresa)

@router.delete("/{empresa_id}", status_code=204, summary="Deletar uma empresa",
               description="Remove uma empresa do banco de dados pelo seu ID.")
def delete_empresa(empresa_id: int, db: Session = Depends(connect_db)):

    service = EmpresaService(db)
    service.delete_empresa(empresa_id)
    return {"message": "Empresa deletada com sucesso"}
