#!/bin/sh -l

set -e

./usr/bin/generate-release-package.sh
python /usr/bin/start-shop-system.py "$1"
