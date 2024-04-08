from shutil import which

SERVER: str = "artifactory.my.com:9001"
DOCKER: str = which("docker") or "docker"
MULTI_PLATFORM_BUILD_CONTEXT: str = "mbuilder"
