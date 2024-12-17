#Makefile

install:
	poetry install
 
brain-games:
	poetry run brain-games

brain_even:
	poetry run brain-even

build:
	poetry build

package-install:
	pip install dist/*.whl

publish:
	poetry publish --dry-run

make lint:
	poetry run flake8 brain_games

upgrade:
	pip uninstall hexlet-code -y
	make build
	make package-install
