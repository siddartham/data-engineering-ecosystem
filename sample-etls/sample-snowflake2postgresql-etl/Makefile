SHELL := bash

dev-install:
	{ python3.8 -m venv venv || py -3.8 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r requirements.txt -e . && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	echo "Dev install success!"

install:
	{ python3.8 -m venv venv || py -3.8 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip && \
	pip3 install -c requirements.txt -e . && \
	echo "Success!"

reinstall:
	{ rm -R venv || echo "" ; } && \
	{ python3.8 -m venv venv || py -3.8 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r test_requirements.txt -r ci_requirements.txt -e '.[all]' && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	make requirements && \
	echo "Success!"

ci-install:
	{ python3 -m venv venv || py -3 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	python3 -m pip install --upgrade pip wheel && \
	python3 -m pip install -r requirements.txt -e . && \
	echo "Installation complete"

reinstall:
	{ rm -R venv || echo "" ; } && \
	{ python3.8 -m venv venv || py -3.8 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r dev_requirements.txt && \
	pip3 install pyspark~=3.0.1 -r test_requirements.txt -r ci_requirements.txt -e .  && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	make requirements && \
	echo "Success!"

upgrade:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools requirements freeze\
	 -nv '*' . pyproject.toml tox.ini ci_requirements.txt\
	 > .requirements.txt && \
	pip3 install --upgrade --upgrade-strategy eager\
	 pyspark~=3.0.1\
	 -r .requirements.txt -e . && \
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
	make upgrade && \
	echo "Success!"

requirements:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	dev-tools requirements update && \
	python3 -m pip install -e . && \
	dev-tools requirements update \
		sample-snowflake2postgresql-etl \
		-r airflow/code/snowflake2postgresql_etl_requirements.txt && \
	echo "Success!"

test:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	if [[ "$$(python -V)" = "Python 3.8."* ]] ;\
	then tox -r -p -o ;\
	else tox -r -e pytest ;\
	fi

distribute:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	dev-tools pypi distribute

# Make sure to bump the version before running the following
test-dev-dag:
	{ venv/Scripts/activate.bat || . venv/bin/activate ; } && \
	dev-tools pypi distribute --skip-existing && \
	make requirements && \
	dev-tools airflow deploy dev && \
	dev-tools airflow run dev --include snowflake2postgresql_etl
