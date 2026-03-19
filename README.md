# EstudaPlus

Plataforma de apoio ao estudo para alunos da rede pública, focada em inclusão digital e reforço escolar.

---

## Stack Tecnológica

**Frontend**  
Next.js | React | TypeScript | Tailwind CSS | Shadcn UI | Zustand | React Hook Form | Zod

**Backend**  
Django | Django REST Framework | Django Simple JWT | Django Filters | Python Decouple

**Banco de Dados**  
MySQL

---

## Arquitetura

Frontend desacoplado (Next.js) consome API REST do backend (Django + DRF), garantindo:

- Separação de responsabilidades  
- Escalabilidade  
- Manutenção modular  

---

## Funcionalidades

### Aluno
- Cadastro e login com JWT  
- Acesso a conteúdos por disciplina  
- Acompanhamento de desempenho  

### Professor Voluntário
- Gestão de conteúdos  
- Monitoramento de desempenho dos alunos  

---

# Configuração do Projeto

## 1. Instalar ferramentas

- Node.js  
- Python  
- MySQL  
- Git  

---

## 2. Clonar repositório

```bash
git clone https://github.com/Davis-leo/EstudaPlus.git
cd EstudaPlus
```

---

## 3. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 5. Configurar .env

Criar arquivo `.env` na raiz do projeto:

```env
DJANGO_SECRET_KEY="sua_secret_key"
DB_NAME="estudaplus"
DB_USER="root"
DB_PASSWORD="sua_senha"
DB_HOST="127.0.0.1"
DB_PORT="3306"
```

Verificar se `.env` está no `.gitignore`.

---

## 6. Criar banco MySQL

```sql
CREATE DATABASE estudaplus
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

---

## 7. Rodar migrations

```bash
python manage.py migrate
```

---

## 8. Criar superusuário

```bash
python manage.py createsuperuser
```

Acessar:

```
http://127.0.0.1:8000/admin/
```

---

## 9. Popular banco (cursos)

### Opção 1 — Restaurar via arquivo `.sql`

Entrar no MySQL:

```bash
mysql -u root -p
```

Selecionar o banco:

```sql
USE estudaplus;
```

Executar o backup:

```sql
SOURCE caminho/cursos_backup.sql;
```

Verificar:

```sql
SHOW TABLES;
SELECT * FROM courses_course;
```

---

### Opção 2 — Seed automatizado (recomendado)

```bash
python manage.py seed_courses
```

---

## 10. Rodar servidor

```bash
python manage.py runserver
```

Acessar:

```
http://127.0.0.1:8000/
```

---

## Configuração do Postman (JWT)

1. Criar um Environment  
2. Definir variável:

```
BASE_URL = http://127.0.0.1:8000/api/v1
```

3. Fazer login  
4. Copiar `access_token`  
5. Usar como Bearer Token nas rotas protegidas  

---

## Status

Em desenvolvimento.