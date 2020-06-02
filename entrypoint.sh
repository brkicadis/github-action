#!/bin/sh -l

set -e

sh /usr/bin/generate-release-package.sh
python /usr/bin/start-shop-system.py "$1"
