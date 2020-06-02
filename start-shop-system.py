import docker
import subprocess

rc2 = subprocess.call("ls")

client = docker.from_env()

CONTAINER_NAME = "web"
client.images.build(tag=CONTAINER_NAME, path='./', dockerfile='./Dockerfile')
print("Image list: ")
client.images.list()
print("Containers list: ")
client.containers.list()
