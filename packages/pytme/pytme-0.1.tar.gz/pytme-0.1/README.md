# Python Template Matching Engine (PyTME)

A software for template matching on electron microscopy data.

📖 **[Official Documentation](https://kosinskilab.github.io/pyTME/)** | 🚀 **[Installation Guide](https://kosinskilab.github.io/pyTME/quickstart/installation.html)** | 📚 **[API Reference](https://kosinskilab.github.io/pyTME/reference/index.html)**

### Installation

There are three ways to get PyTME up and running:

1. **Install from Source:**
```bash
pip install git+https://github.com/KosinskiLab/pyTME
```

2. **Install from PyPi:**
```bash
pip install pytme
```

3. **Docker Container:**
Build and use the PyTME container from Docker. This assumes a linux/amd64 platform and uses Python 3.11.
```bash
docker build \
	-t pytme \
	--platform linux/amd64 \
	--build-arg PYTHON_VERSION=3.11 \
	-f pytme/docker/Dockerfile
	.
```
🔗 For more on the Docker container, visit the [Docker Hub page](https://hub.docker.com).

---
