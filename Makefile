isort = ./env/bin/python3 -m isort src examples
black = ./env/bin/python3 -m black src examples
flake8 = ./env/bin/python3 -m flake8 src examples

set-env:
	virtualenv -p python3 env

install: set-env
	./env/bin/pip install -r build-requirements.txt

publish: install
	echo "We remove unecessary files/folders"
	echo "----------------------------------"
	rm -rf build/*
	rm -rf dist/*
	rm -rf *-info
	echo "----------------------------------\n"
	echo "python3 setup.py sdist bdist_wheel"
	./env/bin/python3 setup.py sdist bdist_wheel
	echo "python3 -m twine upload dist/*"
	./env/bin/python3 -m twine upload dist/*
	echo "----------------------------------\n"
	echo "We remove unecessary files/folders"
	rm -rf build/*
	rm -rf dist/*
	rm -rf *-info
	echo "----------------------------------\n"

format:
	$(isort)
	$(black)

lint: format
	$(flake8)
	$(isort) --check-only --df
	$(black) --check --diff
