.PHONY:
	install
	clean
	requirements
.DEFAULT_GOAL := install

install:
	python3.6 -m venv venv &&\
	venv/bin/pip3 install -r requirements.txt -e '.[test,dev]'\
	 --extra-index-url\
	 https://artifactory.company.com/artifactory/api/pypi/python-virtual/simple\
	 --trusted-host artifactory.company.com

clean:
	venv/bin/daves-dev-tools clean

requirements:
	venv/bin/company-myteam-dev-tools requirements update\
	 -r requirements.txt\
	 setup.py


