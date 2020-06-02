import docker

client = docker.from_env()

CONTAINER_NAME = "web"
client.images.build(tag=CONTAINER_NAME, path='./', dockerfile='./Dockerfile')

client.containers.run('web', 'wp core install --allow-root --url="http://localhost" --admin_password="password" --title=test --admin_user=admin --admin_email=test@test.com', detach=True)

client.containers.list()
