SHELL := bash
PYTHON_VERSION := 3.8

dev-install:
	{ python$(PYTHON_VERSION) -m venv venv || py -$(PYTHON_VERSION) -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r requirements.txt -e . && \
	echo "Success!"

ci-install:
	{ python3 -m venv venv || py -3 -m venv venv ; } && \
	{ venv/Scripts/activate.bat || . venv/bin/activate ; } && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r ci_requirements.txt && \
	pip3 install -r requirements.txt && \
	echo "Installation complete"

# This will circumvent pinned requirements from the requirements.txt file,
# and is suitable for use when requirements.txt has versions with
# conflicting dependencies.
reinstall:
	{ rm -R venv || echo "" ; } && \
	{ python$(PYTHON_VERSION) -m venv venv || py -$(PYTHON_VERSION) -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r test_requirements.txt -r ci_requirements.txt -e . && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	make requirements && \
	echo "Success!"

upgrade:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	dependency requirements freeze\
	 -nv '*' . pyproject.toml tox.ini ci_requirements.txt dev_requirements.txt test_requirements.txt daves-dev-tools \
	 > .requirements.txt && \
	pip install --upgrade --upgrade-strategy eager\
	 -r .requirements.txt && \
	rm .requirements.txt && \
	make requirements

distribute:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools distribute --skip-existing

clean:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools uninstall-all\
	 -e dev_requirements.txt\
	 -e ci_requirements.txt\
	 -e test_requirements.txt\
     -e pyproject.toml\
     -e tox.ini\
	 -e . && \
	daves-dev-tools clean && \
	echo "Cleanup completed successfully!"

requirements:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	dependency requirements update\
	 -i more-itertools -aen all\
	 -do \
	 setup.cfg pyproject.toml tox.ini && \
	daves-dev-tools requirements freeze\
	 -nv setuptools -nv filelock -nv platformdirs\
	 . pyproject.toml tox.ini daves-dev-tools\
	 > requirements.txt

test:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	tox -r -p

# Make sure to bump the version before running the following
test-dev-dag:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	dev-tools pypi distribute --skip-existing && \
	make requirements && \
	python3 scripts/copy_incremental_dag.py && \
	databricks-jobs update-libraries sample-tabular-etl-dev && \
	echo 'pip install -r /Workspace/Shared/sustainability/sample-tabular-etl-dev-requirements.txt' > init.sh && \
	databricks-jobs upload\
	 -f airflow/code/sustainability_footprint_etl_requirements.txt /Workspace/Shared/sustainability/sample-tabular-etl-dev-requirements.txt\
	 -f init.sh /Workspace/Shared/sustainability/sample-tabular-etl-dev-init.sh && \
    rm init.sh && \
	databricks-jobs update-init-scripts\
	 -is /Workspace/Shared/sustainability/sample-tabular-etl-dev-init.sh\
	 sample-tabular-etl-dev\
	 sample-tabular-etl-incremental-dev && \
	dev-tools airflow deploy dev && \
	dev-tools airflow run dev --include sample_tabular_etl --detach

format:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	black . && isort . && \
	flake8 --extend-ignore=E501 sample_etl/_business_logic/transform.py && mypy


