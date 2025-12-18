# ==============================================================================
# Portfolio Application - Flask Backend
# ==============================================================================
import os
import logging
from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv

# Load environment variables from .env file (development only)
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO if os.getenv('ENV_TYPE') == 'prod' else logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Validate required environment variables
REQUIRED_ENV_VARS = [
    'SECRET_KEY',
    'MONGO_URL',
    'MONGO_DB_NAME',
    'GOOGLE_CLIENT_ID',
    'GOOGLE_CLIENT_SECRET',
    'GOOGLE_REDIRECT_URI'
]

def validate_env():
    """Validate that all required environment variables are set."""
    missing = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing)}\n"
            "Please check your .env file or environment configuration."
        )

# Validate environment in production
if os.getenv('ENV_TYPE') == 'prod':
    validate_env()

# Import blueprints
from routes.client import client
from routes.projects import projects
from routes.auth import auth

# Initialize Flask app
app = Flask(__name__)

# Proxy fix for running behind reverse proxy (nginx)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Security configuration
app.config.update(
    SECRET_KEY=os.getenv('SECRET_KEY'),
    SESSION_COOKIE_SECURE=os.getenv('ENV_TYPE') == 'prod',  # HTTPS only in production
    SESSION_COOKIE_HTTPONLY=True,  # Prevent XSS
    SESSION_COOKIE_SAMESITE='Lax',  # CSRF protection
    PERMANENT_SESSION_LIFETIME=86400,  # 24 hours
)

# CORS configuration
if os.getenv('ENV_TYPE') != 'prod':
    CORS(app, 
         supports_credentials=True, 
         origins=['http://localhost:5173', 'http://127.0.0.1:5173'],
         allow_headers=['Content-Type', 'Authorization'],
         methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    )

app.debug = os.getenv('ENV_TYPE') == 'dev'

# Allow OAuth over HTTP only in development
if os.getenv('OAUTHLIB_INSECURE_TRANSPORT') == '1':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    logger.warning("OAuth insecure transport is enabled. Use only in development!")

# Register blueprints
app.register_blueprint(client)
app.register_blueprint(projects)
app.register_blueprint(auth, url_prefix='/auth')

# Health check endpoint
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'env': os.getenv('ENV_TYPE', 'unknown')}, 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8011))
    debug = os.getenv('ENV_TYPE') != 'prod'
    logger.info(f"Starting server on port {port} (debug={debug})")
    app.run(host='0.0.0.0', port=port, debug=debug)
