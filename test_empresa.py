import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

# Teste para criar uma empresa
def test_create_empresa(client):
    response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12.345.678/0007-99",
            "endereco": "Rua Teste, 123",
            "email": "teste@empresa.com",
            "telefone": "(11) 99999-9999"
        },
    )
    empresa_id = response.json()["id"]

    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Empresa Teste"
    assert data["cnpj"] == "12.345.678/0007-99"
    assert "id" in data
    delete_response = client.delete(f"/empresas/{empresa_id}")

# Teste para listar empresas
def test_list_empresas(client):
    response = client.get("/empresas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Teste para obter uma empresa por ID
def test_get_empresa_by_id(client):
    create_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12.345.678/0025-99",
            "endereco": "Rua Teste, 123",
            "email": "teste@empresa.com",
            "telefone": "(11) 99999-9999"
        },
    )
    assert create_response.status_code == 201
    empresa_id = create_response.json()["id"]

    get_response = client.get(f"/empresas/{empresa_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == empresa_id
    assert data["nome"] == "Empresa Teste"
    delete_response = client.delete(f"/empresas/{empresa_id}")

# Teste para atualizar uma empresa
def test_update_empresa(client):
    create_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12.345.678/0012-99",
            "endereco": "Rua Teste, 123",
            "email": "teste@empresa.com",
            "telefone": "(11) 99999-9999"
        },
    )
    assert create_response.status_code == 201
    empresa_id = create_response.json()["id"]

    update_response = client.put(
        f"/empresas/{empresa_id}",
        json={
            "nome": "Empresa Atualizada",
            "cnpj": "98.765.432/0001-11",
            "endereco": "Rua Nova, 456",
            "email": "atualizada@empresa.com",
            "telefone": "(11) 88888-8888"
        },
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["id"] == empresa_id
    assert data["nome"] == "Empresa Atualizada"
    delete_response = client.delete(f"/empresas/{empresa_id}")


# Teste para deletar uma empresa
def test_delete_empresa(client):
    create_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12.345.678/0066-99",
            "endereco": "Rua Teste, 123",
            "email": "teste@empresa.com",
            "telefone": "(11) 99999-9999"
        },
    )
    assert create_response.status_code == 201
    empresa_id = create_response.json()["id"]

    delete_response = client.delete(f"/empresas/{empresa_id}")
    assert delete_response.status_code == 204
    get_response = client.get(f"/empresas/{empresa_id}")
    assert get_response.status_code == 404
