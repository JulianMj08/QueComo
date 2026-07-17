PROMPT_EXTRACT_TICKET = """
Extrae esta factura y responde únicamente en JSON con:

- numero_factura
- fecha
- empresa
- nif
- productos (CADA PRODUCTO DEBE DE IR EJEMPLO {"nombre": "FIDEO ALIPENDE 1KG CABELLIN", "precio": "1,20\u20ac"} NO "descripcion": "LECHE ALIPENDE 1L ENTERA" NI NINGUN OTRO SINOMIMO)
- subtotal
- iva
- total

Responde solo con el JSON.
"""