# Source for the base container is in:
# https://github.com/analytics-platform/ae-runtime-operators/blob/master/py3.6/Dockerfile
FROM artifactory.orm.com:9001/ae-compute/operators-python36:2.1.3
ARG PYTHON_VERSION=3.8.13
USER root
RUN apt-get update -y && apt-get upgrade -y &&\
 apt-get install -y\
 build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev\
 libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev libsasl2-dev\
 libpq-dev make
WORKDIR /usr/src
# Building python from source seems gratuitous, but I couldn't find another
# way (that actually worked) to install python3.8 on the version of Ubuntu
# used by the base image
RUN curl -O\
 https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz &&\
 tar -xf Python-${PYTHON_VERSION}.tar.xz
WORKDIR /usr/src/Python-${PYTHON_VERSION}
RUN ./configure --enable-optimizations && make -j 4 && make altinstall
COPY . /usr/src/app
WORKDIR /usr/src/app
ENV PIP_INDEX_URL=https://pypi.python.org/simple/
ENV PIP_EXTRA_INDEX_URL=https://artifactory.org.com/artifactory/api/pypi/python-virtual/simple
RUN make install
