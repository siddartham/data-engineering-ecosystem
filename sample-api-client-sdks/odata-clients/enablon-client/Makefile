SHELL := bash
install:
	{ python3.8 -m venv venv || py -3.8 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r requirements.txt -e '.' && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	echo "Installation completed successfully!"

ci-install:
	{ python3 -m venv venv || py -3 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	{ python3 -m pip install --upgrade pip || echo "" ; } && \
	python3 -m pip install -r requirements.txt -e '.' && \
	echo "Success!"

upgrade:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools requirements freeze\
	 -nv '*'\
	 . pyproject.toml tox.ini ci_requirements.txt\
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
	echo "Cleanup completed successfully!"

editable:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools install-editable --upgrade-strategy eager && \
	echo "Editable installations completed successfully!" && \
	make upgrade

requirements:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	nike-sustainability-dev-tools requirements update -nv flake8 && \
	echo "Requirements updated successfully!"

test:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	if [[ "$$(python -V)" = "Python 3.8."* ]] ;\
	then tox -r -p -o ;\
	else tox -r -e pytest ;\
	fi
distribute:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	nike-sustainability-dev-tools pypi distribute --skip-existing

remodel:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	python3 scripts/remodel.py && \
	echo "Remodel successful!"

force-remodel:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	python3 scripts/remodel.py -f && \
	echo "Remodel successful!"
