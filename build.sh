#/bin/sh
set -e

VERSION=test
JAVA=17
BASE_IMAGE=mcdreforged/mcdreforged:${VERSION}

if [ "$SLIM" == "true" ]; then
  SUFFIX="-slim"
elif [ "$FULL" == "true" ]; then
  SUFFIX="-full"
else
  SUFFIX=""
fi

docker build . -f Dockerfile-base --progress=plain \
  --build-arg "MCDR=${MCDR:-latest}" \
  --build-arg "SLIM=${SLIM:-false}" \
  --build-arg "FULL=${FULL:-false}" \
  -t "${BASE_IMAGE}${SUFFIX}"
exit 0
for distribution in temurin zulu liberica; do
  docker build . -f "Dockerfile-${distribution}" \
    --build-arg "BASE_IMAGE=${BASE_IMAGE}${SUFFIX}" \
    --build-arg "JAVA=${JAVA}" \
    -t "mcdreforged/mcdreforged-${distribution}:${VERSION}-${JAVA}${SUFFIX}"
done
