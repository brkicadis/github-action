import docker
import subprocess

rc = subprocess.call("generate-release-package.sh")

client = docker.from_env()

CONTAINER_NAME = "web"
client.images.build(tag=CONTAINER_NAME, path='./', dockerfile='./Dockerfile')

#client.images.pull('wirecard/woocommerce-dev')

