# Portfolio Project - Copilot Instructions

## Architecture Overview

This is a **monolithic full-stack application** with separated frontend and backend that are bundled together for production deployment.

```
app/
├── client/    → Vue 3 SPA (Vite, Pinia, TailwindCSS, shadcn-vue)
└── server/    → Flask REST API (Python 3.12, MongoDB, Google OAuth)
```

**Data Flow**: Vue frontend → `/api/*` routes → Flask blueprints → MongoDB models → JSON response

**Production bundling**: Frontend builds to `app/server/template/` and Flask serves it as static files (`vite.config.js` → `build.outDir`).

## Development Commands

```bash
# Recommended: Docker (handles both services)
./docker.sh dev              # Start dev environment with hot reload
./docker.sh prod             # Production mode
./docker.sh stop             # Stop containers

# Manual (separate terminals):
cd app/client && npm run dev     # Frontend: http://localhost:5173
cd app/server && python app.py   # Backend: http://localhost:8011

# Build frontend for production:
cd app/client && npm run build   # Outputs to ../server/template/
```

## Project Conventions

### Frontend (`app/client/`)

- **Components**: Use shadcn-vue from `src/components/ui/` - import via barrel exports (e.g., `import { Button } from "@/components/ui/button"`)
- **State**: Pinia stores in `src/stores/` - use `storeToRefs()` for reactive destructuring
- **i18n**: Add translations to both `src/locales/en_us.js` and `src/locales/pt_br.js` - keys must match
- **Path alias**: Use `@/` for imports from `src/` (configured in `vite.config.js`)
- **Views vs Components**: `src/views/` = page-level components routed in `src/router/index.js`

### Backend (`app/server/`)

- **Blueprints structure**: Routes in `routes/` registered in `app.py` - keep routes thin, logic in models
- **Models pattern**: Inherit from `MongoDB` base class in `models/Mongo.py` for database operations
- **Auth decorator**: Use `@login_required` from `decorators.py` for protected routes
- **API prefix**: All API routes use `/api/` prefix, auth uses `/auth/` prefix

### Key Patterns

```python
# Backend: Creating a new model (models/Example.py)
from models.Mongo import MongoDB
class Example(MongoDB):
    def __init__(self):
        super().__init__(collection_name="examples")
    # Add methods following Projects.py pattern
```

```javascript
// Frontend: Adding a new store (stores/example.js)
import { defineStore } from 'pinia'
export const useExampleStore = defineStore('example', () => {
  // Use composition API style (see stores/projects.js)
})
```

## Environment Variables

Backend requires (see `app.py` REQUIRED_ENV_VARS):
- `SECRET_KEY`, `MONGO_URL`, `MONGO_DB_NAME`
- `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_REDIRECT_URI`

Copy `.env.example` → `.env` and fill credentials before running.

## Important Integration Points

- **CORS**: Only enabled in dev mode for `localhost:5173` (see `app.py`)
- **OAuth flow**: `/auth/login` → Google → `/auth/callback` → session stored
- **Static serving**: Flask `client` blueprint serves built Vue app from `./template/`
- **Dev proxy**: Vite proxies `/api/*` and `/auth/*` to Flask backend (configured in `vite.config.js`)
