# 🛠️ Manutenção App – Sistema de Gestão de Ordens de Serviço

Este projeto é um sistema web de gerenciamento de clientes, técnicos, serviços, peças, equipamentos e faturas, desenvolvido com Django.

---

## 🚀 Tecnologias Utilizadas

- Python 3.13+
- Django 5.2+
- Miniconda
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



### 1. Instale as Tecnologias do Projeto
- Python: https://www.python.org/
- Miniconda: https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
- Visual Studio Code: https://code.visualstudio.com/

### 2. Clone o repositório

git clone https://github.com/seu-usuario/2025-1-A3-UDWMJ-FAPA-12.git
cd 2025-1-A3-UDWMJ-FAPA-12

### 3. Ative o Interpretador do Python
- Após clonar o projeto, vá em "Views"
- Depois em "Command Palette"
- E pesquise por "Python: Select Interpreter"
- Selecione o Interpretador do Conda


### 4. Crie e ative um ambiente virtual

- conda create -n manutencaoapp (ou qualquer outro nome que você escolher: conda create -n nome-do-ambiente)
- conda activate manutencaoapp (ou o nome que você botou ao criar o ambiente: conda activate -n nome-do-ambiente)

### 3. Instale as dependências

- conda install pip
- pip install python-decouple
- pip install Pillow
- pip install oracledb
- conda install django
- pip install markdown
- pip install django-filter
- pip install djangorestframework


### 4. Aplique as migrações

- python manage.py makemigrations
- python manage.py migrate

### 5. Rode o servidor

- python manage.py runserver


Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🗃️ Branches por App

Cada funcionalidade está organizada em branches específicas, como:

- clients-models
- clients-views
- clients-templates
- equipments-models
- services-templates
- 

Para trabalhar em uma funcionalidade, troque de branch com:


git checkout nome-da-branch


---

## 📝 Licença

Este projeto é de uso acadêmico.  
Criado por **Christhopper Marques Ferreira – 2025**
