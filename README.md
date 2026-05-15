# 💈 BarbeariaPRO - Sistema Full Stack de Agendamento

Sistema completo de agendamento para barbearia desenvolvido com FastAPI, JWT, SQLAlchemy e JavaScript puro.

---

# 🚀 Deploy Online

## 🌐 Frontend
https://barbearia-pro-pi.vercel.app

## ⚙️ Backend API
https://barbeariapro.onrender.com/docs

---

# 📸 Funcionalidades

✅ Cadastro de usuários  
✅ Login com autenticação JWT  
✅ Criação de agendamentos  
✅ Listagem de agendamentos  
✅ Exclusão de agendamentos  
✅ Proteção de rotas com token  
✅ Backend online no Render  
✅ Frontend online no Vercel  

---

# 🛠️ Tecnologias Utilizadas

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- FastAPI
- SQLAlchemy
- JWT
- bcrypt

## Banco de Dados
- SQLite

## Deploy
- Render
- Vercel

---

# 🔐 Autenticação JWT

O sistema utiliza autenticação JWT para proteger rotas privadas.

Fluxo:

```txt
Login
↓
Backend verifica usuário
↓
Backend gera token JWT
↓
Frontend salva token no localStorage
↓
Frontend envia Bearer Token
↓
Backend valida autenticação
↓
Usuário autenticado
```

---

# 📁 Estrutura do Projeto

```txt
app/
│
├── auth/
├── database/
├── models/
├── routes/
├── services/
├── security/
```

---

# 🧠 O que aprendi nesse projeto

- APIs REST
- JWT Authentication
- CRUD completo
- SQLAlchemy
- FastAPI
- Deploy Full Stack
- Integração Frontend + Backend
- Debug com logs
- CORS
- Fetch API
- localStorage
- Autenticação Bearer Token
- Organização de backend
- Estruturação de rotas
- Middleware
- Tratamento de erros HTTP
- Render e Vercel
- Autenticação protegida

---

# ⚙️ Como o sistema funciona

## Cadastro

O frontend envia os dados:

```javascript
fetch("/usuarios/")
```

O backend:
- valida os dados
- verifica se usuário já existe
- criptografa senha
- salva no banco

---

## Login

O backend:
- procura usuário no banco
- verifica senha com bcrypt
- cria token JWT
- retorna token para frontend

---

## Agendamentos

Usuário autenticado:
- envia token Bearer
- backend valida JWT
- backend permite criar/listar/deletar agendamentos

---

# 🔒 Segurança

## bcrypt

As senhas NÃO ficam salvas diretamente.

Exemplo:

```txt
123456
```

vira:

```txt
$2b$12$asdasd...
```

---

## JWT

O token contém:

```json
{
  "sub": "usuario",
  "role": "cliente"
}
```

---

# 🌍 Deploy

## Backend → Render

Comando utilizado:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

## Frontend → Vercel

Frontend hospedado separadamente consumindo API online.

---

# 🚨 Problemas que enfrentei

## CORS

Erro porque:
- frontend estava na Vercel
- backend estava no Render

Solução:

```python
CORSMiddleware
```

---

## 404 Not Found

Erro de rota errada.

Exemplo:

```txt
/login
```

quando o correto era:

```txt
/usuarios/login
```

---

## 405 Method Not Allowed

Erro por usar método HTTP errado.

Exemplo:
- GET em rota POST

---

## 403 Forbidden

Erro de autenticação/token inválido.

---

## 500 Internal Server Error

Erro interno Python.

Exemplos:
- variável inexistente
- token inválido
- função duplicada
- rotas incorretas

---

# 🧪 Debug realizado

## Swagger

Utilizado em:

```txt
/docs
```

para testar:
- login
- cadastro
- agendamentos

---

## Console do navegador

Usado para:
- debug JS
- verificar token
- analisar fetch

---

## Logs do Render

Usado para:
- identificar traceback
- erros FastAPI
- problemas JWT
- erros SQLAlchemy

---

# ▶️ Como rodar localmente

## Clone o projeto

```bash
git clone URL_DO_REPOSITORIO
```

---

## Instale dependências

```bash
pip install -r requirements.txt
```

---

## Rode o backend

```bash
uvicorn app.main:app --reload
```

---

# 📌 Melhorias futuras

- PostgreSQL
- Painel Admin
- Upload de imagens
- Responsividade Mobile
- Dashboard avançado
- Sistema de horários reais
- Melhor design responsivo
- Refresh Token
- Logout real
- Sistema de barbeiros

---

# 👨‍💻 Autor

Kauã Fernando
