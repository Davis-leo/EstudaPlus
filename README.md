📚 EstudaPlus

Plataforma de Apoio ao Estudo para Alunos da Rede Pública

O EstudaPlus é uma plataforma educacional desenvolvida com foco em apoio ao aprendizado de alunos da rede pública, promovendo inclusão digital, reforço escolar e redução da evasão.

Este projeto integra conhecimentos de múltiplas disciplinas da área de tecnologia e propõe uma solução escalável, moderna e com impacto social real.


🎯 Objetivo do Projeto

Desenvolver uma plataforma web que ofereça:


📖 Conteúdos didáticos simplificados


👨‍🏫 Painel administrativo para professores voluntários

A proposta é criar um ambiente acessível, responsivo e intuitivo que auxilie alunos no reforço escolar e preparação para avaliações.


🌍 Impacto Social

O EstudaPlus contribui para:

Redução da evasão escolar

Inclusão digital

Apoio a estudantes em situação de vulnerabilidade

Democratização do acesso a materiais educacionais

A plataforma foi idealizada como ferramenta de apoio complementar ao ensino tradicional.


🧠 Disciplinas Integradas


Este projeto integra conhecimentos das seguintes áreas:


💻 Desenvolvimento Web

🗄 Banco de Dados

🏗 Engenharia de Software

🎨 UX/UI

☁️ Computação em Nuvem (Cloud)

🛠 Stack Tecnológica


🔥 Frontend

Next.js

React

TypeScript

Tailwind CSS

Shadcn UI

Zustand

React Hook Form

Zod


🛠 Backend

Django

Django REST Framework

Django Simple JWT (Autenticação)

Django Filters

Python Decouple


💳 Integrações Futuras

Sistema de permissões por perfil (Aluno / Professor)

Escalabilidade via Cloud


🏗 Arquitetura do Sistema

O sistema segue arquitetura desacoplada:

Frontend (Next.js) → Consome API REST
Backend (Django + DRF) → Responsável por:

Autenticação

Gerenciamento de usuários

Gerenciamento de conteúdos

Persistência de dados

Controle de permissões

Essa separação garante:

Escalabilidade

Manutenção facilitada

Evolução modular


🔐 Funcionalidades Principais

👨‍🎓 Área do Aluno

Cadastro e login com JWT

Acesso a conteúdos por disciplina

Acompanhamento de desempenho


👨‍🏫 Área do Professor Voluntário

Cadastro de conteúdos

Monitoramento de desempenho dos alunos



📦 Configuração do projeto:

✅ 1️⃣ Instalar as ferramentas

Instalar:

Python (mesma versão que usava)

MySQL

Git

(Opcional) HeidiSQL

Testar no terminal:

python --version
git --version
mysql --version

Se respondeu → ok.

✅ 2️⃣ Clonar o projeto do GitHub

Escolha a pasta onde quer o projeto:

git clone https://github.com/Davis-leo/EstudaPlus.git
cd EstudaPlus
✅ 3️⃣ Criar o ambiente virtual
python -m venv venv
venv\Scripts\activate

Se aparecer (venv) no terminal → perfeito.

✅ 4️⃣ Instalar dependências
pip install -r requirements.txt

Pronto. Backend instalado.

✅ 5️⃣ Criar o arquivo .env

Criar arquivo .env na raiz do projeto.

Colar seu backup salvo no Drive:

DJANGO_SECRET_KEY="sua_secret_key"

DB_NAME="estudaplus"
DB_USER="root"
DB_PASSWORD="sua_senha"
DB_HOST="127.0.0.1"
DB_PORT="3306"

⚠️ Garantir que .env está no .gitignore.

✅ 6️⃣ Criar o banco no MySQL

Entrar no MySQL e rodar:

CREATE DATABASE estudaplus CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
✅ 7️⃣ Rodar migrations
python manage.py migrate

Isso recria todas as tabelas.

✅ 8️⃣ Criar superusuário
python manage.py createsuperuser

Criar usuário admin.

✅ 9️⃣ Popular banco (cursos)

Opção 1:
Rodar seu script SQL.

Opção 2 (melhor futuramente):
Rodar script seed automatizado.

✅ 🔟 Rodar servidor
python manage.py runserver

Testar:

http://127.0.0.1:8000/admin/

✅ 1️⃣1️⃣ Reconfigurar Postman

Criar Environment

Definir BASE_URL

Fazer login novamente

Gerar novo token

Atualizar Authorization

✅ 1️⃣ Verificar se o remote está configurado

Dentro da pasta do projeto, rode:

git remote -v

Você deve ver algo assim:

origin  https://github.com/Davis-leo/EstudaPlus.git (fetch)
origin  https://github.com/Davis-leo/EstudaPlus.git (push)

Se aparecer isso → está tudo certo ✅


📈 Escalabilidade e Cloud

O projeto foi estruturado para futura implantação em ambiente cloud, permitindo:

Deploy em serviços como AWS, Azure ou Render

Banco de dados gerenciado

Separação de ambientes (dev / staging / prod)

Escalabilidade horizontal


🎓 Finalidade Acadêmica

Este projeto atende ao escopo do:

Projeto 4 – Plataforma de Apoio ao Estudo para Alunos da Rede Pública

Demonstrando aplicação prática de conceitos técnicos, integração multidisciplinar e preocupação com impacto social.

🚧 Status do Projeto

Em desenvolvimento — novas funcionalidades estão sendo implementadas.
