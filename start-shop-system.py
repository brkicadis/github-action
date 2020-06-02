import docker

client = docker.from_env()

WOOCOMMERCE_VERSION = ''
PHP_VERSION = ''

CONTAINER_NAME = "web"
client.images.build(tag=CONTAINER_NAME, path='./', dockerfile='./Dockerfile', buildargs={WOOCOMMERCE_VERSION: '3.8.0', PHP_VERSION: '7.1'})
