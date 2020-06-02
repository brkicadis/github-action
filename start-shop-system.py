import docker
import subprocess

client = docker.from_env()

CONTAINER_NAME = "web"
client.images.build(tag=CONTAINER_NAME, path='./', dockerfile='./Dockerfile')

client.containers.run('web', 'wp core install --allow-root --url="http://localhost" --admin_password="password" --title=test --admin_user=admin --admin_email=test@test.com', detach=True)
client.containers.run('web', 'wp plugin activate woocommerce --allow-root', detach=True)
client.containers.run('web', 'wp plugin activate wirecard-woocommerce-extension --allow-root', detach=True)
client.containers.run('web', 'wp plugin install wordpress-importer --activate --allow-root', detach=True)
client.containers.run('web', 'wp import /var/www/html/wp-content/plugins/woocommerce/sample-data/sample_products.xml --allow-root --authors=create', detach=True)
client.containers.run('web', 'wp theme install storefront --activate --allow-root', detach=True)
client.containers.run('web', 'wp wc tool run install_pages --user=admin --allow-root', detach=True)

subprocess.call(["php", "composer.phar", "require", "wirecard/shopsystem-ui-testsuite:dev-master"], shell=True)

subprocess.call(["docker", "images"], shell=True)
subprocess.call(["docker", "ps"], shell=True)

client.containers.run('web', 'vendor/bin/codecept run acceptance -g woocommerce --debug --html')

