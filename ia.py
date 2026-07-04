from ollama import chat

def extraer_factura(ruta_imagen: str):

    response = chat(
        model="qwen2.5vl:3b",
        messages=[
            {
                "role": "user",
                "content": """
Extrae esta factura y responde únicamente en JSON con:

- numero_factura
- fecha
- empresa
- nif
- nombre del producto con su precio
- subtotal
- iva
- total

Responde solo con el JSON.
                """,
                "images": [ruta_imagen]
            }
        ]
    )

    return response.message.content