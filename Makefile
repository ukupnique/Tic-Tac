PYTHON = python3
PIP = pip3
VENV = venv
BIN = $(VENV)/bin
REQ = ../requirements.txt
TEST_DIR = tests

all: run

install: $(VENV)/bin/activate

$(VENV)/bin/activate: $(REQ)
	test -d $(VENV) || $(PYTHON) -m venv $(VENV)
	$(BIN)/$(PIP) install --upgrade pip
	$(BIN)/$(PIP) install -r $(REQ)
	touch $(VENV)/bin/activate

run: install
	$(BIN)/$(PYTHON) main.py

freeze:install
	$(BIN)/$(PIP) freeze > $(REQ)
	@echo "Библиотеки выгружены в $(REQ)"

test: install
	@echo "Запуск тестов..."
	$(BIN)/$(PYTHON) -m pytest --cov=. $(TEST_DIR)

report: install
	$(BIN)/$(PYTHON) -m pytest --cov=. --cov-report=html $(TEST_DIR)
	@echo "Отчет создан в папке htmlcov/index.html"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf $(VENV) +
	rm -rf .pytest_cache +
	rm -rf .coverage
	rm -rf	htmlcov
	@echo "Окружение и кэш удалены."