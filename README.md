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

📦 Instalação do Backend

1️⃣ Clone o repositório
git clone https://github.com/Davis-leo/EstudaPlus.git
cd EstudaPlus

2️⃣ Crie o ambiente virtual
python -m venv venv
venv\Scripts\activate

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Configure o arquivo .env

Exemplo:

SECRET_KEY=sua_chave_secreta
DEBUG=True

5️⃣ Rode as migrações
python manage.py migrate

6️⃣ Inicie o servidor
python manage.py runserver

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
