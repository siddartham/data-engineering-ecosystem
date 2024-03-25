PYTHON_EXECUTABLE: str = "python3"
ARTIFACTORY_HOSTNAME: str = "artifactory.e1.company.com"
PIP_FLAGS: str = (
    f"--trusted-host {ARTIFACTORY_HOSTNAME} "
    "--extra-index-url "
    f"http://{ARTIFACTORY_HOSTNAME}"
    "/artifactory/api/pypi/python-virtual/simple"
)
