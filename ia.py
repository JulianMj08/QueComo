from ollama import chat
import json

from prompts import PROMPT_EXTRACT_TICKET

def extract_ticket(route_img: str):

    response = chat(
        model="qwen2.5vl:3b",
        format="json",
        messages=[
            {
                "role": "user",
                "content": PROMPT_EXTRACT_TICKET,
                "images": [route_img]
            }
        ]
    )

    return json.loads(response.message.content)
    # return response.message.content