build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

gendiff:
	poetry run gendiff

lint:
	poetry run ruff check

test:
	poetry run pytest

coverage-test:
	poetry run pytest --cov=gendiff --cov-report=xml

.PHONY: gendiff
