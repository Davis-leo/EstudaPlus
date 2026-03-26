# EstudaPlus

Plataforma de apoio ao estudo para alunos da rede pública, focada em inclusão digital e reforço escolar.

---

## 🚀 Stack Tecnológica

**Frontend**
Next.js | React | TypeScript | Tailwind CSS | Shadcn UI | Zustand | React Hook Form | Zod

**Backend**
Django | Django REST Framework | JWT | Django Filters | Python Decouple

**Banco de Dados**
MySQL

---

## 🧠 Arquitetura

Frontend desacoplado (Next.js) consumindo API REST do backend (Django + DRF), garantindo:

* Separação de responsabilidades
* Escalabilidade
* Manutenção modular

---

## ✨ Funcionalidades

### 👨‍🎓 Aluno

* Cadastro e login com JWT
* Acesso a conteúdos por disciplina
* Acompanhamento de desempenho

### 👨‍🏫 Professor Voluntário

* Gestão de conteúdos
* Monitoramento de desempenho dos alunos

---

# ⚙️ Configuração do Projeto

## 📌 1. Pré-requisitos

* Node.js (LTS recomendado)
* Python
* MySQL
* Git

---

## 📥 2. Clonar repositório

```bash
git clone https://github.com/Davis-leo/EstudaPlus.git
cd EstudaPlus
```

---

# 🖥️ BACKEND

## 🔧 3. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 📦 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 🔐 5. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz:

```env
DJANGO_SECRET_KEY="sua_secret_key"
DB_NAME="estudaplus"
DB_USER="root"
DB_PASSWORD="sua_senha"
DB_HOST="127.0.0.1"
DB_PORT="3306"
```

---

## 🗄️ 6. Criar banco de dados

```sql
CREATE DATABASE estudaplus
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

---

## 🔄 7. Rodar migrations

```bash
python manage.py migrate
```

---

## 👤 8. Criar superusuário

```bash
python manage.py createsuperuser
```

Acessar:

```
http://127.0.0.1:8000/admin/
```

---

## 🌱 9. Popular banco

### Opção 1 — Importar `.sql`

```bash
mysql -u root -p
```

```sql
USE estudaplus;
SOURCE caminho/cursos_backup.sql;
```

---

### Opção 2 — Seed automatizado (recomendado)

```bash
python manage.py seed_courses
```

---

## ▶️ 10. Rodar backend

```bash
python manage.py runserver
```

API disponível em:

```
http://127.0.0.1:8000/
```

---

# 🌐 FRONTEND

## 📁 11. Acessar pasta do frontend

```bash
cd frontend/estudaplus-frontend
```

---

## 📦 12. Instalar dependências

```bash
npm install
```

---

## ▶️ 13. Rodar frontend

```bash
npm run dev
```

Acessar:

```
http://localhost:3000
```

---

## 🔐 Autenticação

O frontend utiliza **NextAuth**.

Caso necessário, configure variáveis de ambiente no `.env` do frontend.

---

## 🧪 Testes com Postman (Backend)

1. Criar um Environment
2. Definir:

```
BASE_URL = http://127.0.0.1:8000/api/v1
```

3. Fazer login
4. Copiar `access_token`
5. Usar como Bearer Token

---

## 📁 Estrutura do Frontend

* `src/app` → rotas (App Router)
* `src/components` → componentes
* `src/lib` → utilidades e API
* `src/services` → integração com backend
* `src/schemas` → validações

---

## 📌 Observações importantes

* A pasta `node_modules` não é versionada
* Execute sempre `npm install` ao clonar o projeto
* O backend deve estar rodando para o frontend funcionar corretamente

---

## 🚀 Deploy

Frontend pode ser hospedado na Vercel
Backend pode ser hospedado em serviços como Railway, Render ou VPS

---

## 📊 Status

🚧 Em desenvolvimento
