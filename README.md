#  API de Gestão de Empresas e Obrigações Acessórias

##  Sobre o Projeto
Esta API foi desenvolvida utilizando **FastAPI**, **SQLAlchemy** e **PostgreSQL** para gerenciar **empresas** e suas respectivas **obrigações acessórias**. Ela permite o cadastro, listagem, atualização e remoção dessas entidades, garantindo um gerenciamento eficiente.

##  Tecnologias Utilizadas
- **Python 3.10+**
- **FastAPI** (Framework para API)
- **SQLAlchemy** (ORM para banco de dados)
- **PostgreSQL** (Banco de dados relacional)
- **Pydantic** (Validação de dados)
- **Pytest** (Testes automatizados)

##  Como Configurar o Ambiente

### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/marleypm16/estagio-dev-dcifre.git
cd estagio-dev-dcifre
```

### 2️⃣ Criar um Ambiente Virtual e Instalar Dependências
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ Configurar o Banco de Dados
Crie um arquivo **`.env`** na raiz do projeto com as credenciais do banco:
```
database_url= url do banco de dados
```

### 4️⃣ Criar as Tabelas no Banco de Dados
 execute:
```bash
python migrate.py
```

## 🔧 Endpoints Disponíveis
A documentação interativa pode ser acessada em **`http://127.0.0.1:8000/docs`**.

### 🏢 Empresas
| Método  | Rota            | Descrição |
|---------|----------------|-------------|
| `POST`  | `/empresas/`   | Criar uma empresa |
| `GET`   | `/empresas/`   | Listar todas as empresas |
| `GET`   | `/empresas/{id}` | Obter detalhes de uma empresa |
| `PUT`   | `/empresas/{id}` | Atualizar uma empresa |
| `DELETE` | `/empresas/{id}` | Remover uma empresa |

### 📜 Obrigações Acessórias
| Método  | Rota                    | Descrição |
|---------|--------------------------|-------------|
| `POST`  | `/obrigacoes/`          | Criar uma obrigação |
| `GET`   | `/obrigacoes/`          | Listar todas as obrigações |
| `GET`   | `/obrigacoes/{id}`      | Obter detalhes de uma obrigação |
| `PUT`   | `/obrigacoes/{id}`      | Atualizar uma obrigação |
| `DELETE` | `/obrigacoes/{id}`      | Remover uma obrigação |

##  Testes Automatizados
Para rodar os testes unitários:
```bash
pytest test_arquivo_teste.py
```

##  Funcionalidades Extras
- **Deleção em Cascata**: Quando uma empresa é deletada, suas obrigações também são removidas automaticamente.
- **Validações com Pydantic**: Garantia de dados corretos na entrada.

##  Autor
- **[Marley](https://github.com/marleypm16/)**

