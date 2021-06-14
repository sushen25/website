.PHONY: dev-up
dev-up:
	docker-compose up

.PHONY: dev-up-d
dev-up-d:
	docker-compose up -d

.PHONY: dev-down
dev-down:
	docker-compose down

.PHNY: dev-prompt
dev-prompt:
	docker exec -it website_web_1 bash

## Linting
## Linting Fixes
.PHONY: black-fix
black-fix:
	black --exclude "migrations|venv" ./

.PHONY: isort-fix
isort-fix:
	isort --skip migrations --skip venv ./

.PHONY: fix
fix: isort-fix black-fix

## Linting Checks
.PHONY: black-check
black-check:
	black --exclude migrations --exclude venv --diff --check ./

.PHONY: flake8-check
flake8-check:
	flake8 --exclude venv ./

.PHONY: isort-check
isort-check:
	isort --skip migrations --skip venv --diff ./

.PHONT: pylint-check
pylint-check:
	pylint --ignore migrations --ignore venv ./

.PHONY: check
check: isort-check black-check flake8-check pylint-check