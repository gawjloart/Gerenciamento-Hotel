## Resumo do Projeto:

Este projeto é um sistema de gerenciamento de hotel desenvolvido usando Flask (Python) no backend e Vue.js (JavaScript) no frontend. O sistema permite criar, atualizar e excluir quartos de hotel, registrar check-ins e check-outs de hóspedes e exibir informações detalhadas sobre os quartos e os hóspedes.

## Uso de Linguagens e Tecnologias:

### Backend (Flask):

- **Linguagem**: Python
- **Framework**: Flask
- **Banco de Dados**: SQLite (para este exemplo)
- **Dependências**: Flask, Flask-CORS, SQLAlchemy (opcional)

### Frontend (Vue.js):

- **Linguagem**: JavaScript (ES6+)
- **Framework**: Vue.js
- **Dependências**: Vue CLI, Vue Router (opcional), axios (opcional)

## Instalação e Uso:

1. **Backend (Flask)**:

    Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/).

    Instale as dependências do Flask:
    ```
    pip install Flask flask-cors
    ```

    Execute o servidor Flask:
    ```
    python app.py
    ```

    O servidor estará disponível em **http://localhost:5000**.

2. **Frontend (Vue.js)**:

    Certifique-se de ter o Node.js e o npm instalados em seu sistema. Você pode baixá-los em [nodejs.org](https://nodejs.org/).

    Instale o Vue CLI globalmente:
    ```
    npm install -g @vue/cli
    ```

    Navegue até o diretório frontend:
    ```
    cd frontend
    ```

    Instale as dependências do frontend:
    ```
    npm install
    ```

    Inicie o servidor:
    ```
    npm run serve
    ```

    O servidor estará disponível em **http://localhost:8080**.

## Observações:

- Certifique-se de ter o servidor Flask em execução para que o frontend possa se comunicar com o backend.
- Este é um projeto básico e pode ser expandido para adicionar mais funcionalidades conforme necessário.
- Divirta-se codificando e explorando as tecnologias Flask e Vue.js!
