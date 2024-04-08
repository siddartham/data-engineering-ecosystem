SHELL := bash
# This is the version of python used for local development
PYTHON_VERSION := 3.8

install:
	{ python$(PYTHON_VERSION) -m venv venv || py -$(PYTHON_VERSION) -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade setuptools && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r requirements.txt -e '.[all]' && \
	analytics-orm spark install-snowflake-jdbc-driver && \
	analytics-orm spark install-databricks-jdbc-driver && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	echo "Success!"

ci-install:
	{ python3 -m venv venv || py -3 -m venv venv ; } && \
	pip3 install --upgrade setuptools && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	{ python3 -m pip install --upgrade pip setuptools wheel || echo "" ; } && \
	python3 -m pip install -r requirements.txt -e '.[all]' && \
	echo "Success!"

reinstall:
	{ rm -R venv || echo "" ; } && \
	{ python$(PYTHON_VERSION) -m venv venv || py -$(PYTHON_VERSION) -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade setuptools && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r dev_requirements.txt && \
	pip3 install\
	 --upgrade --upgrade-strategy eager\
	 -r test_requirements.txt\
	 -r ci_requirements.txt\
	 snowflake-connector-python~=3.7\
	 -e '.[all]' --upgrade --upgrade-strategy eager && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	make requirements && \
	analytics-orm spark install-snowflake-jdbc-driver && \
	analytics-orm spark install-databricks-jdbc-driver && \
	echo "Success!"

upgrade:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	dependence freeze\
	 -nv '*' '.[all]' pyproject.toml tox.ini ci_requirements.txt\
	 > .requirements.txt && \
	pip3 install --upgrade --upgrade-strategy eager\
	 -r .requirements.txt -e '.[all]' && \
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
	 -e '.[all]' && \
	daves-dev-tools clean && \
	echo "Success!"

requirements:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools requirements update && \
	echo "Success!"

distribute:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools pypi distribute

test:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	if [[ "$$(python -V)" = "Python $(PYTHON_VERSION)."* ]] ;\
	then tox run -r ;\
	else tox run -r --skip-env 'black|mypy|isort|flake8' ;\
	fi

download-tests:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	python$(PYTHON_VERSION) scripts/download_tests.py && \
	make format

format:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	black . && isort . && flake8 && mypy
