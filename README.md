Este é um projeto desenvolvido como parte da minha jornada para praticar e aprimorar minhas habilidades de segurança cibernética. O repositório contém um **crawler de XSS** (Cross-Site Scripting) e um **scanner de SQL Injection**, ferramentas essenciais no diagnóstico de vulnerabilidades em aplicativos web.

Como estudante apaixonado por segurança, estou utilizando este projeto para aprender e aplicar conceitos de **penetração de sistemas**, **auditoria de segurança** e **desenvolvimento de ferramentas de segurança**. O objetivo é criar soluções simples, mas eficazes, para detectar falhas comuns em websites.

## Funcionalidades

- **Crawler de XSS**: 
  - Identifica pontos potenciais de vulnerabilidade em um site para ataques XSS.
  - Escaneia páginas e procura por entradas de usuário onde scripts maliciosos podem ser injetados.
  
- **Scanner de SQL Injection**: 
  - Detecta vulnerabilidades de SQL Injection ao tentar injetar comandos maliciosos nas entradas do site.
  - Avalia o comportamento das consultas ao banco de dados e indica se há risco de SQL Injection.

## Como Funciona

**EXECUTE O KillerHub.py PRIMEIRO**

1. **Crawler de XSS**: O crawler percorre as páginas de um site em busca de campos de entrada (como formulários, URLs, etc.). Ele tenta injetar scripts simples para verificar se há execuções não autorizadas de código JavaScript.
   
2. **Scanner de SQL Injection**: O scanner testa entradas comuns em formulários de login, pesquisas e outros campos interativos, verificando se é possível manipular a consulta SQL e acessar informações protegidas.

## Como Rodar

### Requisitos

- Python 3.x
- Bibliotecas necessárias:
  - `requests`
  - `beautifulsoup4`
  - `selenium`
  - `tqdm`
  - `colorama`

### Instalação

1. Clone o repositório:
   ```bash
   https://github.com/luknojo/KillerHub-offSEC.git
