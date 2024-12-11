#Makefile

install:
	poetry install
 
brain-games:
	poetry run brain-games

build:
	poetry build

package-install:
	pip install dist/*.whl

publish:
	poetry publish --dry-run

make lint:
	poetry run flake8 brain_games
