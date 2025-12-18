#!/bin/bash
# ==============================================================================
# Portfolio Application - Docker Management Script
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}[✓]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[!]${NC} $1"
}

print_error() {
    echo -e "${RED}[✗]${NC} $1"
}

# Check if .env file exists
check_env() {
    if [ ! -f ".env" ]; then
        print_warning ".env file not found!"
        print_status "Creating .env from .env.example..."
        cp .env.example .env
        print_warning "Please edit .env file with your credentials before running."
        exit 1
    fi
}

case "$1" in
    dev)
        print_status "Starting development environment..."
        check_env
        docker compose -f docker-compose.dev.yml up --build
        ;;

    dev-detached)
        print_status "Starting development environment (detached)..."
        check_env
        docker compose -f docker-compose.dev.yml up --build -d
        print_status "Development servers running:"
        print_status "  - Backend: http://localhost:8011"
        print_status "  - Frontend: http://localhost:5173"
        ;;

    prod)
        print_status "Starting production environment..."
        check_env
        docker compose up --build
        ;;

    prod-detached)
        print_status "Starting production environment (detached)..."
        check_env
        docker compose up --build -d
        print_status "Application running at: http://localhost:8011"
        ;;

    stop)
        print_status "Stopping all containers..."
        docker compose -f docker-compose.dev.yml down 2>/dev/null || true
        docker compose down 2>/dev/null || true
        print_status "All containers stopped."
        ;;

    logs)
        docker compose logs -f
        ;;

    logs-dev)
        docker compose -f docker-compose.dev.yml logs -f
        ;;

    clean)
        print_warning "This will remove all containers, images, and volumes!"
        read -p "Are you sure? (y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            docker compose -f docker-compose.dev.yml down -v --rmi all 2>/dev/null || true
            docker compose down -v --rmi all 2>/dev/null || true
            docker system prune -f
            print_status "Cleanup complete."
        else
            print_status "Cancelled."
        fi
        ;;

    build)
        print_status "Building production Docker image..."
        docker build -t portfolio-app:latest .
        print_status "Build complete!"
        ;;

    shell)
        print_status "Opening shell in running container..."
        docker exec -it portfolio-app /bin/bash
        ;;

    health)
        print_status "Checking application health..."
        curl -f http://localhost:8011/health && echo "" || print_error "Health check failed!"
        ;;

    *)
        echo "Portfolio Application - Docker Management"
        echo ""
        echo "Usage: $0 {command}"
        echo ""
        echo "Commands:"
        echo "  dev            Start development environment (with logs)"
        echo "  dev-detached   Start development environment (background)"
        echo "  prod           Start production environment (with logs)"
        echo "  prod-detached  Start production environment (background)"
        echo "  stop           Stop all containers"
        echo "  logs           View production logs"
        echo "  logs-dev       View development logs"
        echo "  build          Build production Docker image"
        echo "  clean          Remove all containers, images, and volumes"
        echo "  shell          Open shell in running container"
        echo "  health         Check application health"
        echo ""
        exit 1
        ;;
esac
