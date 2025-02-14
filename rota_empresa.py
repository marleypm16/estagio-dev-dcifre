import db
from fastapi import HTTPException, APIRouter
from models import EmpresaCreate  , EmpresaModel
from models import Empresa
from typing import List


db = db.Session()
router = APIRouter(prefix="/empresas")

@router.get("/",response_model=List[EmpresaModel],status_code=200)
def get_empresas():
    return db.query(Empresa).all()

@router.get("/{empresa_id}",response_model=EmpresaModel,status_code=200)
def get_empresa_id(empresa_id: int):
    return db.query(Empresa).get(empresa_id)

@router.post("/", response_model=EmpresaCreate,status_code=201 )
def create_empresa(empresa: EmpresaCreate):
    db_empresa = db.query(Empresa).filter(Empresa.cnpj == empresa.cnpj).first()
    if db_empresa:
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado")


    # Cria uma nova instância do modelo SQLAlchemy (Empresa)
    nova_empresa = Empresa(
        nome=empresa.nome,
        cnpj=empresa.cnpj,
        endereco=empresa.endereco,
        email=empresa.email,
        telefone=empresa.telefone
    )

    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)

    return nova_empresa

@router.put("/{empresa_id}", response_model=EmpresaCreate,status_code=201 )
def update_empresa(empresa_id: int, empresa_update: EmpresaCreate):
    empresa = db.query(Empresa).get(empresa_id)
    if not empresa:
        raise HTTPException(status_code=404,detail="Empresa não encontrada")

    empresa.nome = empresa_update.nome
    empresa.cnpj = empresa_update.cnpj
    empresa.endereco = empresa_update.endereco
    empresa.email = empresa_update.email
    empresa.telefone = empresa_update.telefone
    db.commit()
    db.refresh(empresa)
    return empresa

@router.delete("/{empresa_id}",status_code=200)
def delete_empresa(empresa_id: int):
    empresa = db.query(Empresa).get(empresa_id)
    if not empresa:
        raise HTTPException(status_code=404,detail="Empresa não encontrada")
    db.delete(empresa)
    db.commit()
    return {"Message" : "Empresa deletada com sucesso"}