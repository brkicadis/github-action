FROM python:3

RUN pip install docker

COPY generate-release-package.sh /usr/bin/generate-release-package.sh
COPY start-shop-system.py /usr/bin/start-shop-system.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
