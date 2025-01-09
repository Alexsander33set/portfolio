module.exports = {
  apps: [
    {
      name: 'portfolio',
      script: '/var/www/portfolio/app/server/venv/bin/gunicorn',
      args: '--workers 3 --bind unix:/var/www/portfolio/app/server/portfolio.sock app:app',
      interpreter: 'none',
      cwd: '/var/www/portfolio/app/server',
      env: {
        PATH: '/var/www/portfolio/app/server/venv/bin',
      },
    },
  ],
};
