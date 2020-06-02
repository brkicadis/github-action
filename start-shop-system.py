import docker
import subprocess

rc1 = subprocess.call("chmod +x generate-release-package.sh")
rc3 = subprocess.call("chmod -R 777 .")
rc = subprocess.call("./generate-release-package.sh")

rc2 = subprocess.call("ls")

client = docker.from_env()

CONTAINER_NAME = "web"
client.images.build(tag=CONTAINER_NAME, path='./', dockerfile='./Dockerfile')

# client.images.pull('wirecard/woocommerce-dev')

