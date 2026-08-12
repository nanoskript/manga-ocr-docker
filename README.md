# manga-ocr-docker

[Docker Hub](https://hub.docker.com/r/nanoskript/manga-ocr)
| [Demo](https://manga-ocr.nsk.sh/)

Docker service for <https://github.com/kha-white/manga-ocr>.

## Installation

```
docker run --publish $PORT:$PORT --env PORT=$PORT --detach nanoskript/manga-ocr
```

and navigate to 127.0.0.1:$PORT in your browser.

### CUDA Support

CUDA enabled image available as `nanoskript/manga-ocr-cuda`

You'll need to make sure you have everything set up for docker to access your GPU [as outlined here.](https://saturncloud.io/blog/how-to-use-gpu-from-a-docker-container-a-guide-for-data-scientists-and-software-engineers/)

```
docker run --gpus all --publish $PORT:$PORT --env PORT=$PORT --detach nanoskript/manga-ocr-cuda
```