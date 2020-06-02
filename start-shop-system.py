import docker
import subprocess

rc2 = subprocess.call("ls")

client = docker.from_env()

CONTAINER_NAME = "web"
client.images.build(tag=CONTAINER_NAME, path='./', dockerfile='./Dockerfile')

container = client.containers.run('web', detach=True)

container.logs()

client.containers.exec_run('wp core install --allow-root --url="http://localhost" --admin_password="password" --title=test --admin_user=admin --admin_email=test@test.com', stdout=True)

client.containers.list()


