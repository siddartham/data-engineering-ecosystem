SHELL := bash

install:
	{ python3.8 -m venv venv || py -3.8 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r requirements.txt -e . && \
	mypy --install-types --non-interactive ; \
	echo "Success!"

ci-install:
	{ python3 -m venv venv || py -3 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	python3 -m pip install --upgrade pip wheel && \
	python3 -m pip install -r requirements.txt -e . && \
	echo "Success!"

reinstall:
	{ rm -R venv || echo "" ; } && \
	{ python3.8 -m venv venv || py -3.8 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r test_requirements.txt -r ci_requirements.txt -e . --upgrade --upgrade-strategy eager && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	make requirements && \
	echo "Success!"

upgrade:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools requirements freeze\
	 -nv '*' . pyproject.toml tox.ini ci_requirements.txt\
	 > .requirements.txt && \
	pip3 install --upgrade --upgrade-strategy eager\
	 -r .requirements.txt && \
	rm .requirements.txt && \
	make requirements && \
	echo "Upgrade completed successfully!"

clean:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools uninstall-all\
	 -e dev_requirements.txt\
	 -e ci_requirements.txt\
     -e pyproject.toml\
     -e tox.ini\
	 -e . && \
	daves-dev-tools clean && \
	echo "Success!"

editable:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools install-editable --upgrade-strategy eager && \
	make requirements && \
	echo "Success!"

requirements:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools requirements update -nv flake8 && \
	echo "Success!"

test:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	if [[ "$$(python -V)" = "Python 3.8."* ]] ;\
	then tox -r -p -o ;\
	else tox -r -e pytest ;\
	fi

distribute:
	{ . venv/bin/activate || venv/Scripts/activate.bat; } && \
	daves-dev-tools pypi distribute --skip-existing

remodel:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	python3 scripts/remodel.py

format:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	black . && isort . && flake8 && mypy

