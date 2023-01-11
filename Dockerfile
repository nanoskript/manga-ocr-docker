FROM python:3.10-slim-buster

RUN apt-get update
RUN apt-get install -y mecab

RUN pip install --no-cache-dir pdm
ADD ./pyproject.toml ./pdm.lock ./
RUN pdm sync && pdm cache clear

# Load model in advance.
RUN pdm run python3 -c "from manga_ocr import MangaOcr; MangaOcr()"

ADD ./main.py ./

CMD ["pdm", "run", "uvicorn", \
	"--host", "0.0.0.0", "--port", "$PORT", \
	"main:app"]
