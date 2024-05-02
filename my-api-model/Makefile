SHELL := bash
install:
	{ rm -R venv || echo "" ; } && \
	{ python3.8 -m venv venv || py -3.8 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r requirements.txt -e '.[all]' && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	echo "Success!"

ci-install:
	{ python3 -m venv venv || py -3 -m venv venv ; } && \
	{ venv/Scripts/activate.bat || . venv/bin/activate ; } && \
	python3 -m pip install --upgrade pip wheel && \
	python3 -m pip install -r requirements.txt -e '.[all]' && \
	echo "Installation complete"

reinstall:
	{ rm -R venv || echo "" ; } && \
	{ python3.8 -m venv venv || py -3.8 -m venv venv ; } && \
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	pip3 install --upgrade pip wheel && \
	pip3 install -r dev_requirements.txt && \
	pip3 install -r test_requirements.txt && \
	pip3 install -r ci_requirements.txt -e '.[all]'  && \
	{ mypy --install-types --non-interactive || echo "" ; } && \
	make requirements && \
	echo "Success!"

upgrade:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools requirements freeze\
	 -nv '*'\
	 . pyproject.toml tox.ini ci_requirements.txt\
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

editable:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	daves-dev-tools install-editable --upgrade-strategy eager && \
	make upgrade

requirements:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	dev-tools requirements update -nv flake8 -e backports.zoneinfo && \
	echo "Success!"

test:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	[[ "$$(python -V)" = "Python 3.8."* ]] && tox -r -p || tox -r -e pytest

distribute:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	dev-tools pypi distribute && \
	echo "Success!"

format:
	{ . venv/bin/activate || venv/Scripts/activate.bat ; } && \
	black . && isort . && flake8 && mypy
