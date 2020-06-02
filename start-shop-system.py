import docker
import subprocess

rc2 = subprocess.call("ls")

client = docker.from_env()

CONTAINER_NAME = "web"
client.images.build(tag=CONTAINER_NAME, path='./', dockerfile='./Dockerfile')
client.images.list()
client.containers.list()
# client.images.pull('wirecard/woocommerce-dev')

