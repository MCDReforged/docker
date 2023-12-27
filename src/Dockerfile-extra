ARG BASE_IMAGE_TAG
FROM mcdreforged/mcdreforged:${BASE_IMAGE_TAG}

ARG MCDR=latest
ARG SLIM=false
ARG FULL=false

COPY requirements_common.txt /

# Python packages and and MCDR
RUN <<EOT
set -e
# disable the pip config temporary to install packages to the global storage
export PIP_CONFIG_FILE=/dev/null

pip3 install -r /requirements_common.txt
pip3 install mcdreforged==${MCDR_VERSION}

rm -f /requirements_common.txt
pip3 cache purge
EOT
