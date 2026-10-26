## 📌 Descrição
Nessa PR, criamos a estrutura de pastas inicial com o poetry, configuramos um linter com Ruff e organizador de comandos com o taskipy, criamos um docker compose para conteinizar o postgresql e um dockerfile para conteinizar nosso backend, tambem instalamos as principais dependencias como o fastapi uvicorn pytest, tambem colocamos um template de pr


## 🔄 Tipo de Alteração
Marque com um `x` o tipo de mudança que esta PR introduz:
- [ ] Nova funcionalidade (`feat`)
- [ ] Correção de bug (`fix`)
- [x] Alteração de infraestrutura, dependências ou configuração (`chore`)
- [ ] Documentação (`docs`)
- [x] Adição ou correção de testes (`test`)

## 🛠️ O que foi feito?
<!-- Liste de forma bullet points os principais entregáveis desta PR -->
- Exemplo: Criado o `docker-compose.yml` com os serviços da API e PostgreSQL.
- Exemplo: Configurada a estrutura base de diretórios do FastAPI com suporte assíncrono.

## 🧪 Como Testar?
<!-- Descreva o passo a passo exato para rodar e validar a sua alteração localmente -->
1. Subir os containers:
   ```bash
   docker compose up --build