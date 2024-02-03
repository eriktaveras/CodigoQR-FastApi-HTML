from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import qrcode
from io import BytesIO
from starlette.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from qrcode.image.svg import SvgPathImage, SvgImage, SvgFragmentImage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

class QRCodeInput(BaseModel):
    data: str
    fill_color: str = Field(default="black", alias="fillColor")
    back_color: str = Field(default="white", alias="backgroundColor")
    format: str = Field(default="png", description="Format of the QR code image: png, svg")
    svg_factory: str = Field(default="basic", description="Factory method for SVG generation: basic, fragment, path")

@app.post("/generate_qr")
async def generate_qr_code(qr_input: QRCodeInput):
    data = qr_input.data
    fill_color = qr_input.fill_color
    back_color = qr_input.back_color
    output_format = qr_input.format.lower()
    svg_factory_method = qr_input.svg_factory.lower()

    if not all(c in "0123456789ABCDEFabcdef" for c in fill_color.strip("#")) or not all(c in "0123456789ABCDEFabcdef" for c in back_color.strip("#")):
        raise HTTPException(status_code=400, detail="Invalid color format")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    if output_format == "png":
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img_bytes = BytesIO()
        img.save(img_bytes, format="PNG")
        img_bytes.seek(0)
        return StreamingResponse(img_bytes, media_type="image/png")
    elif output_format == "svg":
        if svg_factory_method == 'basic':
            factory = SvgImage
        elif svg_factory_method == 'fragment':
            factory = SvgFragmentImage
        elif svg_factory_method == 'path':
            factory = SvgPathImage
        else:
            raise HTTPException(status_code=400, detail="Invalid SVG factory method")
        img = qr.make_image(image_factory=factory, fill_color=fill_color, back_color=back_color)
        stream = BytesIO()
        img.save(stream)
        stream.seek(0)
        print(stream.read())  # Solo para depuración, quitar en producción


        return StreamingResponse(stream, media_type="image/svg+xml")
    else:
        raise HTTPException(status_code=400, detail="Unsupported format specified")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
