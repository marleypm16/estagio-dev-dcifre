import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_create_obrigacao(client):
    empresa_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12.345.678/0010-99",
            "endereco": "Rua Teste, 123",
            "email": "teste@empresa.com",
            "telefone": "(11) 99999-9999"
        },
    )
    empresa_id = empresa_response.json()["id"]

    response = client.post(
        "/obrigacao-acessoria/",
        json={
            "nome": "Obrigação Teste",
            "periodicidade": "mensal",
            "empresa_id": empresa_id
        },
    )
    obrigacao_id = response.json()["id"]

    assert response.status_code == 201
    assert response.json()["nome"] == "Obrigação Teste"
    assert response.json()["empresa_id"] == empresa_id
    delete_empresa = client.delete(f"/empresas/{empresa_id}")
    assert delete_empresa.status_code == 204


def test_list_obrigacoes(client):
    response = client.get("/obrigacao-acessoria/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_obrigacao_by_id(client):
    empresa_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12.345.678/0011-99",
            "endereco": "Rua Teste, 123",
            "email": "teste@empresa.com",
            "telefone": "(11) 99999-9999"
        },
    )
    empresa_id = empresa_response.json()["id"]

    obrigacao_response = client.post(
        "/obrigacao-acessoria/",
        json={
            "nome": "Obrigação Teste",
            "periodicidade": "mensal",
            "empresa_id": empresa_id
        },
    )
    obrigacao_id = obrigacao_response.json()["id"]

    response = client.get(f"/obrigacao-acessoria/{obrigacao_id}")
    assert response.status_code == 200
    assert response.json()["id"] == obrigacao_id
    delete_empresa = client.delete(f"/empresas/{empresa_id}")
    assert delete_empresa.status_code == 204



def test_delete_obrigacao(client):
    empresa_response = client.post(
        "/empresas/",
        json={
            "nome": "Empresa Teste",
            "cnpj": "12.345.678/0012-99",
            "endereco": "Rua Teste, 123",
            "email": "teste@empresa.com",
            "telefone": "(11) 99999-9999"
        },
    )
    empresa_id = empresa_response.json()["id"]

    obrigacao_response = client.post(
        "/obrigacao-acessoria/",
        json={
            "nome": "Obrigação Teste",
            "periodicidade": "mensal",
            "empresa_id": empresa_id
        },
    )
    obrigacao_id = obrigacao_response.json()["id"]

    delete_response = client.delete(f"/obrigacao-acessoria/{obrigacao_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/obrigacao-acessoria/{obrigacao_id}")
    assert get_response.status_code == 404
    delete_empresa = client.delete(f"/empresas/{empresa_id}")
    assert delete_empresa.status_code == 204
