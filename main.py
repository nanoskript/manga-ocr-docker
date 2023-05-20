import io

from fastapi import FastAPI, File
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from manga_ocr import MangaOcr
from PIL import Image

app = FastAPI(title="manga-ocr-docker")
app.add_middleware(CORSMiddleware, allow_origins=["*"])
mocr = MangaOcr()


@app.get("/", include_in_schema=False)
async def route_index():
    return RedirectResponse("/docs")


@app.post("/manga-ocr", summary="Run OCR on an image.")
async def route_manga_ocr(image: bytes = File()):
    return mocr(Image.open(io.BytesIO(image)))
