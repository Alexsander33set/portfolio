new env:
	ifeq ($(OS), Windows_NT)
		python -m venv .venv
	else
		python3 -m venv .venv
	endif

env:
	ifeq ($(OS), Windows_NT)
		.\.venv\Scripts\activate
	else
		.\.venv\bin\activate
	endif

run app:
	flask --app .\app\server\app.py run -p 8080
