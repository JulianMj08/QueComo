from ollama import chat
import json

from prompts import PROMPT_EXTRAER_FACTURA

def extraer_factura(ruta_imagen: str):

    response = chat(
        model="qwen2.5vl:3b",
        format="json",
        messages=[
            {
                "role": "user",
                "content": PROMPT_EXTRAER_FACTURA,
                "images": [ruta_imagen]
            }
        ]
    )

    return json.loads(response.message.content)
    # return response.message.content