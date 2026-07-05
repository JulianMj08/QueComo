from ollama import chat

from prompts import PROMPT_EXTRAER_FACTURA

def extraer_factura(ruta_imagen: str):

    response = chat(
        model="qwen2.5vl:3b",
        messages=[
            {
                "role": "user",
                "content": PROMPT_EXTRAER_FACTURA,
                "images": [ruta_imagen]
            }
        ]
    )

    return response.message.content