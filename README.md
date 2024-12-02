# My Portfolio (In development)

![GitHub repo size](https://img.shields.io/github/repo-size/Alexsander33set/portfolio?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/Alexsander33set/portfolio?style=for-the-badge)

![Portfólio webpage](./docs/portfolio-page.png)

> running at: [apfs.com.br](https://apfs.com.br)

## 🚀 How to run the project

### 🎲 Running the application (server + frontend)

```bash
# Clone this repository
$ git clone https://github.com/Alexsander33set/portfolio.git
# Access the folder of the project
$ cd portfolio
# Access the server folder
$ cd app/server
# Install dependencies
$ pip install -r requirements.txt
# Add environment variables
$ cp .env.example .env
# Run the application
$ python3 app.py
# The server will start at port:8080 - access http://localhost:8080
```

### 🧭 Running the Frontend (client)

```bash
# Access the client folder
$ cd app/client

# Install dependencies
$ npm install

# Run the application in development mode
$ npm run dev

# The frontend will start at port:5173 - access http://localhost:5173
```

## 🛠 Tecnologias

The following tools were used in the construction of the project:

- Client
  - [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
  - [Vue.js](https://vuejs.org/)
  - [Vue Router](https://router.vuejs.org/)
  - [Vue I18n](https://kazupon.github.io/vue-i18n/)
  - [Pinia](https://pinia.vuejs.org/)
  - [Axios](https://axios-http.com/)
  - [TailwindCSS](https://tailwindcss.com/)
  - [Shadcn](https://ui.shadcn.com/)
  - [Vite](https://vitejs.dev/)
- Server
  - [Python](https://www.python.org/)
  - [Flask](https://flask.palletsprojects.com/en/2.4.x/)
- Database
  - [MongoDB](https://www.mongodb.com/)

## 📡 Endpoints

- `GET    /api/project/<project_id>`: Returns a specific project
- `GET    /api/projects`: Returns all projects
- `POST   /api/add-project`: Adds a new project
- `PUT    /api/update-project/<project_id>`: Updates a specific project
- `DELETE /api/delete-project/<project_id>`: Deletes a specific project
