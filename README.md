> [!CAUTION]
> Still in early stages of development, expect forced pushes and breaking changes!

# MCDReforged-Docker

Official docker images for [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)

## Usages

### Quick start

Quick test if the docker and image works

```bash
docker run -it --rm mcdreforged/mcdreforged
```

### Persist your server data

For a production usage, you need to persist the working directory: `/mcdr`,
where all MCDR related files and the server folder is in

```bash
docker run --name my_mcdr -v /path/to/my/server:/mcdr mcdreforged/mcdreforged
```

### Python package installation

If you want to installed custom python packages, you can:

1. Mount path `/root/.local/lib/python${PYTHON_VERSION}/site-packages/` to a volume or a local directory 
    - `PYTHON_VERSION` is the major + minor version of the python interpreter, e.g. `3.11`
    - This step is optional. Installing without the directory mounted results in the loss of the new packages when the container is removed
2. Use `pip3` to install whatever packages you want like usual. The `--user` argument is set automatically globally

   ```bash
   $ docker exec -it my_mcdr pip3 install requests
   ```

## Images

### Base

[![Docker](https://img.shields.io/docker/v/mcdreforged/mcdreforged/latest)](https://hub.docker.com/r/mcdreforged/mcdreforged)

Built at https://github.com/Fallen-Breath/MCDReforged

Default Python version: 3.11

```bash
mcdreforged/mcdreforged:latest
mcdreforged/mcdreforged:latest-slim
mcdreforged/mcdreforged:2.13.0
mcdreforged/mcdreforged:2.13.0-slim
mcdreforged/mcdreforged:2.13.0-py3.11
mcdreforged/mcdreforged:2.13.0-py3.11-slim
```

### Extra

Image with extra python packages

Theses extra packages are collected from the [Plugin Catalogue](https://github.com/MCDReforged/PluginCatalogue),
covering almost all required packages of the plugins in the catalogue

See [requirements_common.txt](src/requirements_common.txt) for the full extra package list

```bash
mcdreforged/mcdreforged-extra:latest
mcdreforged/mcdreforged-extra:latest-slim
mcdreforged/mcdreforged-extra:2.13.0
mcdreforged/mcdreforged-extra:2.13.0-slim
mcdreforged/mcdreforged-extra:2.13.0-py3.11
mcdreforged/mcdreforged-extra:2.13.0-py3.11-slim
```

### OpenJDK

Images with OpenJDK installed

Supported OpenJDK distributions:

- [corretoo](https://aws.amazon.com/corretto/)
- [liberica](https://bell-sw.com/libericajdk/)
- [temurin](https://adoptium.net/temurin/)
- [zulu](https://www.azul.com/downloads/?package=jdk#zulu)

Supported java version: 8, 11, 17, 21

Default JDK version: 17

`-extra` suffix means with [extra](#extra) packages

```bash
mcdreforged/mcdreforged-temurin:latest
mcdreforged/mcdreforged-temurin:latest-extra
mcdreforged/mcdreforged-temurin:latest-jdk17
mcdreforged/mcdreforged-temurin:latest-jdk17-extra
mcdreforged/mcdreforged-temurin:latest-slim
mcdreforged/mcdreforged-temurin:latest-slim-extra
mcdreforged/mcdreforged-temurin:latest-slim-jdk17
mcdreforged/mcdreforged-temurin:latest-slim-jdk17-extra

mcdreforged/mcdreforged-temurin:2.13.0
mcdreforged/mcdreforged-temurin:2.13.0-extra
mcdreforged/mcdreforged-temurin:2.13.0-jdk17
mcdreforged/mcdreforged-temurin:2.13.0-jdk17-extra
mcdreforged/mcdreforged-temurin:2.13.0-slim
mcdreforged/mcdreforged-temurin:2.13.0-slim-extra
mcdreforged/mcdreforged-temurin:2.13.0-slim-jdk17
mcdreforged/mcdreforged-temurin:2.13.0-slim-jdk17-extra

mcdreforged/mcdreforged-temurin:2.13.0-py3.11
mcdreforged/mcdreforged-temurin:2.13.0-py3.11-extra
mcdreforged/mcdreforged-temurin:2.13.0-py3.11-jdk17
mcdreforged/mcdreforged-temurin:2.13.0-py3.11-jdk17-extra
mcdreforged/mcdreforged-temurin:2.13.0-py3.11-slim
mcdreforged/mcdreforged-temurin:2.13.0-py3.11-slim-extra
mcdreforged/mcdreforged-temurin:2.13.0-py3.11-slim-jdk17
mcdreforged/mcdreforged-temurin:2.13.0-py3.11-slim-jdk17-extra
```
