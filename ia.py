from ollama import chat

response = chat(
    model="qwen2.5vl:3b",
    messages=[
        {
            "role":"user",
            "content":"""
Extrae esta factura y responde únicamente en JSON con:

- numero_factura
- fecha
- empresa
- nif
- nombre del producto con su precio
- subtotal
- iva
- total
            """,
            "images":["factura_1.jpeg"]
        }
    ]
)

print(response.message.content)