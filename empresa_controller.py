from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.orm import Session

from empresa_service import EmpresaService
from empresa_schema import EmpresaCreate,Empresa
from db import connect_db

router = APIRouter(prefix="/empresas")

@router.post("/", response_model=EmpresaCreate)
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(connect_db)):
    service = EmpresaService(db)
    return service.create_empresa(empresa)

@router.get("/", response_model=List[Empresa])
def list_empresas(db: Session = Depends(connect_db)):
    service = EmpresaService(db)
    return service.get_empresas()

@router.get("/{empresa_id}", response_model=Empresa)
def read_empresa(empresa_id: int, db: Session = Depends(connect_db)):
    service = EmpresaService(db)
    db_empresa = service.get_empresa_id(empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa not found")
    return db_empresa

@router.put("/{empresa_id}", response_model=EmpresaCreate)
def update_empresa(empresa_id: int, empresa: EmpresaCreate, db: Session = Depends(connect_db)):
    service = EmpresaService(db)
    return service.update_empresa(empresa_id, empresa)

@router.delete("/{empresa_id}")
def delete_empresa(empresa_id: int, db: Session = Depends(connect_db)):
    service = EmpresaService(db)
    service.delete_empresa(empresa_id)
    return {"message": "Empresa deleted"}