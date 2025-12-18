# My Portfolio

![GitHub repo size](https://img.shields.io/github/repo-size/Alexsander33set/portfolio?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/Alexsander33set/portfolio?style=for-the-badge)

![Portfólio webpage](./docs/portfolio-page.png)

> Running at: [apfs.com.br](https://apfs.com.br)

## 🐳 Running with Docker (Recommended)

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Quick Start

```bash
# Clone this repository
git clone https://github.com/Alexsander33set/portfolio.git
cd portfolio

# Copy environment variables template
cp .env.example .env

# Edit .env with your credentials
nano .env

# Start with Docker (production mode)
./docker.sh prod

# Or start in development mode (with hot reload)
./docker.sh dev
```

### Docker Commands

| Command | Description |
|---------|-------------|
| `./docker.sh dev` | Start development environment (frontend + backend with hot reload) |
| `./docker.sh dev-detached` | Start development in background |
| `./docker.sh prod` | Start production environment |
| `./docker.sh prod-detached` | Start production in background |
| `./docker.sh stop` | Stop all containers |
| `./docker.sh logs` | View logs |
| `./docker.sh build` | Build production image |
| `./docker.sh clean` | Remove all containers and images |
| `./docker.sh health` | Check application health |

### Ports Used
- **8011**: Backend API (production & development)
- **5173**: Frontend dev server (development only)

---

## 🚀 Running without Docker (Manual Setup)

### Backend (Python/Flask)

```bash
cd app/server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env
# Edit .env with your credentials
python app.py
# Server starts at http://localhost:8011
```

### Frontend (Vue.js)

```bash
cd app/client
npm install
npm run dev
# Frontend starts at http://localhost:5173
```

---

## 🛠 Technologies

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
