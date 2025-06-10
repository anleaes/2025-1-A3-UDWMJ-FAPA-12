# 🛠️ Manutenção App – Sistema de Gestão de Ordens de Serviço

Este projeto é um sistema web de gerenciamento de clientes, técnicos, serviços, peças, equipamentos e faturas, desenvolvido com Django.

---

## 🚀 Tecnologias Utilizadas

- Python 3.13+
- Django 5.2+
- SQLite (padrão) ou PostgreSQL
- Bootstrap 5 (frontend)
- Git (controle de versão)

---

## 📁 Estrutura do Projeto

```
2025-1-A3-UDWMJ-FAPA-12/
├── apps/
│   ├── clients/
│   ├── equipments/
│   ├── invoices/
│   ├── parts/
│   ├── services/
│   └── technicians/
├── templates/
│   ├── clients/
│   ├── equipments/
│   ├── invoices/
│   ├── parts/
│   ├── services/
│   └── technicians/
├── manutencaoapp/   # Configurações do Django
├── db.sqlite3
└── manage.py
```

---

## 📦 Como rodar o projeto em outra máquina

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/2025-1-A3-UDWMJ-FAPA-12.git
cd 2025-1-A3-UDWMJ-FAPA-12
```

### 2. Crie e ative um ambiente virtual

```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

> Caso não exista um `requirements.txt`, você pode gerar com:
```bash
pip freeze > requirements.txt
```

### 4. Aplique as migrações

```bash
python manage.py migrate
```

### 5. Rode o servidor

```bash
python manage.py runserver
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🗃️ Branches por App

Cada funcionalidade está organizada em branches específicas, como:

- `clients-models`
- `clients-views`
- `clients-templates`
- `equipments-models`
- `services-templates`
- ...

Para trabalhar em uma funcionalidade, troque de branch com:

```bash
git checkout nome-da-branch
```

---

## 📝 Licença

Este projeto é de uso acadêmico.  
Criado por **Christhopper Marques Ferreira – 2025**
