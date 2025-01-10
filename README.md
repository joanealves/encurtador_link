# Link Shortener API

## Desafio Back-end

Este projeto consiste na criação de uma REST API para um encurtador de links utilizando **Python** e **Django**. A API possui as seguintes funcionalidades:

### Funcionalidades
- **Cadastro de novos links**: Permite a criação de links encurtados personalizados.
- **Atualização de links**: Possibilidade de alterar informações dos links encurtados.
- **Redirecionamento automático**: O usuário será redirecionado ao acessar o link encurtado.
- **Estatísticas**: Exibe:
  - Total de cliques únicos.
  - Total de cliques gerais.
- **QRCode**: Geração de QR Codes para os links encurtados.
- **Gerenciamento de validade**:
  - Links podem possuir tempo de expiração.
  - Limitação de cliques únicos permitidos.
- **Desativação de links**: Permite ao usuário desativar um link manualmente a qualquer momento.

---

## Setup do Ambiente

### 1. Criação do Ambiente Virtual
Primeiro, crie o ambiente virtual para isolar as dependências do projeto:

#### Linux
```bash
python3 -m venv venv
```

#### Windows
```bash
python -m venv venv
```

### 2. Ativação do Ambiente Virtual
Após criar o ambiente virtual, ative-o com o comando correspondente ao seu sistema operacional:

#### Linux
```bash
source venv/bin/activate
```

#### Windows
```bash
venv\Scripts\Activate
```

Se houver erro de permissão ao ativar o ambiente virtual, execute o comando abaixo e tente novamente:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

---

## Instalação de Dependências

Com o ambiente virtual ativado, instale o **Django** e as demais bibliotecas necessárias para o projeto:

```bash
pip install django
pip install django-ninja
pip install qrcode
```

---

## Configuração do Projeto Django

### 1. Criação do Projeto
Crie o projeto Django utilizando o comando:

```bash
django-admin startproject core .
```

### 2. Rodando o Servidor
Após criar o projeto, execute o servidor para garantir que está tudo configurado corretamente:

```bash
python manage.py runserver
```

Acesse o endereço fornecido no terminal (geralmente `http://127.0.0.1:8000`) para confirmar que o servidor está funcionando.

### 3. Criação do App
Adicione um novo app chamado **shortener** para gerenciar as funcionalidades do encurtador:

```bash
python manage.py startapp shortener
```

---

## Estrutura do Projeto

A organização básica dos arquivos será:

```
project_root/
├── core/               # Diretório principal do projeto Django
│   ├── settings.py     # Configurações do projeto
│   ├── urls.py         # URLs do projeto
│   └── ...
├── shortener/          # App de encurtador de links
│   ├── models.py       # Modelos do banco de dados
│   ├── views.py        # Lógica das rotas
│   ├── urls.py         # URLs específicas do app
│   └── ...
├── manage.py           # Script de gerenciamento do Django
└── venv/               # Ambiente virtual
```

---

## Próximos Passos
- Definir os modelos no arquivo `models.py` para representar links encurtados e suas estatísticas.
- Implementar as rotas e a lógica de negócio utilizando o **Django Ninja**.
- Criar os testes automatizados para validar as funcionalidades.

---

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Django**: Framework para desenvolvimento da API.
- **Django Ninja**: Framework leve para criação de APIs REST.
- **QRCode**: Biblioteca para geração de códigos QR.

---

## Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

---

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).
