import docker
import subprocess

rc2 = subprocess.call("ls")

client = docker.from_env()

CONTAINER_NAME = "web"
client.images.build(tag=CONTAINER_NAME, path='./', dockerfile='./Dockerfile')

rc = subprocess.call("docker ps")

print("Docker images: ")
rc3 = subprocess.call("docker images")


