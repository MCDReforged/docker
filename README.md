> [!CAUTION]
> Still in early stages of development, expect forced pushes and breaking changes!

# MCDReforged-Docker

Official docker images for [MCDReforged](https://github.com/Fallen-Breath/MCDReforged)

## Images

### Base Image

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

### Image with extra packages

Extra packages are collected from the [Plugin Catalogue](https://github.com/MCDReforged/PluginCatalogue),
covering almost all required packages of the plugins in the catalogue

```bash
mcdreforged/mcdreforged-extra:latest
mcdreforged/mcdreforged-extra:latest-slim
mcdreforged/mcdreforged-extra:2.13.0
mcdreforged/mcdreforged-extra:2.13.0-slim
mcdreforged/mcdreforged-extra:2.13.0-py3.11
mcdreforged/mcdreforged-extra:2.13.0-py3.11-slim
```

### Image with OpenJDK

Supported openjdk distributions:

- [corretoo](https://aws.amazon.com/corretto/)
- [liberica](https://bell-sw.com/libericajdk/)
- [temurin](https://adoptium.net/temurin/)
- [zulu](https://www.azul.com/downloads/?package=jdk#zulu)

Default JDK version: 17

`-extra` suffix means with extra packages

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
